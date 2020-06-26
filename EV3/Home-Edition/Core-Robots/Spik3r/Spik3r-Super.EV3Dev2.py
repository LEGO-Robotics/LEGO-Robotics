#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_B, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor import INPUT_4, INPUT_2, INPUT_1
from ev3dev2.sensor.lego import InfraredSensor, TouchSensor, ColorSensor
from ev3dev2.sound import Sound

from time import sleep


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
GO_MOTOR = LargeMotor(address=OUTPUT_B)
STING_MOTOR = LargeMotor(address=OUTPUT_D)

INFRARED_SENSOR = InfraredSensor(address=INPUT_4)
TOUCH_SENSOR = TouchSensor(address=INPUT_1)
COLOR_SENSOR = ColorSensor(address=INPUT_2)

SPEAKER = Sound()


def sting_if_see_something():
    if INFRARED_SENSOR.proximity <= 30:
        for i in range(2):
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


def be_noisy_to_people():
    if COLOR_SENSOR.reflected_light_intensity > 30:
        for i in range(4):
            SPEAKER.play_file(
                wav_file='/home/robot/sound/Blip 2.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
            

def pinch_if_touched():
    if TOUCH_SENSOR.is_pressed:
        MEDIUM_MOTOR.on_for_seconds(
            speed=50,
            seconds=1,
            brake=True,
            block=True)

        MEDIUM_MOTOR.on_for_seconds(
            speed=-50,
            seconds=0.3,
            brake=True,
            block=True)


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
    be_noisy_to_people()
    sting_if_see_something()
    pinch_if_touched()
