#!/usr/bin/env micropython


from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D


MOTOR_PAIR = \
    MoveSteering(
        left_motor_port=OUTPUT_B,
        right_motor_port=OUTPUT_C)

MOTOR_PAIR.on(
    steering=0,
    speed=10)

while True:
    pass
