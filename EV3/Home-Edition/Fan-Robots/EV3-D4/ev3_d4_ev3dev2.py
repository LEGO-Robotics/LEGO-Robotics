#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

from random import randint
from time import sleep

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor,
    TouchSensor as FastTouchSensor,
    ColorSensor as FastColorSensor
)
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


class EV3D4(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_C, right_motor_port: str = OUTPUT_B,
            head_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel,
            polarity=Motor.POLARITY_INVERSED,
            fast=fast)

        if fast:
            self.head_motor = FastMediumMotor(address=head_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

            self.color_sensor = FastColorSensor(address=color_sensor_port)

        else:
            self.head_motor = MediumMotor(address=head_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

            self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_beacon_channel = ir_beacon_channel

        self.leds = Leds()
        self.speaker = Sound()

        self.state = 0

    def main_switch_loop(self, driving_speed: float = 75):
        """
        This is the Main Switch Loop that allows you to control EV3-D4 using
        the Remote and at the same time it helps EV3-D4 to utilise its B+C
        motors when these are not used when driving EV3-D4 with Remote Control.

        The logic is simple:
        If buttons of Remote Control are pressed then EV3-D4 goes (B+C motors)
        wherever you command it, else it moves according to the behavioural
        state that is changed upon interacting with its Touch Sensor, else stop
        B+C motors.
        """
        while True:
            if self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                self.steer_driver.stop(brake=True)

                if self.state == 0:
                    self.steer_driver.stop(brake=True)

                elif self.state == 1:
                    self.steer_driver.on_for_rotations(
                        steering=-100,
                        speed=driving_speed,
                        rotations=1.5,
                        brake=True,
                        block=True)

                    self.steer_driver.on_for_rotations(
                        steering=100,
                        speed=driving_speed,
                        rotations=1.5,
                        brake=True,
                        block=True)

                elif self.state == 2:
                    self.steer_driver.on_for_rotations(
                        steering=0,
                        speed=-driving_speed,
                        rotations=0.5,
                        brake=True,
                        block=True)

                    self.steer_driver.on_for_rotations(
                        steering=0,
                        speed=driving_speed,
                        rotations=0.5,
                        brake=True,
                        block=True)

                elif self.state == 3:
                    self.steer_driver.on_for_rotations(
                        steering=0,
                        speed=driving_speed,
                        rotations=0.5,
                        brake=True,
                        block=True)

                    self.steer_driver.on_for_rotations(
                        steering=0,
                        speed=-driving_speed,
                        rotations=0.5,
                        brake=True,
                        block=True)

                self.state = 0

            else:
                self.drive_once_by_ir_beacon()

    def color_sensor_loop(self):
        """
        This is the Color Sensor Loop that supports 4 different behaviors that
        are triggered RANDOMLY!!!
        """
        ...

    def touch_sensor_loop(self):
        """
        This is the Touch Sensor Loop that supports 6 different behaviors that
        are triggered RANDOMLY!!!
        """
        ...

    def main(self, driving_speed: float = 75):
        self.main_switch_loop(driving_speed=driving_speed)

if __name__ == '__main__':
    ev3_d4 = EV3D4()

    ev3_d4.main()
