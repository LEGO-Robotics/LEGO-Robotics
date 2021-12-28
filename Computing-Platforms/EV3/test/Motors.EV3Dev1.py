#!/usr/bin/env python3


from ev3dev.ev3 import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D


MOTOR_0 = LargeMotor(address=OUTPUT_B)
MOTOR_1 = LargeMotor(address=OUTPUT_C)

MOTOR_0.run_forever(speed_sp=100)
MOTOR_1.run_forever(speed_sp=100)

while True:
    pass
