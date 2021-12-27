#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from ev3dev2.sound import Sound

from multiprocessing import Process
from time import time


TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)

MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)

TOUCH_SENSOR = TouchSensor(address=INPUT_1)
COLOR_SENSOR = ColorSensor(address=INPUT_3)

SPEAKER = Sound()


def run_away_whenever_dark():
    while True:
        if COLOR_SENSOR.ambient_light_intensity < 5:   # 15 not dark enough
            TANK_DRIVER.on_for_seconds(
                left_speed=-80,
                right_speed=-100,
                seconds=1.5,
                brake=True,
                block=True)

            TANK_DRIVER.on_for_seconds(
                left_speed=-100,
                right_speed=100,
                seconds=1.5,
                brake=True,
                block=True)

        else:
            if time() % 3 < 1.5:
                TANK_DRIVER.on(
                    left_speed=50,
                    right_speed=100)

            else:
                TANK_DRIVER.on(
                    left_speed=100,
                    right_speed=50)


def laugh_whenever_touched():
    while True:
        if TOUCH_SENSOR.is_pressed:
            SPEAKER.play_file(
                wav_file='/home/robot/sound/Laughing 1.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            MEDIUM_MOTOR.on_for_rotations(
                speed=100,
                rotations=6,
                brake=True,
                block=True)


Process(target=run_away_whenever_dark).start()

laugh_whenever_touched()
