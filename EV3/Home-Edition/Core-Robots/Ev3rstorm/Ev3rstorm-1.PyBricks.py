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
DRIVE_BASE = DriveBase(left_motor=LEFT_MOTOR,
                       right_motor=RIGHT_MOTOR,
                       wheel_diameter=WHEEL_DIAMETER,
                       axle_track=AXLE_TRACK)
DRIVE_BASE.settings(
    straight_speed=300,   # milimeters per second
    straight_acceleration=300,
    turn_rate=90,   # degrees per second
    turn_acceleration=90)


BRICK.screen.load_image(ImageFile.NEUTRAL)

DRIVE_BASE.straight(
    distance=300   # milimeters
)

BRICK.screen.load_image(ImageFile.MIDDLE_LEFT)

DRIVE_BASE.turn(
    angle=90   # degrees
)

BRICK.screen.load_image(ImageFile.NEUTRAL)

DRIVE_BASE.straight(
    distance=300   # milimeters
)

BRICK.screen.load_image(ImageFile.MIDDLE_RIGHT)

DRIVE_BASE.turn(
    angle=-90   # degrees
)
