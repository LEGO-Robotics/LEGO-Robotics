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

    def drive_or_operate_lift_once_by_ir_beacon(
            self,
            speed: float = 1000   # degrees per second
            ):
        # lower the lift
        if self.remote_control.red_up and self.remote_control.red_down:
            self.reversing = False

            self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
            self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

            self.lift_motor.run_forever(speed_sp=100)

        # raise the lift
        if self.remote_control.blue_up and self.remote_control.blue_down:
            self.reversing = False

            self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
            self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

            self.lift_motor.run_forever(speed_sp=-100)

        # forward
        if self.remote_control.red_up and self.remote_control.blue_up:
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

    def keep_driving_or_operating_lift_by_ir_beacon(
            self,
            speed: float = 1000   # degrees per second
            ):
        while True:
            self.drive_or_operate_lift_once_by_ir_beacon(speed=speed)

    def sound_alarm_if_reversing(self):
        if self.reversing:
            if not self.playing_sound:
                self.playing_sound = True

                self.speaker.play(
                    wav_file='/home/robot/sound/Backing alert.wav').wait()

        elif self.playing_sound:
            self.playing_sound = False

        sleep(0.01)

    def sound_alarm_whenever_reversing(self):
        while True:
            self.sound_alarm_if_reversing()
