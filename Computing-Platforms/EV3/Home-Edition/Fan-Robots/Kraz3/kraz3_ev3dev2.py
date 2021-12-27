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


class Kraz3(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_C, right_motor_port: str = OUTPUT_B,
            wiggle_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast: bool = False,
            debug: bool = False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel,
            polarity=Motor.POLARITY_INVERSED,
            fast=fast,
            debug=debug)

        if fast:
            self.wiggle_motor = FastMediumMotor(address=wiggle_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

            self.color_sensor = FastColorSensor(address=color_sensor_port)

        else:
            self.wiggle_motor = MediumMotor(address=wiggle_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

            self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_beacon_channel = ir_beacon_channel

        self.leds = Leds()
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

        elif self.ir_sensor.beacon(channel=self.ir_beacon_channel):
            self.wiggle_motor.on(
                speed=11,
                brake=False,
                block=False)

        else:
            self.wiggle_motor.off(brake=True)

    def kungfu_manoeuvre_whenever_touched_or_remote_controlled(self):
        while True:
            self.kungfu_manoeuvre_if_touched_or_remote_controlled()

    def react_to_color(self):
        detected_color = self.color_sensor.color

        if detected_color == ColorSensor.COLOR_YELLOW:
            self.speaker.play_file(
                wav_file='/home/robot/sound/Yellow.wav',
                volume=100,
                play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

            self.wiggle_motor.on_for_rotations(
                speed=-86,
                rotations=1,
                brake=True,
                block=True)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Uh-oh.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            sleep(0.5)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Sneezing.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            sleep(0.5)

        elif detected_color == ColorSensor.COLOR_RED:
            self.speaker.play_file(
                wav_file='/home/robot/sound/Shouting.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            for _ in range(randint(1, 6)):
                self.speaker.play_file(
                    wav_file='/home/robot/sound/Smack.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.leds.set_color(
                group='LEFT',
                color='RED',
                pct=1)
            self.leds.set_color(
                group='RIGHT',
                color='RED',
                pct=1)

            self.wiggle_motor.on_for_rotations(
                speed=17,
                rotations=1,
                brake=True,
                block=True)

            self.speaker.play_file(
                wav_file='/home/robot/sound/LEGO.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
            self.speaker.play_file(
                wav_file='/home/robot/sound/MINDSTORMS.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.leds.all_off()

        elif detected_color == ColorSensor.COLOR_BROWN:
            self.speaker.play_file(
                wav_file='/home/robot/sound/Brown.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            sleep(1)

            self.wiggle_motor.on_for_rotations(
                speed=-20,
                rotations=1,
                brake=True,
                block=True)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Crying.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        elif detected_color == ColorSensor.COLOR_GREEN:
            self.speaker.play_file(
                wav_file='/home/robot/sound/Green.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.wiggle_motor.on_for_rotations(
                speed=-40,
                rotations=1,
                brake=True,
                block=True)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Yes.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            sleep(1)

        elif detected_color == ColorSensor.COLOR_BLUE:
            self.speaker.play_file(
                wav_file='/home/robot/sound/Blue.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Fantastic.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Good job.wav',
                volume=100,
                play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

            self.wiggle_motor.on_for_rotations(
                speed=75,
                rotations=1,
                brake=True,
                block=True)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Magic wand.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    def keep_reacting_to_colors(self):
        while True:
            self.react_to_color()

    def main(self):
        while True:
            self.drive_once_by_ir_beacon()

            self.kungfu_manoeuvre_if_touched_or_remote_controlled()

            self.react_to_color()


if __name__ == '__main__':
    KRAZ3 = Kraz3()

    KRAZ3.main()
