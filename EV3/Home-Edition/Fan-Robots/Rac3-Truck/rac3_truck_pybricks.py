#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


class Rac3Truck(EV3Brick):
    WHEEL_DIAMETER = 30   # milimeters
    AXLE_TRACK = 120      # milimeters

    def __init__(
            self,
            left_motor_port: str = Port.B, right_motor_port: str = Port.C,
            polarity: str = 'inversed',
            turn_motor_port: str = Port.A,
            ir_sensor_port: str = Port.S4, ir_beacon_channel: int = 1):
        self.left_motor = Motor(port=left_motor_port,
                                positive_direction=
                                    Direction.CLOCKWISE
                                    if polarity == 'normal'
                                    else Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(port=right_motor_port,
                                 positive_direction=
                                    Direction.CLOCKWISE
                                    if polarity == 'normal'
                                    else Direction.COUNTERCLOCKWISE)
        self.drive_base = DriveBase(left_motor=self.left_motor,
                                    right_motor=self.right_motor,
                                    wheel_diameter=self.WHEEL_DIAMETER,
                                    axle_track=self.AXLE_TRACK)

        self.turn_motor = Motor(port=turn_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    def reset(self):
        self.turn_motor.run(speed=300)

        wait(1500)

        self.turn_motor.run_angle(
            speed=-500,
            rotation_angle=120,
            then=Stop.HOLD,
            wait=True)

        self.turn_motor.reset_angle(angle=0)

    def left(self):
        if self.turn_motor.angle() > -65:
            self.turn_motor.run(speed=-200)

            while self.turn_motor.angle() > -65:
                pass

            self.turn_motor.hold()

        else:
            self.turn_motor.hold()

    def right(self):
        if self.turn_motor.angle() < 65:
            self.turn_motor.run(speed=200)

            while self.turn_motor.angle() < 65:
                pass

            self.turn_motor.hold()

        else:
            self.turn_motor.hold()
