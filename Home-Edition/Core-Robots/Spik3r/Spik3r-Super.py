#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_B, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor import INPUT_4, INPUT_2, INPUT_1
from ev3dev2.sensor.lego import InfraredSensor, TouchSensor, ColorSensor
from ev3dev2.sound import Sound

from time import sleep


MEDIUM_MOTOR = MediumMotor(OUTPUT_A)
GO_MOTOR = LargeMotor(OUTPUT_B)
STING_MOTOR = LargeMotor(OUTPUT_D)

INFRARED_SENSOR = InfraredSensor(INPUT_4)
TOUCH_SENSOR = TouchSensor(INPUT_1)
COLOR_SENSOR = ColorSensor(INPUT_2)

SPEAKER = Sound()


def sting_if_see_something():
    if INFRARED_SENSOR.proximity <= 30:
        for i in range(3):
            STING_MOTOR.on_for_degrees(
                speed=-75,
                degrees=220,
                brake=True,
                block=False)

            SPEAKER.play_file(
                wav_file='/home/robot/sound/Blip 1.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            STING_MOTOR.on_for_seconds(
                speed=-100,
                seconds=1,
                brake=True,
                block=True)

            STING_MOTOR.on_for_seconds(
                speed=100,
                seconds=1,
                brake=True,
                block=True)

            sleep(1)


def drive_by_ir_beacon(channel=1):
    if INFRARED_SENSOR.top_left(channel=channel) and INFRARED_SENSOR.top_right(channel=channel):
        GO_MOTOR.on(
            speed=91,
            block=False,
            brake=False)

    elif INFRARED_SENSOR.top_right(channel=channel):
        GO_MOTOR.on(
            speed=-100,
            brake=False,
            block=False)

    else:
        GO_MOTOR.off(brake=True)


while True:
    drive_by_ir_beacon(channel=1)
    
    sting_if_see_something()
