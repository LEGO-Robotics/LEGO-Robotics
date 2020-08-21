#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.robotics import DriveBase


EV3_BRICK = EV3Brick()

MEDIUM_MOTOR = Motor(port=Port.A, 
                     positive_direction=Direction.CLOCKWISE)                     

LEFT_MOTOR = Motor(port=Port.B,
                   positive_direction=Direction.CLOCKWISE)
RIGHT_MOTOR = Motor(port=Port.C,
                    positive_direction=Direction.CLOCKWISE)
DRIVE_BASE = DriveBase(left_motor=LEFT_MOTOR,
                       right_motor=RIGHT_MOTOR,
                       wheel_diameter=26,
                       axle_track=115)
DRIVE_BASE.settings(
    straight_speed=750,   # milimeters per second
    straight_acceleration=750,
    turn_rate=90,   # degrees per second
    turn_acceleration=90)

TOUCH_SENSOR = TouchSensor(port=Port.S1)
IR_SENSOR = InfraredSensor(port=Port.S4)


def drive_once_by_ir_beacon(
        channel: int = 1,
        speed: float = 1000   # milimeters per second
    ):
    ir_beacon_buttons_pressed = set(IR_SENSOR.buttons(channel=channel))

    # forward
    if ir_beacon_buttons_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
        DRIVE_BASE.drive(
            speed=speed,
            turn_rate=0   # degrees per second
        )

    # backward
    elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
        DRIVE_BASE.drive(
            speed=-speed,
            turn_rate=0   # degrees per second
        )

    # turn left on the spot
    elif ir_beacon_buttons_pressed == {Button.LEFT_UP, Button.RIGHT_DOWN}:
        DRIVE_BASE.drive(
            speed=0,
            turn_rate=-90   # degrees per second
        )

    # turn right on the spot
    elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN, Button.RIGHT_UP}:
        DRIVE_BASE.drive(
            speed=0,
            turn_rate=90   # degrees per second
        )

    # turn left forward
    elif ir_beacon_buttons_pressed == {Button.LEFT_UP}:
        DRIVE_BASE.drive(
            speed=speed,
            turn_rate=-90   # degrees per second
        )

    # turn right forward
    elif ir_beacon_buttons_pressed == {Button.RIGHT_UP}:
        DRIVE_BASE.drive(
            speed=speed,
            turn_rate=90   # degrees per second
        )

    # turn left backward
    elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN}:
        DRIVE_BASE.drive(
            speed=-speed,
            turn_rate=90   # degrees per second
        )

    # turn right backward
    elif ir_beacon_buttons_pressed == {Button.RIGHT_DOWN}:
        DRIVE_BASE.drive(
            speed=-speed,
            turn_rate=-90   # degrees per second
        )

    # otherwise stop
    else:
        DRIVE_BASE.stop()


while True:
    drive_once_by_ir_beacon(speed=1000)

    if Button.BEACON in IR_SENSOR.buttons(channel=1):
        if TOUCH_SENSOR.pressed():
            MEDIUM_MOTOR.run_time(
                speed=500,
                time=1000,
                then=Stop.BRAKE,
                wait=True)

        else:
            MEDIUM_MOTOR.run(speed=-500)

            while not TOUCH_SENSOR.pressed():
                pass

            MEDIUM_MOTOR.stop()

        while Button.BEACON in IR_SENSOR.buttons(channel=1):
            pass
