#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.button import Button
from ev3dev2.console import Console
from ev3dev2.sound import Sound

from ev3dev2.control.rc_tank import RemoteControlledTank

from time import sleep

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor,
    TouchSensor as FastTouchSensor,
    ColorSensor as FastColorSensor
)


class Kraz3(RemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_C, right_motor_port: str = OUTPUT_B,
            wiggle_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_beacon_channel: int = 1,
            fast=False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity='inversed',
            speed=1000,
            channel=ir_beacon_channel)

        if fast:
            self.wiggle_motor = FastMediumMotor(address=wiggle_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

            self.color_sensor = FastColorSensor(address=color_sensor_port)

        else:
            self.wiggle_motor = MediumMotor(address=wiggle_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

            self.color_sensor = ColorSensor(address=color_sensor_port)

        self.console = Console()
        self.speaker = Sound()

    def kungfu_manoeuvre_if_touched_or_remote_controlled(self):
        """
        Kung-Fu manoeuvre via Touch Sensor and Remote Control of head and arms
        """
        if self.touch_sensor.is_pressed:
            self.speaker.play_file(
                wav_file='/home/robot/sound/Kung fu.wav',
                volume=100,
                play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

            self.wiggle_motor.on_for_rotations(
                speed=50,
                rotations=1,
                brake=True,
                block=True)

        elif self.remote.beacon(channel=self.channel):
            self.wiggle_motor.on(
                speed=11,
                brake=False,
                block=False)

        else:
            self.wiggle_motor.off(brake=True)

    def kungfu_manoeuvre_whenever_touched_or_remote_controlled(self):
        while True:
            self.kungfu_manoeuvre_if_touched_or_remote_controlled()
