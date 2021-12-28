#!/usr/bin/env python3
# (Display not yet working in MicroPython as of 2020)


from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveSteering, MoveTank
from ev3dev2.display import Display


TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)
STEER_DRIVER = MoveSteering(left_motor_port=OUTPUT_B,
                            right_motor_port=OUTPUT_C,
                            motor_class=LargeMotor)

SCREEN = Display()


SCREEN.image_filename(
    filename='/home/robot/image/Neutral.bmp',
    clear_screen=True)
SCREEN.update()

TANK_DRIVER.on_for_rotations(
    left_speed=75,
    right_speed=75,
    rotations=5,
    brake=True,
    block=True)

SCREEN.image_filename(
    filename='/home/robot/image/Middle left.bmp',
    clear_screen=True)
SCREEN.update()

STEER_DRIVER.on_for_rotations(
    steering=50,
    speed=75,
    rotations=5,
    brake=True,
    block=True)

SCREEN.image_filename(
    filename='/home/robot/image/Neutral.bmp',
    clear_screen=True)
SCREEN.update()

TANK_DRIVER.on_for_rotations(
    left_speed=75,
    right_speed=75,
    rotations=5,
    brake=True,
    block=True)

SCREEN.image_filename(
    filename='/home/robot/image/Middle right.bmp',
    clear_screen=True)
SCREEN.update()

STEER_DRIVER.on_for_rotations(
    steering=-50,
    speed=75,
    rotations=5,
    brake=True,
    block=True)
