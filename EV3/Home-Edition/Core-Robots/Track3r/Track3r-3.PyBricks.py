#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Direction, Port, Stop

from time import sleep


BRICK = EV3Brick()

MEDIUM_MOTOR = Motor(port=Port.A, 
                     positive_direction=Direction.CLOCKWISE)

LEFT_MOTOR = Motor(port=Port.B,
                   positive_direction=Direction.CLOCKWISE)
RIGHT_MOTOR = Motor(port=Port.C,
                    positive_direction=Direction.CLOCKWISE)
WHEEL_DIAMETER = 26
AXLE_TRACK = 140
DRIVE_BASE = DriveBase(left_motor=LEFT_MOTOR,
                       right_motor=RIGHT_MOTOR,
                       wheel_diameter=WHEEL_DIAMETER,
                       axle_track=AXLE_TRACK)
DRIVE_BASE.settings(
    straight_speed=250,   # milimeters per second
    straight_acceleration=250,
    turn_rate=90,   # degrees per second
    turn_acceleration=90)


MEDIUM_MOTOR.run(speed=-1000)

for i in range(2):
    DRIVE_BASE.straight(distance=2)

    MEDIUM_MOTOR.run(speed=-1000)


    BRICK.speaker.play_file(file=SoundFile.AIRBRAKE)

    sleep(0.5)

    DRIVE_BASE.turn(angle=35)

    MEDIUM_MOTOR.run(speed=-1000)

    MEDIUM_MOTOR.stop()
    
    BRICK.speaker.play_file(file=SoundFile.AIR_RELEASE)

    sleep(0.5)

    DRIVE_BASE.turn(angle=-35)

DRIVE_BASE.straight(distance=-4)

BRICK.speaker.play_file(file=SoundFile.CHEERING)
