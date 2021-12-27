#!/usr/bin/env micropython


from ev3dev2.motor import (
    LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
)
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, InfraredSensor, TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

from time import time


TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)

MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)

TOUCH_SENSOR = TouchSensor(address=INPUT_1)
COLOR_SENSOR = ColorSensor(address=INPUT_3)
IR_SENSOR = InfraredSensor(address=INPUT_4)

LEDS = Leds()
SPEAKER = Sound()


while True:
    if IR_SENSOR.proximity < 25:
        TANK_DRIVER.off(brake=True)

        LEDS.animate_police_lights(
            color1=Leds.ORANGE,
            color2=Leds.RED,
            group1=Leds.LEFT,
            group2=Leds.RIGHT,
            sleeptime=0.5,
            duration=5,
            block=True)

        SPEAKER.play_file(
            wav_file='/home/robot/sound/Object.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        SPEAKER.play_file(
            wav_file='/home/robot/sound/Detected.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        SPEAKER.play_file(
            wav_file='/home/robot/sound/Error alarm.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        MEDIUM_MOTOR.on(
            speed=100,
            block=False,
            brake=False)

        TANK_DRIVER.on_for_rotations(
            left_speed=100,
            right_speed=80,
            rotations=1,
            brake=True,
            block=True)

        MEDIUM_MOTOR.on(
            speed=-100,
            block=False,
            brake=False)

        TANK_DRIVER.on_for_rotations(
            left_speed=-100,
            right_speed=-80,
            rotations=1,
            brake=True,
            block=True)

        MEDIUM_MOTOR.off(brake=True)

        TANK_DRIVER.on_for_rotations(
            left_speed=100,
            right_speed=-100,
            rotations=2,
            brake=True,
            block=True)

        TANK_DRIVER.on_for_rotations(
            left_speed=0,
            right_speed=100,
            rotations=1,
            brake=True,
            block=True)

    else:
        LEDS.animate_police_lights(
            color1=Leds.YELLOW,
            color2=Leds.GREEN,
            group1=Leds.LEFT,
            group2=Leds.RIGHT,
            sleeptime=0.5,
            duration=5,
            block=True)

        if time() % 3 < 1.5:
            TANK_DRIVER.on(
                left_speed=50,
                right_speed=100)

        else:
            TANK_DRIVER.on(
                left_speed=100,
                right_speed=50)
