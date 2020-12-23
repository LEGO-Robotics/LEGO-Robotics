#!/usr/bin/env python3


from ev3dev2.motor import MediumMotor, Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.display import Display
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

from random import choice, randint
from threading import Thread
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
        self.screen = Display()
        self.speaker = Sound()

        self.state = 0

    def action_1(self):
        self.state = 1

        for _ in range(2):
            self.screen.image_filename(
                filename='/home/robot/image/Dial 0.bmp',
                clear_screen=True)
            self.screen.update()

            self.speaker.play_file(
                wav_file='/home/robot/sound/Blip 2.wav',
                volume=100,
                play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

            self.leds.animate_flash(
                color='ORANGE',
                groups=('LEFT', 'RIGHT'),
                sleeptime=0.5,
                duration=2,
                block=True)

            sleep(0.1)

            self.leds.animate_flash(
                color='GREEN',
                groups=('LEFT', 'RIGHT'),
                sleeptime=0.5,
                duration=2,
                block=True)

            sleep(0.1)

            self.leds.animate_flash(
                color='RED',
                groups=('LEFT', 'RIGHT'),
                sleeptime=0.5,
                duration=2,
                block=True)

            sleep(0.1)

        self.speaker.play_file(
            wav_file='/home/robot/sound/Blip 3.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    def action_2(self):
        self.screen.image_filename(
            filename='/home/robot/image/Dial 1.bmp',
            clear_screen=True)
        self.screen.update()

        self.speaker.play_file(
            wav_file='/home/robot/sound/Confirm.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        self.speaker.play_file(
            wav_file='/home/robot/sound/Walk.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        self.shake_head(left_first=True)

        self.leds.set_color(
            group='LEFT',
            color='RED',
            pct=1)
        self.leds.set_color(
            group='RIGHT',
            color='RED',
            pct=1)

    def action_3(self):
        self.screen.image_filename(
            filename='/home/robot/image/Dial 3.bmp',
            clear_screen=True)
        self.screen.update()

        self.speaker.play_file(
            wav_file='/home/robot/sound/Overpower.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        self.speaker.play_file(
            wav_file='/home/robot/sound/Arm 1.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        self.speaker.play_file(
            wav_file='/home/robot/sound/Servo 2.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        self.shake_head(
            left_first=False,
            n_times=3)

        self.speaker.play_file(
            wav_file='/home/robot/sound/Blip 3.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    def action_4(self):
        self.screen.image_filename(
            filename='/home/robot/image/Dial 4.bmp',
            clear_screen=True)
        self.screen.update()

        self.shake_head(
            left_first=True,
            n_times=2)

        self.speaker.play_file(
            wav_file='/home/robot/sound/Power down.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        self.speaker.play_file(
            wav_file='/home/robot/sound/Ready.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        self.speaker.play_file(
            wav_file='/home/robot/sound/Blip 2.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        self.speaker.play_file(
            wav_file='/home/robot/sound/Blip 1.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        self.speaker.play_file(
            wav_file='/home/robot/sound/Blip 3.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    def action_5(self):
        for _ in range(3):
            self.screen.image_filename(
                filename='/home/robot/image/EV3.bmp',
                clear_screen=True)
            self.screen.update()

            self.leds.set_color(
                group='LEFT',
                color='ORANGE',
                pct=1)
            self.leds.set_color(
                group='RIGHT',
                color='ORANGE',
                pct=1)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Blip 1.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Blip 2.wav',
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

            self.speaker.play_file(
                wav_file='/home/robot/sound/Blip 4.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.leds.set_color(
                group='LEFT',
                color='GREEN',
                pct=1)
            self.leds.set_color(
                group='RIGHT',
                color='GREEN',
                pct=1)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Blip 3.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    def shake_head(self, left_first: bool = True, n_times: int = 1):
        speed_sign = 1 if left_first else -1

        for _ in range(n_times):
            self.head_motor.on_for_degrees(
                speed=speed_sign * 50,
                degrees=100,
                brake=True,
                block=True)

            self.head_motor.on_for_degrees(
                speed=-speed_sign * 50,
                degrees=200,
                brake=True,
                block=True)

            self.head_motor.on_for_degrees(
                speed=speed_sign * 50,
                degrees=100,
                brake=True,
                block=True)

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
            if not (self.ir_sensor.buttons_pressed(channel=1) or
                    self.ir_sensor.buttons_pressed(channel=2) or
                    self.ir_sensor.buttons_pressed(channel=3) or
                    self.ir_sensor.buttons_pressed(channel=4)):
                self.steer_driver.stop(brake=True)

                if self.state == 1:
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

            elif self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                self.shake_head(left_first=choice((False, True)))

            else:
                self.drive_once_by_ir_beacon(speed=driving_speed)

    def color_sensor_loop(self):
        """
        This is the Color Sensor Loop that supports 4 different behaviors that
        are triggered RANDOMLY!!!
        """
        while True:
            if self.color_sensor.color == ColorSensor.COLOR_RED:
                random_number = randint(1, 4)

                if random_number == 1:
                    self.action_1()

                elif random_number == 2:
                    self.action_2()

                elif random_number == 3:
                    self.action_3()

                elif random_number == 4:
                    self.action_4()

    def touch_sensor_loop(self):
        """
        This is the Touch Sensor Loop that supports 5 different behaviors that
        are triggered RANDOMLY!!!
        """
        while True:
            if self.touch_sensor.is_pressed:
                random_number = randint(1, 5)

                if random_number == 1:
                    self.action_1()

                elif random_number == 2:
                    self.state = 2
                    self.action_2()

                elif random_number == 3:
                    self.state = 3
                    self.action_3()

                elif random_number == 4:
                    self.state = 2
                    self.action_4()

                elif random_number == 5:
                    self.state = 3
                    self.action_5()

    def main(self, driving_speed: float = 75):
        Thread(target=self.color_sensor_loop).start()

        Thread(target=self.touch_sensor_loop).start()

        self.main_switch_loop(driving_speed=driving_speed)


if __name__ == '__main__':
    ev3_d4 = EV3D4()

    ev3_d4.main()
