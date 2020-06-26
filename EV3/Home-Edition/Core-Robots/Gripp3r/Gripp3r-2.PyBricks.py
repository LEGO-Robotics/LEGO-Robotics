#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase


EV3_BRICK = EV3Brick()

MEDIUM_MOTOR = Motor(port=Port.A)
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

EV3_BRICK.speaker.play_file(SoundFile.AIRBRAKE)

MEDIUM_MOTOR.run_time(
    speed=50,
    time=1,
    then=Stop.BRAKE,
    wait=True)

TWO_WHEEL_DRIVER   # TODO

TWO_WHEEL_DRIVER   # TODO

MEDIUM_MOTOR.run(speed=-50)

EV3_BRICK.speaker.play_file(SoundFile.AIR_RELEASE)
