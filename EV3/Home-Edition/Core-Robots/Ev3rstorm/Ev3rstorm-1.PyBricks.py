#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import ImageFile
from pybricks.parameters import Direction, Port


BRICK = EV3Brick()

LEFT_MOTOR = Motor(port=Port.B,
                   positive_direction=Direction.CLOCKWISE)
RIGHT_MOTOR = Motor(port=Port.C,
                    positive_direction=Direction.CLOCKWISE)
WHEEL_DIAMETER = 26
AXLE_TRACK = 102
DRIVER = DriveBase(left_motor=LEFT_MOTOR,
                   right_motor=RIGHT_MOTOR,
                   wheel_diameter=WHEEL_DIAMETER,
                   axle_track=AXLE_TRACK)
DRIVER.settings(
    straight_speed=75,
    straight_acceleration=100,
    turn_rate=75,
    turn_acceleration=100)


BRICK.screen.draw_image(
    x=0, y=0,
    source=ImageFile.NEUTRAL)

DRIVER.straight(distance=300)

BRICK.screen.draw_image(
    x=0, y=0,
    source=ImageFile.MIDDLE_LEFT)

DRIVER.turn(angle=90)

BRICK.screen.draw_image(
    x=0, y=0,
    source=ImageFile.NEUTRAL)

DRIVER.straight(distance=300)

BRICK.screen.draw_image(
    x=0, y=0,
    source=ImageFile.MIDDLE_RIGHT)

DRIVER.turn(angle=-90)
