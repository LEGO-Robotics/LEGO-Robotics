#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    InfraredSensor, RemoteControl, INPUT_4,
    Screen, Sound
)

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    LargeMotor as FastLargeMotor,
    MediumMotor as FastMediumMotor
)

from time import sleep


class Bobb3e:
    """
    CHALLENGES:

    Here are some challenges you can try to do in order to make BOBB3E better:

    - Can you make BOBB3E say sounds when he is lifting/lowering his forks?

    - BOBB3E does by default drive rather slow - try to see if you can
    make him go faster!

    - You could utilise that the remote has 4 channels and use that as
    different gears. Say, for instance, that when using Channel 1 is the same
    as driving in 1st gear; very slow. Channel 2 could make him go a little
    faster and using channel 4 would make him go very fast!

    - The remote control can also be used as a Beacon, which BOBB3E is able to
    detect and drive towards. Can you make him automatically find the Beacon
    and lift it, when BOBB3E comes close enough to it?
    """
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            lift_motor_port: str = OUTPUT_A,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        if fast:
            self.left_motor = FastLargeMotor(address=left_motor_port)
            self.right_motor = FastLargeMotor(address=right_motor_port)

            self.lift_motor = FastMediumMotor(address=lift_motor_port)

        else:
            self.left_motor = LargeMotor(address=left_motor_port)
            self.right_motor = LargeMotor(address=right_motor_port)

            self.lift_motor = MediumMotor(address=lift_motor_port)

        self.left_motor.polarity = self.right_motor.polarity = \
            Motor.POLARITY_INVERSED

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.remote_control = RemoteControl(sensor=self.ir_sensor,
                                            channel=ir_beacon_channel)

        self.screen = Screen()
        self.speaker = Sound()

        self.reversing = False
        self.playing_sound = False

    """
    BOBB3E takes advantage of running multiple subprograms;
    one for receiving the commands from the remote control and
    one for handling the reversing alarm.
    """

    def drive_or_operate_forks_once_by_ir_beacon(
            self,
            speed: float = 1000   # degrees per second
            ):
        """
        Read the commands from the remote control and convert them into actions
        such as go forward, lift and turn.
        """
        # lower the forks
        if self.remote_control.red_up and self.remote_control.red_down:
            self.reversing = False

            self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
            self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

            self.lift_motor.run_forever(speed_sp=100)

        # raise the forks
        elif self.remote_control.blue_up and self.remote_control.blue_down:
            self.reversing = False

            self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
            self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

            self.lift_motor.run_forever(speed_sp=-100)

        # forward
        elif self.remote_control.red_up and self.remote_control.blue_up:
            self.reversing = False

            self.left_motor.run_forever(speed_sp=speed)
            self.right_motor.run_forever(speed_sp=speed)

            self.lift_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        # backward
        elif self.remote_control.red_down and self.remote_control.blue_down:
            self.reversing = True

            self.left_motor.run_forever(speed_sp=-speed)
            self.right_motor.run_forever(speed_sp=-speed)

            self.lift_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        # turn left on the spot
        elif self.remote_control.red_up and self.remote_control.blue_down:
            self.reversing = False

            self.left_motor.run_forever(speed_sp=-speed)
            self.right_motor.run_forever(speed_sp=speed)

            self.lift_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        # turn right on the spot
        elif self.remote_control.red_down and self.remote_control.blue_up:
            self.reversing = False

            self.left_motor.run_forever(speed_sp=speed)
            self.right_motor.run_forever(speed_sp=-speed)

            self.lift_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        # turn left forward
        elif self.remote_control.red_up:
            self.reversing = False

            self.right_motor.run_forever(speed_sp=speed)

            self.lift_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        # turn right forward
        elif self.remote_control.blue_up:
            self.reversing = False

            self.left_motor.run_forever(speed_sp=speed)

            self.lift_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        # turn left backward
        elif self.remote_control.red_down:
            self.reversing = True

            self.right_motor.run_forever(speed_sp=-speed)

            self.lift_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        # turn right backward
        elif self.remote_control.blue_down:
            self.reversing = True

            self.left_motor.run_forever(speed_sp=-speed)

            self.lift_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        # otherwise stop
        else:
            self.reversing = False

            self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
            self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

            self.lift_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

    def keep_driving_or_operating_forks_by_ir_beacon(
            self,
            speed: float = 1000   # degrees per second
            ):
        """
        Main Loop
        """
        while True:
            self.drive_or_operate_forks_once_by_ir_beacon(speed=speed)

    def sound_alarm_if_reversing(self):
        """
        Reversing alarm sound:
        - Whenever the Reversing variable is changed to True
        the alarm starts to play.
        - When the value of the Reversing variable is set to False
        the alarm stops.
        """
        if self.reversing:
            if not self.playing_sound:
                self.playing_sound = True

                self.speaker.play(
                    wav_file='/home/robot/sound/Backing alert.wav').wait()

        elif self.playing_sound:
            self.playing_sound = False

        sleep(0.01)

    def sound_alarm_whenever_reversing(self):
        """
        Backing Sound Loop
        """
        while True:
            self.sound_alarm_if_reversing()
