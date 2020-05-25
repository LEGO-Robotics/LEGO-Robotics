#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sound import Sound

from time import sleep


MEDIUM_MOTOR = MediumMotor(OUTPUT_A)
SPEAKER = Sound()


MEDIUM_MOTOR.on_for_seconds(
    speed=-50,
    seconds=1,
    brake=True,
    block=True)

SPEAKER.play_file(
    wav_file='/home/robot/sounds/Airbrake.wav',
    volume=100,
    play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

MEDIUM_MOTOR.on_for_seconds(
    speed=50,
    seconds=1,
    brake=True,
    block=True)

sleep(1)

SPEAKER.play_file(
    wav_file='/home/robot/sounds/Air release.wav',
    volume=100,
    play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

MEDIUM_MOTOR.on_for_seconds(
    speed=-50,
    seconds=1,
    brake=True,
    block=True)
