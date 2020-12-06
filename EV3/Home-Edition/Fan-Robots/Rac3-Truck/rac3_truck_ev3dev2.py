#!/usr/bin/env micropython


from ev3dev2.motor import \
    Motor, LargeMotor, MediumMotor, MoveTank, MoveSteering, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor,
    MoveTank as FastMoveTank,
    MoveSteering as FastMoveSteering
)

from time import sleep


class Rac3Truck:
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            polarity: str = Motor.POLARITY_INVERSED,
            steer_motor_port: str = OUTPUT_A,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        if fast:
            self.tank_driver = \
                FastMoveTank(
                    left_motor_port=left_motor_port,
                    right_motor_port=right_motor_port,
                    motor_class=LargeMotor)
            self.steer_driver = \
                FastMoveSteering(
                    left_motor_port=left_motor_port,
                    right_motor_port=right_motor_port,
                    motor_class=LargeMotor)

            self.steer_motor = FastMediumMotor(address=steer_motor_port)

        else:
            self.tank_driver = \
                MoveTank(
                    left_motor_port=left_motor_port,
                    right_motor_port=right_motor_port,
                    motor_class=LargeMotor)
            self.steer_driver = \
                MoveSteering(
                    left_motor_port=left_motor_port,
                    right_motor_port=right_motor_port,
                    motor_class=LargeMotor)

            self.steer_motor = MediumMotor(address=steer_motor_port)

        self.tank_driver.left_motor.polarity = \
            self.tank_driver.right_motor.polarity = \
            self.steer_driver.left_motor.polarity = \
            self.steer_driver.right_motor.polarity = polarity

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.speaker = Sound()

    def reset(self):
        """
        Always begin with Reset.
        This puts the steering wheel centred in the middle.
        Then you can drive with MoveTank. Mind the speed settings!
        """
        self.steer_motor.on(
            speed=30,
            brake=False,
            block=False)
        sleep(1.5)
        # *** THE BELOW, WHICH IS IDENTICAL, CAUSES A MOTOR JAM MORE OFTEN ***
        # self.steer_motor.on_for_seconds(
        #     speed=30,
        #     seconds=1.5,
        #     brake=False,
        #     block=True)

        self.steer_motor.on_for_degrees(
            speed=-50,
            degrees=120,
            brake=True,
            block=True)

        self.steer_motor.reset()

    def left(self):
        """
        Steer to the Left. This only turns the steering wheel.
        So after steering, use MoveTank to drive. Mind the speed settings!
        """
        if self.steer_motor.position > -65:
            self.steer_motor.on(
                speed=-20,
                brake=False,
                block=False)

            while self.steer_motor.position > -65:
                pass

        self.steer_motor.off(brake=True)

    def steer_left(self):
        if self.steer_motor.position > -65:
            self.steer_motor.on_to_position(
                speed=-20,
                position=-65,
                brake=True,
                block=True)

        else:
            self.steer_motor.off(brake=True)

    def right(self):
        """
        Steer to the Right. This only turns the steering wheel.
        So after steering, use MoveTank to drive. Mind the speed settings!
        """
        if self.steer_motor.position < 65:
            self.steer_motor.on(
                speed=20,
                brake=False,
                block=False)

            while self.steer_motor.position < 65:
                pass

        self.steer_motor.off(brake=True)

    def steer_right(self):
        if self.steer_motor.position < 65:
            self.steer_motor.on_to_position(
                speed=20,
                position=65,
                brake=True,
                block=True)

        else:
            self.steer_motor.off(brake=True)

    def center(self):
        """
        When you want to go forwards again, use Center.
        """
        if self.steer_motor.position < -7:
            self.steer_motor.on(
                speed=20,
                brake=False,
                block=False)

            while self.steer_motor.position < 4:
                pass

        elif self.steer_motor.position > 7:
            self.steer_motor.on(
                speed=-20,
                brake=False,
                block=False)

            while self.steer_motor.position > -4:
                pass

        self.steer_motor.off(brake=True)

        sleep(0.1)

    def steer_center(self):
        if self.steer_motor.position < -7:
            self.steer_motor.on_to_position(
                speed=20,
                position=4,
                brake=True,
                block=True)

        elif self.steer_motor.position > 7:
            self.steer_motor.on_to_position(
                speed=-20,
                position=-4,
                brake=True,
                block=True)

        self.steer_motor.off(brake=True)

        sleep(0.1)

    def drive_once_by_ir_beacon(self, speed: float = 80):
        """
        Remote-control your Rac3 Truck with the IR Beacon
        """
        # forward
        if self.ir_sensor.top_left(channel=self.ir_beacon_channel) and \
                self.ir_sensor.top_right(channel=self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=speed,
                right_speed=speed)

            self.steer_center()

        # backward
        elif self.ir_sensor.bottom_left(channel=self.ir_beacon_channel) and \
                self.ir_sensor.bottom_right(channel=self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=-speed)

            self.steer_center()

        # turn left forward
        elif self.ir_sensor.top_left(channel=self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=60,
                right_speed=100)

            self.steer_left()

        # turn right forward
        elif self.ir_sensor.top_right(channel=self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=100,
                right_speed=60)

            self.steer_right()

        # turn left backward
        elif self.ir_sensor.bottom_left(channel=self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-60,
                right_speed=-100)

            self.steer_left()

        # turn right backward
        elif self.ir_sensor.bottom_right(channel=self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-100,
                right_speed=-60)

            self.steer_right()

        # otherwise stop
        else:
            self.tank_driver.off(brake=False)

            self.steer_center()

    def keep_driving_by_ir_beacon(self, speed: float = 80):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

    def main(self):
        """
        You can control your truck with the IR Beacon
        """
        self.reset()

        sleep(1)

        self.keep_driving_by_ir_beacon()


if __name__ == '__main__':
    RAC3_TRUCK = Rac3Truck()

    RAC3_TRUCK.main()
