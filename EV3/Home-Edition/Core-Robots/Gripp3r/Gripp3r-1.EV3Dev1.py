#!/usr/bin/env micropython


from ev3dev.ev3 import MediumMotor, OUTPUT_A, Sound

from time import sleep


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
SPEAKER = Sound()


MEDIUM_MOTOR.on_for_seconds(
    speed=-50,
    seconds=1,
    brake=True,
    block=True)

SPEAKER.play(wav_file='/home/robot/sound/Airbrake.wav')

MEDIUM_MOTOR.on_for_seconds(
    speed=50,
    seconds=1,
    brake=True,
    block=True)

sleep(1)

SPEAKER.play(wav_file='/home/robot/sound/Air release.wav')

MEDIUM_MOTOR.on_for_seconds(
    speed=-50,
    seconds=1,
    brake=True,
    block=True)
