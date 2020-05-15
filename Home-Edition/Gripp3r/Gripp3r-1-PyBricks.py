#!/usr/bin/env pybricks-micropython


from pybricks.ev3devices import Motor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Port, Stop

from time import sleep


MEDIUM_MOTOR = Motor(port=Port.A)


MEDIUM_MOTOR.run_time(
    speed=-50,
    time=1,
    then=Stop.BRAKE,
    wait=True)

SoundFile.AIRBRAKE   # TODO

MEDIUM_MOTOR.run_time(
    speed=50,
    time=1,
    then=Stop.BRAKE,
    wait=True)

sleep(1)

SoundFile.AIR_RELEASE   # TODO

MEDIUM_MOTOR.run_time(
    speed=-50,
    time=1,
    then=Stop.BRAKE,
    wait=True)
