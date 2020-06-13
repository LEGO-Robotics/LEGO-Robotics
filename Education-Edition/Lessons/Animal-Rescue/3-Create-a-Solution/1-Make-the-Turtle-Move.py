#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank


TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B, right_motor_port=OUTPUT_C)


def zigzag(for_seconds: int):
    for i in range(for_seconds // 2):
        TANK_DRIVER.on_for_seconds(
            left_speed=-100,
            right_speed=0,
            seconds=1,
            brake=True,
            block=True)

        TANK_DRIVER.on_for_seconds(
            left_speed=0,
            right_speed=-100,
            seconds=1,
            brake=True,
            block=True)


zigzag(for_seconds=30)
