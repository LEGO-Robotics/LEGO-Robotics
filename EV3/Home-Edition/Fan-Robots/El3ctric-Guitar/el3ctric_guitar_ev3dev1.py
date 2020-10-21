#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_D,
    TouchSensor, InfraredSensor, INPUT_1, INPUT_4,
    Sound
)

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

        self.lever_motor.run_timed(
            speed_sp=50,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_COAST)
        self.lever_motor.wait_while(Motor.STATE_RUNNING)

        self.lever_motor.run_to_rel_pos(
            speed_sp=50,
            position_sp=-30,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.lever_motor.wait_while(Motor.STATE_RUNNING)

        sleep(0.1)

        self.lever_motor.reset()

    def read_lever(self):
        self.lever = 0 \
            if -4 <= self.lever_motor.position <= 4 \
            else self.lever_motor.position

    def keep_reading_lever(self):
        while True:
            self.read_lever()
