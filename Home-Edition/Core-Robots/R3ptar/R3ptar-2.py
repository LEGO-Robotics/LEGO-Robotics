#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound

from time import sleep


LARGE_MOTOR = LargeMotor(OUTPUT_D)
MEDIUM_MOTOR = MediumMotor(OUTPUT_A)
IR_SENSOR = InfraredSensor(INPUT_4)
SPEAKER = Sound()


while True:
    if IR_SENSOR.proximity < 30:   # no InfraredSensor.wait_for_proximity(...) yet
        SPEAKER.play_file(
            wav_file='/home/robot/LEGO-Mindstorms/sounds/Snake hiss.wav',
            volume=100,
            play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

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

    # do 2nd process SEQUENTIALLY for now
    MEDIUM_MOTOR.on_for_seconds(
        speed=10,
        seconds=1,
        brake=False,
        block=True)

    SPEAKER.play_file(
        wav_file='/home/robot/LEGO-Mindstorms/sounds/Snake rattle.wav',
        volume=100,
        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    MEDIUM_MOTOR.on_for_seconds(
        speed=-10,
        seconds=1,
        brake=False,
        block=True)

    sleep(1)
