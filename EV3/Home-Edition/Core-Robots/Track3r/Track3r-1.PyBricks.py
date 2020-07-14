#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Direction, Port, Stop


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
    straight_speed=300,   # milimeters per second
    straight_acceleration=300,
    turn_rate=90,   # degrees per second
    turn_acceleration=90)


BRICK.screen.load_image(ImageFile.PINCHED_LEFT)

DRIVE_BASE.straight(distance=100)

MEDIUM_MOTOR.run_angle(
    speed=750,
    rotation_angle=3 * 360,
    then=Stop.COAST,
    wait=True)

DRIVE_BASE.straight(distance=-100)

BRICK.speaker.play_file(file=SoundFile.FANFARE)
