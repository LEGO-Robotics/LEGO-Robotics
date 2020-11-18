#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.console import Console
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    LargeMotor as FastLargeMotor,
    MediumMotor as FastMediumMotor,
    TouchSensor as FastTouchSensor
)

from random import randint
from time import sleep, time


class Wack3m:
    N_WACK_TIMES = 10

    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            middle_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, ir_sensor_port: str = INPUT_4,
            fast=False):
        if fast:
            self.left_motor = FastLargeMotor(address=left_motor_port)
            self.right_motor = FastLargeMotor(address=right_motor_port)
            self.middle_motor = FastMediumMotor(address=middle_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

        else:
            self.left_motor = LargeMotor(address=left_motor_port)
            self.right_motor = LargeMotor(address=right_motor_port)
            self.middle_motor = MediumMotor(address=middle_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)

        self.console = Console()
        self.leds = Leds()
        self.speaker = Sound()

    def start_up(self):
        self.leds.animate_flash(
            color='RED',
            groups=('LEFT', 'RIGHT'),
            sleeptime=0.5,
            duration=1,
            block=True)

        self.console.text_at(
            column=5, row=2,
            text='WACK3M',
            reset_console=True,
            inverse=False,
            alignment='L')

        self.left_motor.on_for_seconds(
            speed=-30,
            seconds=1,
            brake=True,
            block=True)

        self.left_motor.reset()

        self.middle_motor.on_for_seconds(
            speed=-5,
            seconds=2,
            brake=True,
            block=True)

        self.middle_motor.reset()

        self.right_motor.on_for_seconds(
            speed=-30,
            seconds=1,
            brake=True,
            block=True)

        self.right_motor.reset()

    def main(self):
        self.start_up()

        while True:
            self.speaker.play_file(
                wav_file='/home/robot/sound/Start.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.leds.animate_flash(
                color='ORANGE',
                groups=('LEFT', 'RIGHT'),
                sleeptime=0.5,
                duration=1,
                block=True)

            self.touch_sensor.wait_for_pressed()

            self.speaker.play_file(
                wav_file='/home/robot/sound/Go.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.leds.animate_flash(
                color='GREEN',
                groups=('LEFT', 'RIGHT'),
                sleeptime=0.5,
                duration=1,
                block=True)

            total_response_time = 0

            sleep(1)

            for _ in range(self.N_WACK_TIMES):
                self.leds.animate_flash(
                    color='GREEN',
                    groups=('LEFT', 'RIGHT'),
                    sleeptime=0.5,
                    duration=1,
                    block=True)

                sleep(0.1 + (3 - 0.1) * randint(1, 10) / 10)

                which_motor = randint(1, 3)

                if which_motor == 1:
                    self.left_motor.on_for_degrees(
                        speed=100,
                        degrees=60,
                        brake=False,
                        block=True)

                    self.left_motor.on_for_seconds(
                        speed=-40,
                        seconds=0.5,
                        brake=True,
                        block=True)

                    proximity = self.ir_sensor.proximity
                    start_time = time()
                    while abs(self.ir_sensor.proximity - proximity) <= 2:
                        pass

                elif which_motor == 2:
                    self.middle_motor.on_for_degrees(
                        speed=50,
                        degrees=170,
                        brake=False,
                        block=True)

                    self.middle_motor.on_for_seconds(
                        speed=-40,
                        seconds=0.4,
                        brake=True,
                        block=True)

                    proximity = self.ir_sensor.proximity
                    start_time = time()
                    while abs(self.ir_sensor.proximity - proximity) <= 3:
                        pass

                else:
                    self.right_motor.on_for_degrees(
                        speed=100,
                        degrees=60,
                        brake=False,
                        block=True)

                    self.right_motor.on_for_seconds(
                        speed=-40,
                        seconds=0.5,
                        brake=True,
                        block=True)

                    proximity = self.ir_sensor.proximity
                    start_time = time()
                    while abs(self.ir_sensor.proximity - proximity) <= 3:
                        pass

                response_time = time() - start_time

                self.console.text_at(
                    column=1, row=1,
                    text='Time: {:.1f}s'.format(response_time),
                    reset_console=True,
                    inverse=False,
                    alignment='L')

                self.leds.animate_flash(
                    color='RED',
                    groups=('LEFT', 'RIGHT'),
                    sleeptime=0.5,
                    duration=1,
                    block=True)

                self.speaker.play_file(
                    wav_file='/home/robot/sound/Boing.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                total_response_time += response_time

            average_response_time = total_response_time / self.N_WACK_TIMES

            self.console.text_at(
                column=1, row=1,
                text='Avg Time: {:.1f}s'.format(average_response_time),
                reset_console=True,
                inverse=False,
                alignment='L')

            self.speaker.play_file(
                wav_file='/home/robot/sound/Fantastic.wav'
                         if average_response_time <= 1
                         else '/home/robot/sound/Good job.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Game over.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.leds.animate_flash(
                color='RED',
                groups=('LEFT', 'RIGHT'),
                sleeptime=0.5,
                duration=1,
                block=True)

            sleep(4)


if __name__ == '__main__':
    WACK3M = Wack3m()

    WACK3M.main()
