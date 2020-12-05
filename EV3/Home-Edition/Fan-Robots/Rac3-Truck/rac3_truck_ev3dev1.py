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


class Rac3Truck:
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            polarity: str = Motor.POLARITY_INVERSED,
            turn_motor_port: str = OUTPUT_A,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        if fast:
            self.left_motor = FastLargeMotor(address=left_motor_port)
            self.right_motor = FastLargeMotor(address=right_motor_port)

            self.turn_motor = FastMediumMotor(address=turn_motor_port)

        else:
            self.left_motor = LargeMotor(address=left_motor_port)
            self.right_motor = LargeMotor(address=right_motor_port)

            self.turn_motor = MediumMotor(address=turn_motor_port)

        self.left_motor.polarity = self.right_motor.polarity = polarity

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.remote_control = RemoteControl(sensor=self.ir_sensor,
                                            channel=ir_beacon_channel)

        self.speaker = Sound()

    def reset(self):
        """
        Always begin with Reset.
        This puts the steering wheel centred in the middle.
        Then you can drive with MoveTank. Mind the speed settings!
        """
        self.turn_motor.run_forever(speed=300)

        sleep(1.5)

        self.turn_motor.run_to_rel_pos(
            speed_sp=-500,
            position_sp=120,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.turn_motor.wait_while(Motor.STOP_ACTION_HOLD)

        self.turn_motor.reset()

    def left(self):
        """
        Steer to the Left. This only turns the steering wheel.
        So after steering, use MoveTank to drive. Mind the speed settings!
        """
        if self.turn_motor.position > -65:
            self.turn_motor.run_forever(speed_sp=-200)

            while self.turn_motor.position > -65:
                pass

            self.turn_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        else:
            self.turn_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

    def right(self):
        """
        Steer to the Right. This only turns the steering wheel.
        So after steering, use MoveTank to drive. Mind the speed settings!
        """
        if self.turn_motor.position < 65:
            self.turn_motor.run_forever(speed_sp=200)

            while self.turn_motor.position < 65:
                pass

            self.turn_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        else:
            self.turn_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

    def center(self):
        """
        When you want to go forwards again, use Center.
        """
        ...
