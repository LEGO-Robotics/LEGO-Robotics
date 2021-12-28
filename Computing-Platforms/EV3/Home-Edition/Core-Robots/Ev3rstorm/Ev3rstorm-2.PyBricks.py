#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Color, Direction, Port


BRICK = EV3Brick()

LEFT_MOTOR = Motor(port=Port.B,
                   positive_direction=Direction.CLOCKWISE)
RIGHT_MOTOR = Motor(port=Port.C,
                    positive_direction=Direction.CLOCKWISE)
WHEEL_DIAMETER = 26
AXLE_TRACK = 102
DRIVE_BASE = DriveBase(left_motor=LEFT_MOTOR,
                       right_motor=RIGHT_MOTOR,
                       wheel_diameter=WHEEL_DIAMETER,
                       axle_track=AXLE_TRACK)
DRIVE_BASE.settings(
    straight_speed=300,   # milimeters per second
    straight_acceleration=300,
    turn_rate=90,   # degrees per second
    turn_acceleration=90)

TOUCH_SENSOR = TouchSensor(port=Port.S1)


while True:
    BRICK.screen.load_image(ImageFile.SLEEPING)

    BRICK.light.on(color=Color.ORANGE)

    # TODO: parallel process/thread
    while not TOUCH_SENSOR.pressed():
        BRICK.speaker.play_file(SoundFile.SNORING)

    BRICK.screen.load_image(ImageFile.WINKING)

    BRICK.speaker.play_file(SoundFile.ACTIVATE)

    BRICK.speaker.play_file(SoundFile.EV3)

    BRICK.screen.load_image(ImageFile.NEUTRAL)
    
    BRICK.light.on(color=Color.GREEN)    

    DRIVE_BASE.turn(
        angle=90   # degrees
    )

    DRIVE_BASE.turn(
        angle=-90   # degrees
    )

    while not TOUCH_SENSOR.pressed():
        pass

    BRICK.screen.load_image(ImageFile.TIRED_MIDDLE)

    BRICK.speaker.play_file(SoundFile.GOODBYE)    
