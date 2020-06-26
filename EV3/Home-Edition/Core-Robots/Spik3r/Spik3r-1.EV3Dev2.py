#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, OUTPUT_D
from ev3dev2.sound import Sound


LARGE_MOTOR = LargeMotor(address=OUTPUT_D)

SPEAKER = Sound()


LARGE_MOTOR.on_for_seconds(
    speed=40,
    seconds=1,
    brake=True,
    block=True)

LARGE_MOTOR.on_for_degrees(
    speed=-75,
    degrees=220,
    brake=True,
    block=True)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Blip 3.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

LARGE_MOTOR.on_for_seconds(
    speed=-100,
    seconds=1,
    block=True,
    brake=True)

LARGE_MOTOR.on_for_seconds(
    speed=100,   # 40 too weak
    seconds=1,
    block=True,
    brake=True)
