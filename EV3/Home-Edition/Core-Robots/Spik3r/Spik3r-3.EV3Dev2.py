#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_B, OUTPUT_A
from ev3dev2.sound import Sound


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
LARGE_MOTOR = LargeMotor(address=OUTPUT_B)

SPEAKER = Sound()


MEDIUM_MOTOR.on_for_seconds(
    speed=50,
    seconds=1,
    block=True,
    brake=True)

MEDIUM_MOTOR.on_for_seconds(
    speed=-50,
    seconds=0.3,
    block=True,
    brake=True)


for i in range(2):
    for l in range(3):
        MEDIUM_MOTOR.on_for_seconds(
            speed=75,
            seconds=0.2,
            brake=True,
            block=True)

        MEDIUM_MOTOR.on_for_seconds(
            speed=-75,
            seconds=0.2,
            brake=True,
            block=True)

    LARGE_MOTOR.on_for_rotations(
        speed=100,
        rotations=3,
        brake=True,
        block=True)

    SPEAKER.play_file(
        wav_file='/home/robot/sound/Blip 2.wav',
        volume=100,
        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    LARGE_MOTOR.on_for_rotations(
        speed=-100,
        rotations=2,
        brake=True,
        block=True)

    SPEAKER.play_file(
        wav_file='/home/robot/sound/Blip 4.wav',
        volume=100,
        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    LARGE_MOTOR.on(
        speed=25,
        block=False,
        brake=False)

    SPEAKER.play_file(
        wav_file='/home/robot/sound/Blip 1.wav',
        volume=100,
        play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)
