#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound

from time import sleep

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor,
    TouchSensor as FastTouchSensor
)
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank

from dinor3x_util import cyclic_position_offset


class Dinor3x(IRBeaconRemoteControlledTank):
    """
    Challenges:
    - Can you make DINOR3X remote controlled with the IR-Beacon?
    - Can you attach a colorsensor to DINOR3X, and make it behave differently
        depending on which color is in front of the sensor
        (red = walk fast, white = walk slow, etc.)?
    """

    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            jaw_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel,
            fast=fast)

        if fast:
            self.jaw_motor = FastMediumMotor(address=jaw_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

        else:
            self.jaw_motor = MediumMotor(address=jaw_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.button = Button()
        self.speaker = Sound()

    def walk_once_by_ir_beacon(
            self,
            speed: float = 1000   # degrees per second
            ):
        # forward
        if self.ir_sensor.top_left and self.ir_sensor.top_right:
            self.walk(speed=speed)

        # backward
        elif self.ir_sensor.bottom_left and self.ir_sensor.bottom_right:
            self.walk(speed=-speed)

        # turn left on the spot
        elif self.ir_sensor.top_left:
            self.turn(speed=speed)

        # turn right on the spot
        elif self.ir_sensor.top_right:
            self.turn(speed=-speed)

        # stop
        elif self.ir_sensor.bottom_left:
            self.tank_driver.off(brake=True)

        # calibrate legs
        elif self.ir_sensor.bottom_right:
            self.calibrate_legs()

    def keep_walking_by_ir_beacon(self, speed: float):
        while True:
            self.walk_once_by_ir_beacon(speed=speed)

    def open_mouth(self):
        self.jaw_motor.on(
            speed=20,
            block=False,
            brake=False)
        sleep(1)
        self.jaw_motor.off(brake=True)

    def roar(self):
        self.speaker.play_file(
            wav_file='/home/robot/sound/T-rex roar.wav',
            volume=100,
            play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

        self.jaw_motor.on_for_degrees(
            speed=40,
            degrees=-60,
            block=True,
            brake=True)

        for i in range(12):
            self.jaw_motor.on_for_seconds(
                speed=-40,
                seconds=0.05,
                block=True,
                brake=True)

            self.jaw_motor.on_for_seconds(
                speed=40,
                seconds=0.05,
                block=True,
                brake=True)

        self.jaw_motor.on(
            speed=20,
            brake=False,
            block=False)

        sleep(0.5)

    def walk_until_blocked(self):
        self.steer_driver.on(
            steering=0,
            speed=-40)

        while self.ir_sensor.proximity >= 25:
            pass

        self.steer_driver.off(brake=True)

    def run_away(self):
        self.steer_driver.on_for_rotations(
            speed=75,
            steering=0,
            rotations=3,
            brake=True,
            block=True)

    def jump(self):
        """
        Dinor3x Mission 02 Challenge: make it jump
        """
        ...

    # TRANSLATED FROM EV3-G MY BLOCKS
    # -------------------------------

    def calibrate_legs(self):
        self.tank_driver.on(
            left_speed=10,
            right_speed=20)

        self.touch_sensor.wait_for_released()

        self.tank_driver.off(brake=True)

        self.left_motor.on(speed=40)

        self.touch_sensor.wait_for_pressed()

        self.left_motor.off(brake=True)

        self.left_motor.on_for_rotations(
            rotations=-0.2,
            speed=50,
            brake=True,
            block=True)

        self.right_motor.on(speed=40)

        self.touch_sensor.wait_for_pressed()

        self.right_motor.off(brake=True)

        self.right_motor.on_for_rotations(
            rotations=-0.2,
            speed=50,
            brake=True,
            block=True)

        self.left_motor.reset()
        self.right_motor.reset()

    def leg_to_pos(
            self,
            speed: float = 100,
            left_position: float = 0,
            right_position: float = 0):
        self.tank_driver.stop(brake=True)

        self.left_motor.on_for_degrees(
            speed=speed,
            degrees=left_position -
                    cyclic_position_offset(
                        rotation_sensor=self.left_motor.position,
                        cyclic_degrees=360),
            brake=True,
            block=True)

        self.right_motor.on_for_degrees(
            speed=speed,
            degrees=right_position -
                    cyclic_position_offset(
                        rotation_sensor=self.right_motor.position,
                        cyclic_degrees=360),
            brake=True,
            block=True)

    def position_legs(
            self,
            speed: float = 100,
            left_position: float = 0,
            right_position: float = 0):
        self.tank_driver.stop(brake=True)

        self.left_motor.on_for_degrees(
            speed=speed,
            degrees=left_position - self.left_motor.position % 360,
            brake=True,
            block=True)

        self.right_motor.on_for_degrees(
            speed=speed,
            degrees=right_position - self.right_motor.position % 360,
            brake=True,
            block=True)

    def leg_adjust(
            self,
            cyclic_degrees: float = 360,
            speed: float = 100,
            leg_offset_percent: float = 0,
            mirrored_adjust: bool = False,
            brake: bool = True):
        self.tank_driver.stop(brake=True)

        diff = cyclic_position_offset(
                rotation_sensor=self.left_motor.position,
                cyclic_degrees=cyclic_degrees) \
            - cyclic_position_offset(
                rotation_sensor=self.right_motor.position,
                cyclic_degrees=cyclic_degrees)

        if diff > (cyclic_degrees / 2):
            diff -= cyclic_degrees

        if diff < -180:
            diff += cyclic_degrees

        if speed >= 0:
            if diff >= 0:
                self.left_motor.on_for_degrees(
                    speed=-speed,
                    degrees=diff,
                    brake=brake,
                    block=True)

            else:
                self.right_motor.on_for_degrees(
                    speed=-speed,
                    degrees=abs(diff),
                    brake=brake,
                    block=True)

        else:
            if diff >= 0:
                self.right_motor.on_for_degrees(
                    speed=-speed,
                    degrees=diff,
                    brake=brake,
                    block=True)

            else:
                self.left_motor.on_for_degrees(
                    speed=-speed,
                    degrees=abs(diff),
                    brake=brake,
                    block=True)

            # TODO: print to screen

    def adjust_legs(self, speed: float = 100, brake: bool = True):
        self.tank_driver.stop(brake=True)

        diff = (self.left_motor.position % 360) \
            - (self.right_motor.position % 360)

        if diff > 180:
            diff -= 360
        elif diff < -180:
            diff += 360

        if speed >= 0:
            if diff >= 0:
                self.left_motor.on_for_degrees(
                    speed=-speed,
                    degrees=diff,
                    brake=brake,
                    block=True)

            else:
                self.right_motor.on_for_degrees(
                    speed=-speed,
                    degrees=abs(diff),
                    brake=brake,
                    block=True)

        else:
            if diff >= 0:
                self.right_motor.on_for_degrees(
                    speed=-speed,
                    degrees=diff,
                    brake=brake,
                    block=True)

            else:
                self.left_motor.on_for_degrees(
                    speed=-speed,
                    degrees=abs(diff),
                    brake=brake,
                    block=True)

    def walk(self, speed: float = 100):
        # to make legs ready to walk properly
        self.calibrate_legs()

        # self.adjust_legs(
        #     speed=speed,
        #     brake=False)
        # self.leg_adjust(
        #     cyclic_degrees=360,
        #     speed=speed,
        #     leg_offset_percent=0,
        #     mirrored_adjust=False,
        #     brake=False)

        self.steer_driver.on(
            steering=0,
            speed=-speed)

    def walk_n_steps(self, speed: float = 100, n_steps: int = 1):
        ...

    def turn(self, speed: float = 100):
        # to make legs ready to walk properly
        self.calibrate_legs()

        # self.adjust_legs(
        #     speed=speed,
        #     brake=False)
        # self.leg_adjust(
        #     cyclic_degrees=360,
        #     speed=speed,
        #     leg_offset_percent=0,
        #     mirrored_adjust=False,
        #     brake=False)

        if speed >= 0:
            self.left_motor.on_for_degrees(
                degrees=180,
                speed=speed,
                brake=True,
                block=True)

        else:
            self.right_motor.on_for_degrees(
                degrees=180,
                speed=-speed,
                brake=True,
                block=True)

        self.tank_driver.on(
            left_speed=speed,
            right_speed=-speed)

    def turn_n_steps(self, speed: float = 100, n_steps: int = 1):
        ...
