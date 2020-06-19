#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, OUTPUT_D, OUTPUT_B
from ev3dev2.sound import Sound


STING_MOTOR = LargeMotor(OUTPUT_D)
GO_MOTOR = LargeMotor(OUTPUT_B)

SPEAKER = Sound()


STING_MOTOR.on_for_seconds(
    speed=40,
    seconds=1,
    brake=True,
    block=True)

GO_MOTOR.on_for_rotations(
    speed=100,
    rotations=3,
    block=True,
    brake=True)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Blip 2.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

GO_MOTOR.on_for_rotations(
    speed=-100,
    rotations=2,
    block=True,
    brake=True)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Blip 4.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

STING_MOTOR.on_for_degrees(
    speed=-75,
    degrees=220,
    brake=True,
    block=True)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Blip 3.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

STING_MOTOR.on_for_seconds(
    speed=-100,
    seconds=1,
    brake=True,
    block=True)

STING_MOTOR.on_for_seconds(
    speed=100,   # 40 too weak
    seconds=1,
    brake=True,
    block=True)
