#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop


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

IR_SENSOR = InfraredSensor(port=Port.S4)


while True: 
    BRICK.light.on(color=Color.ORANGE)

    if Button.BEACON in IR_SENSOR.buttons(channel=1):
        # TODO: fix to make it work

        distance, heading = IR_SENSOR.beacon(channel=1)
        heading_difference = heading - (-3)
        proximity_difference = distance - 70

        if (heading_difference == 0) and (proximity_difference == 0):
            DRIVER.stop()

            BRICK.light.on(color=Color.RED)

            MEDIUM_MOTOR.run_angle(
                speed=1000,
                rotation_angle=6 * 360,
                then=Stop.HOLD,
                wait=True)

            BRICK.speaker.play_file(file=SoundFile.LAUGHING_2)

        else:
            DRIVER.turn(angle=heading_difference)
            DRIVER.straight(distance=proximity_difference)

    else:
        DRIVER.stop()
