#!/usr/bin/env python3


# BUG: https://github.com/ev3dev/ev3dev/issues/1422


from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor

from multiprocessing import Process


TOUCH_SENSOR = TouchSensor(address=INPUT_1)
MOTOR = MediumMotor(address=OUTPUT_A)


def motor_on_when_touched():
    while True:
        if TOUCH_SENSOR.is_pressed:
            MOTOR.on_for_seconds(
                speed=100,
                seconds=1,
                brake=False,
                block=True)


Process(target=motor_on_when_touched,
        daemon=True).start()


while True:
    pass
