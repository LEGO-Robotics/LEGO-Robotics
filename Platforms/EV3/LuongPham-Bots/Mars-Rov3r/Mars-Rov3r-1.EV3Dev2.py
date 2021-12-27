#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)

IR_SENSOR = InfraredSensor(address=INPUT_4)

SPEAKER = Sound()


is_gripping = False

MEDIUM_MOTOR.on_for_seconds(
    speed=50,
    seconds=1,
    brake=True,
    block=True)


while True:
    if IR_SENSOR.beacon(channel=1):
        if is_gripping:
            MEDIUM_MOTOR.on_for_seconds(
                speed=100,
                seconds=2,
                brake=True,
                block=True)

            SPEAKER.play_file(
                wav_file='/home/robot/sound/Air release.wav',
                volume=100,
                play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

            is_gripping = False

        else:
            MEDIUM_MOTOR.on_for_seconds(
                speed=-100,
                seconds=2,
                brake=True,
                block=True)

            SPEAKER.play_file(
                wav_file='/home/robot/sound/Airbrake.wav',
                volume=100,
                play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

            is_gripping = True

        while IR_SENSOR.beacon(channel=1):
            pass
