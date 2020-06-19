#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_B, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound


MEDIUM_MOTOR = MediumMotor(OUTPUT_A)
STING_MOTOR = LargeMotor(OUTPUT_D)
GO_MOTOR = LargeMotor(OUTPUT_B)

INFRARED_SENSOR = InfraredSensor(INPUT_4)

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

STING_MOTOR.on_for_seconds(
    speed=40,
    seconds=1,
    brake=True,
    block=True)

for i in range(3):
    GO_MOTOR.on(
        speed=-100,
        brake=False,
        block=False)

    SPEAKER.play_file(
        wav_file='/home/robot/sound/Blip 2.wav',
        volume=100,
        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    while INFRARED_SENSOR.proximity >= 40:
        pass

    GO_MOTOR.on(
        speed=25,
        brake=False,
        block=False)

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

    SPEAKER.play_file(
        wav_file='/home/robot/sound/Blip 1.wav',
        volume=100,
        play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

    MEDIUM_MOTOR.on_for_seconds(
        speed=75,
        seconds=0.2,
        block=True,
        brake=True)

    MEDIUM_MOTOR.on_for_seconds(
        speed=-75,
        seconds=0.2,
        block=True,
        brake=True)

    GO_MOTOR.on_for_rotations(
        speed=-100,
        rotations=2,
        brake=True,
        block=True)

    STING_MOTOR.on_for_seconds(
        speed=100,
        seconds=1,
        block=True,
        brake=True)

    GO_MOTOR.on_for_rotations(
        speed=100,
        rotations=2,
        brake=True,
        block=True)
