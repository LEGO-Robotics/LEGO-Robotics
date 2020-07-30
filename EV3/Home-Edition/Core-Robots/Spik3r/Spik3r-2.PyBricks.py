#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Direction, Port, Stop


BRICK = EV3Brick()

STING_MOTOR = Motor(port=Port.D,
                    positive_direction=Direction.CLOCKWISE)
                
GO_MOTOR = Motor(port=Port.B,   
                 positive_direction=Direction.CLOCKWISE)


STING_MOTOR.run_time(
    speed=400,
    time=1000,
    then=Stop.HOLD,
    wait=True)
    
# This block controls how far SPIK3R crawls.
GO_MOTOR.run_angle(
    speed=1000,
    rotation_angle=3 * 360,
    then=Stop.HOLD,
    wait=True)

BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

GO_MOTOR.run_angle(
    speed=-1000,
    rotation_angle=2 * 360,
    then=Stop.HOLD,
    wait=True)

BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

STING_MOTOR.run_angle(
    speed=-750,
    rotation_angle=220,
    then=Stop.HOLD,
    wait=True)

BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

STING_MOTOR.run_time(
    speed=-1000,
    time=1000,
    then=Stop.HOLD,
    wait=True)

STING_MOTOR.run_time(
    speed=1000,
    time=1000,
    then=Stop.HOLD,
    wait=True)
