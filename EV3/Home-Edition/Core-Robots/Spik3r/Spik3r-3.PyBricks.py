#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Stop, Direction, Port
from pybricks.media.ev3dev import SoundFile


BRICK = EV3Brick()

STING_MOTOR = Motor(port=Port.D,
                    positive_direction=Direction.CLOCKWISE)
                
GO_MOTOR = Motor(port=Port.B,   
                 positive_direction=Direction.CLOCKWISE)

MEDIUM_MOTOR = Motor(port=Port.A,
                     positive_direction=Direction.CLOCKWISE)


MEDIUM_MOTOR.run_time(
    speed=400,
    time=1000,
    then=Stop.HOLD,
    wait=True)

MEDIUM_MOTOR.run_time(
    speed=-400,
    time=0.3000,
    then=Stop.HOLD,
    wait=True)

for i in range(2):
    for i in range(3):
        MEDIUM_MOTOR.run_time(
            speed=750,
            time=0.2000,
            then=Stop.HOLD,
            wait=True)

        MEDIUM_MOTOR.run_time(
            speed=-750,
            time=0.2000,
            then=Stop.HOLD,
            wait=True)

    GO_MOTOR.run_angle(
        speed=1000,
        rotation_angle=3 * 360,
        then=Stop.HOLD,
        wait=True)

    BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

    GO_MOTOR.run_angle(
        speed=1000,
        rotation_angle=-3 * 360,
        then=Stop.HOLD,
        wait=True)

    BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

    GO_MOTOR.run(speed=250)
    
    BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)
