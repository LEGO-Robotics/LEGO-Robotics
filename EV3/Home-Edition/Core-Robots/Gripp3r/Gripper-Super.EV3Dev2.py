#!/usr/bin/env python3

"""
Implementation of Gripp3r
from https://github.com/ev3dev/ev3dev-lang-python-demo/blob/stretch/robots/GRIPP3R/GRIPP3R.py
- use the remote control on channel 1 to drive the robot
- use the remote control on channel 4 to open/close the claw
    - press the top left button to close
    - press the bottom left button to open
- If Gripp3r drives into something solid enough to press the
  TouchSensor underneath the claw will close. Once close the
  remote control must be used to open it.
"""

import logging
import signal
import sys
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, MediumMotor
from ev3dev2.control.rc_tank import RemoteControlledTank
from ev3dev2.sensor.lego import TouchSensor
from threading import Thread, Event
from time import sleep

log = logging.getLogger(__name__)


class MonitorTouchSensor(Thread):
    """
    A thread to monitor Gripper's TouchSensor and close the gripper when
    the TouchSensor is pressed
    """

    def __init__(self, parent):
        Thread.__init__(self)
        self.parent = parent
        self.shutdown_event = Event()
        self.monitor_ts = Event()

    def __str__(self):
        return "MonitorTouchSensor"

    def run(self):

        while True:

            if self.monitor_ts.is_set() and self.parent.ts.is_released:

                # We only wait for 1000ms so that we can wake up to see if
                # our shutdown_event has been set
                if self.parent.ts.wait_for_pressed(timeout_ms=1000):
                    self.parent.claw_close(True)

            if self.shutdown_event.is_set():
                log.info('%s: shutdown_event is set' % self)
                break


class MonitorRemoteControl(Thread):
    """
    A thread to monitor Gripper's InfraredSensor and process signals
    from the remote control
    """

    def __init__(self, parent):
        Thread.__init__(self)
        self.parent = parent
        self.shutdown_event = Event()
        self.monitor_ts = Event()

    def __str__(self):
        return "MonitorRemoteControl"

    def run(self):

        while True:
            self.parent.remote.process()
            sleep(0.01)

            if self.shutdown_event.is_set():
                log.info('%s: shutdown_event is set' % self)
                break


class Gripp3r(RemoteControlledTank):
    """
    To enable the medium motor toggle the beacon button on the EV3 remote.
    """
    CLAW_DEGREES_OPEN = 225
    CLAW_DEGREES_CLOSE = 920
    CLAW_SPEED_PCT = 50

    def __init__(self, left_motor_port=OUTPUT_B, right_motor_port=OUTPUT_C, medium_motor_port=OUTPUT_A):
        RemoteControlledTank.__init__(self, left_motor_port, right_motor_port)
        self.set_polarity(MediumMotor.POLARITY_NORMAL)
        self.medium_motor = MediumMotor(medium_motor_port)
        self.ts = TouchSensor()
        self.mts = MonitorTouchSensor(self)
        self.mrc = MonitorRemoteControl(self)
        self.shutdown_event = Event()

        # Register our signal_term_handler() to be called if the user sends
        # a 'kill' to this process or does a Ctrl-C from the command line
        signal.signal(signal.SIGTERM, self.signal_term_handler)
        signal.signal(signal.SIGINT, self.signal_int_handler)

        self.claw_open(True)
        self.remote.on_channel4_top_left = self.claw_close
        self.remote.on_channel4_bottom_left = self.claw_open

    def shutdown_robot(self):

        if self.shutdown_event.is_set():
            return

        self.shutdown_event.set()
        log.info('shutting down')
        self.mts.shutdown_event.set()
        self.mrc.shutdown_event.set()
        self.remote.on_channel4_top_left = None
        self.remote.on_channel4_bottom_left = None
        self.left_motor.off(brake=False)
        self.right_motor.off(brake=False)
        self.medium_motor.off(brake=False)
        self.mts.join()
        self.mrc.join()

    def signal_term_handler(self, signal, frame):
        log.info('Caught SIGTERM')
        self.shutdown_robot()

    def signal_int_handler(self, signal, frame):
        log.info('Caught SIGINT')
        self.shutdown_robot()

    def claw_open(self, state):
        if state:

            # Clear monitor_ts while we are opening the claw. We do this because
            # the act of opening the claw presses the TouchSensor so we must
            # tell mts to ignore that press.
            self.mts.monitor_ts.clear()
            self.medium_motor.on(speed=self.CLAW_SPEED_PCT * -1, block=True)
            self.medium_motor.off()
            self.medium_motor.reset()
            self.medium_motor.on_to_position(speed=self.CLAW_SPEED_PCT,
                                             position=self.CLAW_DEGREES_OPEN,
                                             brake=False, block=True)
            self.mts.monitor_ts.set()

    def claw_close(self, state):
        if state:
            self.medium_motor.on_to_position(speed=self.CLAW_SPEED_PCT,
                                             position=self.CLAW_DEGREES_CLOSE)

    def main(self):
        self.mts.start()
        self.mrc.start()
        self.shutdown_event.wait()


if __name__ == '__main__':
    GRIPP3R = Gripp3r()
    
    GRIPP3R.main()
