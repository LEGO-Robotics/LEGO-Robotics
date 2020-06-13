#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, OUTPUT_B

from random import randint


LARGE_MOTOR = LargeMotor(OUTPUT_B)


LARGE_MOTOR.on_for_seconds(
    speed=randint(0, 100),
    seconds=randint(1, 5),
    block=True,
    brake=True)

while True:
    LARGE_MOTOR.on_for_seconds(
        speed=randint(-100, 100),
        seconds=randint(1, 5),
        block=True,
        brake=True)
