#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, OUTPUT_B

from time import sleep


LARGE_MOTOR = LargeMotor(address=OUTPUT_B)


def step_leg():
    LARGE_MOTOR.on_for_degrees(
        speed=100,
        degrees=90,
        brake=True,
        block=True)

    sleep(1)

    LARGE_MOTOR.on_for_degrees(
        speed=50,
        degrees=360,
        block=True,
        brake=True)

    
for i in range(3):
    step_leg()
