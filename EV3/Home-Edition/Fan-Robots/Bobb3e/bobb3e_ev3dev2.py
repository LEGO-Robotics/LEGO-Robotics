#!/usr/bin/env micropython


from ev3dev2.motor import \
    Motor, LargeMotor, MediumMotor, MoveTank, MoveSteering, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.console import Console
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


class Bobb3e:
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            lift_motor_port: str = OUTPUT_A,
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

            self.lift_motor = FastMediumMotor(address=lift_motor_port)

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

            self.lift_motor = MediumMotor(address=lift_motor_port)

        self.tank_driver.left_motor.polarity = \
            self.tank_driver.right_motor.polarity = \
            self.steer_driver.left_motor.polarity = \
            self.steer_driver.right_motor.polarity = Motor.POLARITY_INVERSED

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.console = Console()
        self.speaker = Sound()

        self.reversing = False
        self.playing_sound = False

    def drive_or_operate_lift_once_by_ir_beacon(self, speed: float = 100):
        # lower the lift
        if self.ir_sensor.top_left(channel=self.ir_beacon_channel) and \
                self.ir_sensor.bottom_left(channel=self.ir_beacon_channel):
            self.reversing = False

            self.tank_driver.off(brake=True)

            self.lift_motor.on(
                speed=10,
                brake=False,
                block=False)

        # raise the lift
        elif self.ir_sensor.top_right(channel=self.ir_beacon_channel) and \
                self.ir_sensor.bottom_right(channel=self.ir_beacon_channel):
            self.reversing = False

            self.tank_driver.off(brake=True)

            self.lift_motor.on(
                speed=-10,
                brake=False,
                block=False)

        # forward
        elif self.ir_sensor.top_left(channel=self.ir_beacon_channel) and \
                self.ir_sensor.top_right(channel=self.ir_beacon_channel):
            self.reversing = False

            self.tank_driver.on(
                left_speed=speed,
                right_speed=speed)

            self.lift_motor.off(brake=True)

        # backward
        elif self.ir_sensor.bottom_left(channel=self.ir_beacon_channel) and \
                self.ir_sensor.bottom_right(channel=self.ir_beacon_channel):
            self.reversing = True

            self.tank_driver.on(
                left_speed=-speed,
                right_speed=-speed)

            self.lift_motor.off(brake=True)

        # turn left on the spot
        elif self.ir_sensor.top_left(channel=self.ir_beacon_channel) and \
                self.ir_sensor.bottom_right(channel=self.ir_beacon_channel):
            self.reversing = False

            self.steer_driver.on(
                steering=-100,
                speed=speed)

            self.lift_motor.off(brake=True)

        # turn right on the spot
        elif self.ir_sensor.top_right(channel=self.ir_beacon_channel) and \
                self.ir_sensor.bottom_left(channel=self.ir_beacon_channel):
            self.reversing = False

            self.steer_driver.on(
                steering=100,
                speed=speed)

            self.lift_motor.off(brake=True)

        # turn left forward
        elif self.ir_sensor.top_left(channel=self.ir_beacon_channel):
            self.reversing = False

            self.steer_driver.on(
                steering=-50,
                speed=speed)

            self.lift_motor.off(brake=True)

        # turn right forward
        elif self.ir_sensor.top_right(channel=self.ir_beacon_channel):
            self.reversing = False

            self.steer_driver.on(
                steering=50,
                speed=speed)

            self.lift_motor.off(brake=True)

        # turn left backward
        elif self.ir_sensor.bottom_left(channel=self.ir_beacon_channel):
            self.reversing = True

            self.tank_driver.on(
                left_speed=0,
                right_speed=-speed)

            self.lift_motor.off(brake=True)

        # turn right backward
        elif self.ir_sensor.bottom_right(channel=self.ir_beacon_channel):
            self.reversing = True

            self.tank_driver.on(
                left_speed=-speed,
                right_speed=0)

            self.lift_motor.off(brake=True)

        # otherwise stop
        else:
            self.reversing = False

            self.tank_driver.off(brake=True)

            self.lift_motor.off(brake=True)

    def keep_driving_or_operating_lift_by_ir_beacon(self, speed: float = 100):
        while True:
            self.drive_or_operate_lift_once_by_ir_beacon(speed=speed)

    def sound_alarm_if_reversing(self):
        if self.reversing:
            if not self.playing_sound:
                self.playing_sound = True

                self.speaker.play_file(
                    wav_file='/home/robot/sound/Backing alert.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        elif self.playing_sound:
            self.playing_sound = False

        sleep(0.01)

    def sound_alarm_whenever_reversing(self):
        while True:
            self.sound_alarm_if_reversing()
