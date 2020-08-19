#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Port, Stop, Direction

from time import sleep


EV3_BRICK = EV3Brick()
MEDIUM_MOTOR = Motor(port=Port.A,
                     positive_direction=Direction.COUNTERCLOCKWISE)


MEDIUM_MOTOR.run_time(
    speed=-500,
    time=1000,
    then=Stop.BRAKE,
    wait=True)

EV3_BRICK.speaker.play_file(file=SoundFile.AIRBRAKE)

MEDIUM_MOTOR.run_time(
    speed=500,
    time=1000,
    then=Stop.BRAKE,
    wait=True)

sleep(1)

EV3_BRICK.speaker.play_file(file=SoundFile.AIR_RELEASE)

MEDIUM_MOTOR.run_time(
    speed=500,
    time=1000,
    then=Stop.BRAKE,
    wait=True)
