#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B


LARGE_MOTOR = LargeMotor(OUTPUT_B)
MEDIUM_MOTOR = MediumMotor(OUTPUT_A)


LARGE_MOTOR.on(
    speed=100,
    brake=False,
    block=False)

for i in range(3):   # MUST NOT have spaces between commands within a func/loop in MICROPYTHON
    MEDIUM_MOTOR.on_for_seconds(
        speed=10,
        seconds=1,
        brake=False,
        block=True)
    MEDIUM_MOTOR.on_for_seconds(
        speed=-10,
        seconds=1,
        brake=False,
        block=True)
