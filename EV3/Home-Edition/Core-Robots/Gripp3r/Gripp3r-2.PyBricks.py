#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase


EV3_BRICK = EV3Brick()

MEDIUM_MOTOR = Motor(port=Port.A)
DRIVE_BASE = DriveBase(left_motor=Port.B,
                       right_motor=Port.C,
                       wheel_diameter=...,
                       axle_track=...)


