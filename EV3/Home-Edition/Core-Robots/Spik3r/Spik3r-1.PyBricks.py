#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Direction, Port, Stop


BRICK = EV3Brick()

LARGE_MOTOR = Motor(port=Port.D,
                    positive_direction=Direction.CLOCKWISE)
                    

LARGE_MOTOR.run_time(
    time=1000,
    speed=400,
    then=Stop.HOLD,
    wait=True)

LARGE_MOTOR.run_angle(
    speed=-750,
    rotation_angle=220,
    then=Stop.HOLD,
    wait=True)

BRICK.speaker.play_file(SoundFile.ERROR_ALARM)

LARGE_MOTOR.run_time(
    speed=-1000,
    time=1000,
    then=Stop.HOLD,
    wait=True)

LARGE_MOTOR.run_time(
    speed=1000,
    time=1000,
    then=Stop.HOLD,
    wait=True)
