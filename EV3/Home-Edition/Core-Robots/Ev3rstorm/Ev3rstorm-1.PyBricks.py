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
    straight_speed=300,
    straight_acceleration=300,
    turn_rate=90,
    turn_acceleration=90)


BRICK.screen.load_image(ImageFile.NEUTRAL)

DRIVER.straight(distance=300)

BRICK.screen.load_image(ImageFile.MIDDLE_LEFT)

DRIVER.turn(angle=90)

BRICK.screen.load_image(ImageFile.NEUTRAL)

DRIVER.straight(distance=300)

BRICK.screen.load_image(ImageFile.MIDDLE_RIGHT)

DRIVER.turn(angle=-90)
