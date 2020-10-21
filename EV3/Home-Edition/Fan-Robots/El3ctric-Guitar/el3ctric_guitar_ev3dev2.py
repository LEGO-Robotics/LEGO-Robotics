#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.sound import Sound

from time import sleep

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor,
    TouchSensor as FastTouchSensor
)


class El3ctricGuitar:
    NOTES = [1318, 1174, 987, 880, 783, 659, 587, 493, 440, 392, 329, 293]

    def __init__(
                self,
                lever_motor_port: str = OUTPUT_D,
                touch_sensor_port: str = INPUT_1,
                ir_sensor_port: str = INPUT_4,
                fast=False):
        if fast:
            self.lever_motor = FastMediumMotor(address=lever_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

        else:
            self.lever_motor = MediumMotor(address=lever_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)

        self.speaker = Sound()

        self.lever = 0

        self.lever_motor.on_for_seconds(
            speed=5,
            seconds=1,
            brake=False,
            block=True)

        self.lever_motor.on_for_degrees(
            speed=-5,
            degrees=30,
            brake=True,
            block=True)

        sleep(0.1)

        self.lever_motor.reset()
