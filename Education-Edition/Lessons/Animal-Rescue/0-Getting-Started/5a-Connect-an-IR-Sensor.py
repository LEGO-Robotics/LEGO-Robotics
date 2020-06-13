#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, OUTPUT_B
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4

from time import sleep


LARGE_MOTOR = LargeMotor(OUTPUT_B)
IR_SENSOR = InfraredSensor(INPUT_4)


while True:
    LARGE_MOTOR.on_for_seconds(
        speed=100.0,
        seconds=3.0,
        block=True,
        brake=True)

    LARGE_MOTOR.on_for_seconds(
        speed=-100.0,
        seconds=3.0,
        block=True,
        brake=True)

    if IR_SENSOR.proximity <= 30:
        LARGE_MOTOR.off(brake=True)
        sleep(6)
