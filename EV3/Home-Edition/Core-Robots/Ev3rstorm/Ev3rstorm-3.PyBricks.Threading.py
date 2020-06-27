#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Color, Direction, Port, Stop

from threading import Thread
from time import time


BRICK = EV3Brick()

MEDIUM_MOTOR = Motor(port=Port.A, 
                     positive_direction=Direction.CLOCKWISE)

LEFT_MOTOR = Motor(port=Port.B,
                   positive_direction=Direction.CLOCKWISE)
RIGHT_MOTOR = Motor(port=Port.C,
                    positive_direction=Direction.CLOCKWISE)
WHEEL_DIAMETER = 26
AXLE_TRACK = 102
DRIVER = DriveBase(left_motor=LEFT_MOTOR,
                   right_motor=RIGHT_MOTOR,
                   wheel_diameter=WHEEL_DIAMETER,
                   axle_track=AXLE_TRACK)
DRIVER.settings(
    straight_speed=300,
    straight_acceleration=300,
    turn_rate=90,
    turn_acceleration=90)

TOUCH_SENSOR = TouchSensor(port=Port.S1)

COLOR_SENSOR = ColorSensor(port=Port.S3)


def run_away_whenever_dark():
    while True:
        if COLOR_SENSOR.ambient() < 5:   # 15 not dark enough
            BRICK.screen.load_image(ImageFile.MIDDLE_LEFT)

            DRIVER.straight(distance=-100)

            BRICK.screen.load_image(ImageFile.MIDDLE_RIGHT)

            DRIVER.turn(angle=-135)

        else:
            if time() % 3 < 1.5:
                DRIVER.drive(
                    speed=100,
                    turn_rate=-30)

            else:
                DRIVER.drive(
                    speed=100,
                    turn_rate=30)

            BRICK.screen.load_image(ImageFile.AWAKE)


def laugh_whenever_touched():
    while True:
        if TOUCH_SENSOR.pressed():
            BRICK.speaker.play_file(file=SoundFile.LAUGHING_2)

            MEDIUM_MOTOR.run_angle(
                speed=1000,
                rotation_angle=6 * 360,
                then=Stop.HOLD,
                wait=True)


Thread(target=run_away_whenever_dark).start()

laugh_whenever_touched()
