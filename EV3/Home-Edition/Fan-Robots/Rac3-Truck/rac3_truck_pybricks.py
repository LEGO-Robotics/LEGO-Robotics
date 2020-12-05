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
            steer_motor_port: str = Port.A,
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

        self.steer_motor = Motor(port=steer_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    def reset(self):
        """
        Always begin with Reset.
        This puts the steering wheel centred in the middle.
        Then you can drive with MoveTank. Mind the speed settings!
        """
        self.steer_motor.run_time(
            speed=300,
            time=1500,
            then=Stop.COAST,
            wait=True)

        self.steer_motor.run_angle(
            speed=-500,
            rotation_angle=120,
            then=Stop.HOLD,
            wait=True)

        self.steer_motor.reset_angle(angle=0)

    def left(self):
        """
        Steer to the Left. This only turns the steering wheel.
        So after steering, use MoveTank to drive. Mind the speed settings!
        """
        if self.steer_motor.angle() > -65:
            self.steer_motor.run(speed=-200)

            while self.steer_motor.angle() > -65:
                pass

        self.steer_motor.hold()

    def steer_left(self):
        if self.steer_motor.angle() > -65:
            self.steer_motor.run_target(
                speed=-200,
                target_angle=-65,
                then=Stop.HOLD,
                wait=True)

        else:
            self.steer_motor.hold()

    def right(self):
        """
        Steer to the Right. This only turns the steering wheel.
        So after steering, use MoveTank to drive. Mind the speed settings!
        """
        if self.steer_motor.angle() < 65:
            self.steer_motor.run(speed=200)

            while self.steer_motor.angle() < 65:
                pass

        self.steer_motor.hold()

    def steer_right(self):
        if self.steer_motor.angle() > 65:
            self.steer_motor.run_target(
                speed=200,
                target_angle=65,
                then=Stop.HOLD,
                wait=True)

        else:
            self.steer_motor.hold()

    def center(self):
        """
        When you want to go forwards again, use Center.
        """
        if self.steer_motor.angle() < -7:
            self.steer_motor.run(speed=200)

            while self.steer_motor.angle() < 4:
                pass

        elif self.steer_motor.angle() > 7:
            self.steer_motor.run(speed=-200)

            while self.steer_motor.angle() > -4:
                pass

        self.steer_motor.hold()

        wait(100)

    def steer_center(self):
        if self.steer_motor.angle() < -7:
            self.steer_motor.run_target(
                speed=200,
                target_angle=4,
                then=Stop.HOLD,
                wait=True)

        elif self.steer_motor.angle() > 7:
            self.steer_motor.run_target(
                speed=-200,
                target_angle=-4,
                then=Stop.HOLD,
                wait=True)

        self.steer_motor.hold()

        wait(100)
