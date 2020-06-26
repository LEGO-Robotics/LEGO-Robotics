#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_B, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound

from time import sleep


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
GO_MOTOR = LargeMotor(address=OUTPUT_B)
STING_MOTOR = LargeMotor(address=OUTPUT_D)

INFRARED_SENSOR = InfraredSensor(address=INPUT_4)

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

GO_MOTOR.on(
    speed=-50,
    block=False,
    brake=False)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Blip 2.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

while INFRARED_SENSOR.proximity >= 30:
    pass

while INFRARED_SENSOR.heading(channel=1) <= 5:
    pass

GO_MOTOR.on(
    speed=-20,
    brake=False,
    block=False)

while INFRARED_SENSOR.heading(channel=1) >= 3:
    pass

GO_MOTOR.off(brake=True)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Blip 4.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

for i in range(3):
    GO_MOTOR.on_for_degrees(
        speed=-100,
        degrees=10,
        block=True,
        brake=True)

    STING_MOTOR.on_for_degrees(
        speed=-75,
        degrees=220,
        brake=True,
        block=True)

    sleep(0.1)

    STING_MOTOR.on_for_seconds(
        speed=-100,
        seconds=1,
        brake=True,
        block=True)

    STING_MOTOR.on_for_seconds(
        speed=100,   # 40 too weak?
        seconds=1,
        block=True,
        brake=True)

    # to avoid jerking
    sleep(1)

GO_MOTOR.on(
    speed=100,
    brake=False,
    block=False)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Blip 1.wav',
    volume=100,
    play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

for i in range(5):
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

SPEAKER.play_file(
    wav_file='/home/robot/sound/Blip 3.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

GO_MOTOR.on_for_rotations(
    speed=-100,
    rotations=2,
    brake=True,
    block=True)

GO_MOTOR.on_for_rotations(
    speed=100,
    rotations=2,
    brake=True,
    block=True)
