#!/usr/bin/env python3


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.console import Console
from ev3dev2.display import Display
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
from time import sleep


class EV3Game:
    def __init__(
            self,
            b_motor_port: str = OUTPUT_B, c_motor_port: str = OUTPUT_C,
            grip_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        if fast:
            self.b_motor = LargeMotor(address=b_motor_port)
            self.c_motor = LargeMotor(address=c_motor_port)

            self.grip_motor = MediumMotor(address=grip_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

        else:
            self.b_motor = FastLargeMotor(address=b_motor_port)
            self.c_motor = FastLargeMotor(address=c_motor_port)

            self.grip_motor = FastMediumMotor(address=grip_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.console = Console()
        self.leds = Leds()
        self.screen = Display()
        self.speaker = Sound()

    def start_up(self):
        self.leds.set_color(
            group='LEFT',
            color='RED',
            pct=1)
        self.leds.set_color(
            group='RIGHT',
            color='RED',
            pct=1)

        self.calibrate_grip()

        self.screen.clear()

        self.level = 1

        self.display_level()

        self.choice = 2

        self.display_cup_number()

        self.offset_holdcup = 60
        self.current_b = self.current_c = 1

    def calibrate_grip(self):
        self.grip_motor.on(
            speed=-10,
            block=False,
            brake=False)

        sleep(0.5)

        self.grip_motor.wait_until_not_moving()

        self.grip_motor.on_for_degrees(
            speed=10,
            degrees=30,
            brake=True,
            block=True)

    def display_level(self):
        ...

    def display_cup_number(self):
        ...

    def select_level(self):
        ...

    def move_1_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = self.offset_holdcup + 180

        elif self.current_b == 2:
            self.rotate_b = 2 * self.offset_holdcup + 180

        elif self.current_b == 3:
            self.rotate_b = 180

    def move_1_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = 0

        elif self.current_c == 2:
            self.rotate_c = -self.offset_holdcup

        elif self.current_c == 3:
            self.rotate_c = self.offset_holdcup

    def move_2_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = self.offset_holdcup + 180

        elif self.current_b == 2:
            self.rotate_b = -180

        elif self.current_b == 3:
            self.rotate_b = 2 * self.offset_holdcup + 180

    def move_2_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = 0

        elif self.current_c == 2:
            self.rotate_c = -self.offset_holdcup

        elif self.current_c == 3:
            self.rotate_c = self.offset_holdcup

    def move_3_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = 0

        elif self.current_b == 2:
            self.rotate_b = self.offset_holdcup

        elif self.current_b == 3:
            self.rotate_b = -self.offset_holdcup

    def move_3_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = self.offset_holdcup + 180

        elif self.current_c == 2:
            self.rotate_c = 180

        elif self.current_c == 3:
            self.rotate_c = 2 * self.offset_holdcup + 180

    def move_4_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = 0

        elif self.current_b == 2:
            self.rotate_b = self.offset_holdcup

        elif self.current_b == 3:
            self.rotate_b = -self.offset_holdcup

    def move_4_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = self.offset_holdcup + 180

        elif self.current_c == 2:
            self.rotate_c = 2 * self.offset_holdcup + 180

        elif self.current_c == 3:
            self.rotate_c = -180

    def execute_move(self):
        speed = 10 * self.level

        if self.rotate_b * self.rotate_c > 0:
            self.b_motor.on_for_degrees(
                speed=speed,
                degrees=self.rotate_b,
                brake=True,
                block=False)
            self.c_motor.on_for_degrees(
                speed=speed,
                degrees=self.rotate_c,
                brake=True,
                block=True)

        elif self.current_b == 1:
            self.b_motor.on_for_degrees(
                speed=speed,
                degrees=self.rotate_b,
                brake=True,
                block=True)

            self.c_motor.on_for_degrees(
                speed=speed,
                degrees=self.rotate_c,
                brake=True,
                block=True)

        else:
            self.c_motor.on_for_degrees(
                speed=speed,
                degrees=self.rotate_c,
                brake=True,
                block=True)

            self.b_motor.on_for_degrees(
                speed=speed,
                degrees=self.rotate_b,
                brake=True,
                block=True)

    def update_ball_cup(self):
        if self.move in {1, 2}:
            if self.cup_with_ball == 1:
                self.cup_with_ball = 2

            elif self.cup_with_ball == 2:
                self.cup_with_ball = 1

        else:
            if self.cup_with_ball == 2:
                self.cup_with_ball = 3

            elif self.cup_with_ball == 3:
                self.cup_with_ball = 2

    def shuffle(self):
        for _ in range(15):
            self.move = randint(1, 4)

            if self.move == 1:
                self.move_1_rotate_b()
                self.move_1_rotate_c()

                self.current_b = 3
                self.current_c = 1

            elif self.move == 2:
                self.move_2_rotate_b()
                self.move_2_rotate_c()

                self.current_b = 2
                self.current_c = 1

            elif self.move == 3:
                self.move_3_rotate_b()
                self.move_3_rotate_c()

                self.current_b = 1
                self.current_c = 2

            elif self.move == 4:
                self.move_4_rotate_b()
                self.move_4_rotate_c()

                self.current_b = 1
                self.current_c = 3

            self.execute_move()

            self.update_ball_cup()

    def select_choice(self):
        ...

    def cup_to_center(self):
        ...

    def main(self):
        self.start_up()

        while True:
            self.cup_with_ball = 2

            self.select_level()

            self.leds.set_color(
                group='LEFT',
                color='GREEN',
                pct=1)
            self.leds.set_color(
                group='RIGHT',
                color='GREEN',
                pct=1)

            self.shuffle()

            self.move_3_rotate_b()

            self.move_1_rotate_c()

            self.current_b = self.current_c = 1

            self.execute_move()

            self.leds.all_off()

            correct_choice = False

            while not correct_choice:
                self.select_choice()

                self.cup_to_center()

                self.grip_motor.on_for_degrees(
                    speed=10,
                    degrees=220,
                    brake=True,
                    block=True)

                correct_choice = (self.cup_with_ball == 2)

                if correct_choice:
                    self.leds.animate_flash(
                        color='GREEN',
                        groups=('LEFT', 'RIGHT'),   # (Leds.LEFT, Leds.RIGHT)
                        sleeptime=0.5,
                        duration=3,
                        block=False)

                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Cheering.wav',
                        volume=100,
                        play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

                else:
                    self.leds.animate_flash(
                        color='RED',
                        groups=('LEFT', 'RIGHT'),   # (Leds.LEFT, Leds.RIGHT)
                        sleeptime=0.5,
                        duration=3,
                        block=False)

                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Boo.wav',
                        volume=100,
                        play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

            sleep(2)

            self.calibrate_grip()


if __name__ == '__main__':
    EV3_GAME = EV3Game()

    EV3_GAME.main()
