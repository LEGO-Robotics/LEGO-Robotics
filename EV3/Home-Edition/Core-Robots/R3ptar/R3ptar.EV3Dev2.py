#!/usr/bin/env python3


import logging
import signal
import sys
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MediumMotor, LargeMotor
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound
from threading import Thread, Event
from time import sleep


log = logging.getLogger(__name__)


class MonitorRemoteControl(Thread):
    """
    A thread to monitor R3PTAR's InfraredSensor and process signals
    from the remote control
    """
    def __init__(self, parent):
        Thread.__init__(self)
        self.parent = parent
        self.shutdown_event = Event()

    def __str__(self):
        return "MonitorRemoteControl"

    def run(self):
        STRIKE_SPEED_PCT = 40

        while True:

            if self.shutdown_event.is_set():
                log.info('%s: shutdown_event is set' % self)
                break

            #log.info("proximity: %s" % self.parent.remote.proximity)
            if self.parent.remote.proximity < 30:
                self.parent.speaker.play('snake-hiss.wav', Sound.PLAY_NO_WAIT_FOR_COMPLETE)
                self.parent.strike_motor.on_for_seconds(speed=STRIKE_SPEED_PCT, seconds=0.5)
                self.parent.strike_motor.on_for_seconds(speed=(STRIKE_SPEED_PCT * -1), seconds=0.5)

            self.parent.remote.process()
            sleep(0.01)


class R3ptar:
    def __init__(self,
                 drive_motor_port=OUTPUT_B,
                 strike_motor_port=OUTPUT_D,
                 steer_motor_port=OUTPUT_A,
                 drive_speed_pct=60):

        self.drive_motor = LargeMotor(drive_motor_port)
        self.strike_motor = LargeMotor(strike_motor_port)
        self.steer_motor = MediumMotor(steer_motor_port)
        self.speaker = Sound()
        STEER_SPEED_PCT = 30

        self.remote = InfraredSensor()
        self.remote.on_channel1_top_left = self.make_move(self.drive_motor, drive_speed_pct)
        self.remote.on_channel1_bottom_left = self.make_move(self.drive_motor, drive_speed_pct * -1)
        self.remote.on_channel1_top_right = self.make_move(self.steer_motor, STEER_SPEED_PCT)
        self.remote.on_channel1_bottom_right = self.make_move(self.steer_motor, STEER_SPEED_PCT * -1)

        self.shutdown_event = Event()
        self.mrc = MonitorRemoteControl(self)

        # Register our signal_term_handler() to be called if the user sends
        # a 'kill' to this process or does a Ctrl-C from the command line
        signal.signal(signal.SIGTERM, self.signal_term_handler)
        signal.signal(signal.SIGINT, self.signal_int_handler)

    def make_move(self, motor, speed):
        def move(state):
            if state:
                motor.on(speed)
            else:
                motor.stop()
        return move

    def shutdown_robot(self):

        if self.shutdown_event.is_set():
            return

        self.shutdown_event.set()
        log.info('shutting down')
        self.mrc.shutdown_event.set()

        self.remote.on_channel1_top_left = None
        self.remote.on_channel1_bottom_left = None
        self.remote.on_channel1_top_right = None
        self.remote.on_channel1_bottom_right = None

        self.drive_motor.off(brake=False)
        self.strike_motor.off(brake=False)
        self.steer_motor.off(brake=False)

        self.mrc.join()

    def signal_term_handler(self, signal, frame):
        log.info('Caught SIGTERM')
        self.shutdown_robot()

    def signal_int_handler(self, signal, frame):
        log.info('Caught SIGINT')
        self.shutdown_robot()

    def main(self):
        self.mrc.start()
        self.shutdown_event.wait()


if __name__ == '__main__':
    R3PTAR = R3ptar()

    R3PTAR.main()
