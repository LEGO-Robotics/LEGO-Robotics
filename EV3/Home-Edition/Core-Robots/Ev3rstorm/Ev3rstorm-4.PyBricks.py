#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Color, Direction, Port

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
    straight_speed=300,   # milimeters per second
    straight_acceleration=300,
    turn_rate=90,   # degrees per second
    turn_acceleration=90)

IR_SENSOR = InfraredSensor(port=Port.S4)


while True:
    if IR_SENSOR.distance() < 25:
        DRIVER.stop()

        BRICK.light.on(color=Color.RED)

        BRICK.speaker.play_file(file=SoundFile.OBJECT)
        BRICK.speaker.play_file(file=SoundFile.DETECTED)
        BRICK.speaker.play_file(file=SoundFile.ERROR_ALARM)

        MEDIUM_MOTOR.run(
            speed=1000   # degrees per second
        )

        DRIVER.straight(
            distance=100   # milimeters
        )

        MEDIUM_MOTOR.run(
            speed=-1000   # degrees per second
        )

        DRIVER.straight(
            distance=-100   # milimeters
        )

        MEDIUM_MOTOR.hold()

        DRIVER.turn(
            angle=135   # degrees
        )

        DRIVER.turn(
            angle=-30   # degrees
        )

    else:
        BRICK.light.on(color=Color.GREEN)

        if time() % 3 < 1.5:
            DRIVER.drive(
                speed=360,   # degrees per second
                turn_rate=-30   # degrees per second
            )

        else:
            DRIVER.drive(
                speed=360,   # degrees per second
                turn_rate=30   # degrees per second
            )
