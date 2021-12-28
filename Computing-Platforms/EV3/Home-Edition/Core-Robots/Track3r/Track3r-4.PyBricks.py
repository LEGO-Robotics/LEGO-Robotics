#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
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
    straight_speed=750,   # milimeters per second
    straight_acceleration=750,
    turn_rate=90,   # degrees per second
    turn_acceleration=90)

IR_SENSOR = InfraredSensor(port=Port.S4)


MEDIUM_MOTOR.run_time(
    speed=-200,   # deg/s
    time=1000,   # ms
    then=Stop.HOLD,
    wait=True)

while True:
    if IR_SENSOR.distance() < 25:
        BRICK.screen.load_image(ImageFile.PINCHED_RIGHT)

        DRIVE_BASE.turn(angle=-180)

        BRICK.screen.load_image(ImageFile.ANGRY)

        MEDIUM_MOTOR.run_time(
            speed=1000,   # deg/s
            time=1000,   # ms
            then=Stop.HOLD,
            wait=True)

        BRICK.speaker.play_file(file=SoundFile.LAUGHING_2)

        MEDIUM_MOTOR.run_time(
            speed=-1000,   # deg/s
            time=1000,   # ms
            then=Stop.HOLD,
            wait=True)

    else:
        BRICK.screen.load_image(ImageFile.CRAZY_1)

        DRIVE_BASE.drive(
            speed=750,
            turn_rate=0)

        MEDIUM_MOTOR.run_time(
            speed=1000,   # deg/s
            time=0.3 * 1000,   # ms
            then=Stop.HOLD,
            wait=True)

        sleep(0.1)

        BRICK.screen.load_image(ImageFile.CRAZY_2)

        DRIVE_BASE.drive(
            speed=750,
            turn_rate=500)

        MEDIUM_MOTOR.run_time(
            speed=-1000,   # deg/s
            time=0.3 * 1000,   # ms
            then=Stop.COAST,
            wait=True)
