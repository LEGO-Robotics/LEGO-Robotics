#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, OUTPUT_B


LARGE_MOTOR = LargeMotor(OUTPUT_B)


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
