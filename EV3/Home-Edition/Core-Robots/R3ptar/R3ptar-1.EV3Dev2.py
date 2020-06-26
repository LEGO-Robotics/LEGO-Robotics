#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B


LARGE_MOTOR = LargeMotor(address=OUTPUT_B)
MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)


LARGE_MOTOR.on(
    speed=100,
    brake=False,
    block=False)

for i in range(3):
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
