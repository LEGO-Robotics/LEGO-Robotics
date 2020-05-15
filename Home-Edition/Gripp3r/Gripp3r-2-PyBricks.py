#!/usr/bin/env pybricks-micropython


from pybricks.ev3devices import Motor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase


MEDIUM_MOTOR = Motor(Port.A)
TWO_WHEEL_DRIVER = DriveBase(left_motor=Port.B,
                             right_motor=Port.C,
                             wheel_diameter=None,  # TODO
                             axle_track=None)


MEDIUM_MOTOR.run_time(
    speed=-50,
    time=1,
    then=Stop.BRAKE,
    wait=True)

TWO_WHEEL_DRIVER   # TODO

SoundFile.AIRBRAKE   # TODO

MEDIUM_MOTOR.run_time(
    speed=50,
    time=1,
    then=Stop.BRAKE,
    wait=True)

TWO_WHEEL_DRIVER   # TODO

TWO_WHEEL_DRIVER   # TODO

MEDIUM_MOTOR.run(speed=-50)

SoundFile.AIR_RELEASE   # TODO
