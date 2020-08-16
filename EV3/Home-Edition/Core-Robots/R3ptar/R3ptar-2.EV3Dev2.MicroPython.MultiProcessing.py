#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound

from multiprocessing import Process
from time import sleep


LARGE_MOTOR = LargeMotor(address=OUTPUT_D)
MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)

IR_SENSOR = InfraredSensor(address=INPUT_4)

SPEAKER = Sound()


def rattle():
    while True:
        MEDIUM_MOTOR.on_for_seconds(
            speed=10,
            seconds=1,
            brake=False,
            block=True)

        SPEAKER.play_file(
            wav_file='/home/robot/sound/Snake rattle.wav',
            volume=50,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        MEDIUM_MOTOR.on_for_seconds(
            speed=-10,
            seconds=1,
            brake=False,
            block=True)

        sleep(1)


def scare_people():
    while True:
        if IR_SENSOR.proximity < 30:
            LARGE_MOTOR.on_for_seconds(
                speed=100,
                seconds=1,
                brake=True,
                block=True)

        else:
            LARGE_MOTOR.on_for_seconds(
                speed=-30,
                seconds=1,
                brake=True,
                block=True)


Process(target=scare_people).start()

rattle()
