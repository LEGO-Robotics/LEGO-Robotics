#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase


EV3_BRICK = EV3Brick()

MEDIUM_MOTOR = Motor(port=Port.A, 
                     positive_direction=Direction.CLOCKWISE)

LEFT_MOTOR = Motor(port=Port.B,
                   positive_direction=Direction.CLOCKWISE)
RIGHT_MOTOR = Motor(port=Port.C,
                    positive_direction=Direction.CLOCKWISE)
DRIVE_BASE = DriveBase(left_motor=LEFT_MOTOR,
                       right_motor=RIGHT_MOTOR,
                       wheel_diameter=26,
                       axle_track=115)
DRIVE_BASE.settings(
    straight_speed=750,   # milimeters per second
    straight_acceleration=750,
    turn_rate=90,   # degrees per second
    turn_acceleration=90)


MEDIUM_MOTOR.run_time(
    speed=-500,
    time=1000,
    then=Stop.COAST,
    wait=True)

DRIVE_BASE.straight(distance=300)

EV3_BRICK.speaker.play_file(file=SoundFile.AIRBRAKE)

MEDIUM_MOTOR.run_time(
    speed=500,
    time=1000,
    then=Stop.COAST,
    wait=True)

DRIVE_BASE.turn(angle=850)

DRIVE_BASE.straight(distance=300)

MEDIUM_MOTOR.run(speed=-500)

EV3_BRICK.speaker.play_file(file=SoundFile.AIR_RELEASE)
