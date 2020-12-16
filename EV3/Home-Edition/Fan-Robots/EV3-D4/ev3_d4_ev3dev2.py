#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

from random import randint
from time import sleep

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor,
    TouchSensor as FastTouchSensor,
    ColorSensor as FastColorSensor
)
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


class Ev3d4(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_C, right_motor_port: str = OUTPUT_B,
            turn_head_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel,
            polarity=Motor.POLARITY_INVERSED,
            fast=fast)

        if fast:
            self.turn_head_motor = FastMediumMotor(address=turn_head_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

            self.color_sensor = FastColorSensor(address=color_sensor_port)

        else:
            self.turn_head_motor = MediumMotor(address=turn_head_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

            self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_beacon_channel = ir_beacon_channel

        self.leds = Leds()
        self.speaker = Sound()

    def main(self):
        while True:
            self.drive_once_by_ir_beacon()


if __name__ == '__main__':
    EV3D4 = Ev3d4()

    EV3D4.main()
