#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.sound import Sound


CHEST_MOTOR = LargeMotor(OUTPUT_D)
TAIL_MOTOR = LargeMotor(OUTPUT_B)
MEDIUM_MOTOR = MediumMotor(OUTPUT_A)

TOUCH_SENSOR = TouchSensor(INPUT_1)
COLOR_SENSOR = ColorSensor(INPUT_2)
IR_SENSOR = InfraredSensor(INPUT_4)

SPEAKER = Sound()


while True:
    if COLOR_SENSOR.reflected_light_intensity > 30:
        TAIL_MOTOR.on_for_seconds(
            speed=50,
            seconds=4,
            brake=True,
            block=False)

        for i in range(2):
            MEDIUM_MOTOR.on_for_seconds(
                speed=10,
                seconds=1,
                brake=False,
                block=True)

            MEDIUM_MOTOR.on_for_seconds(
                speed=-10,
                seconds=1,
                brake=False,
                block=True)

    else:
        if TOUCH_SENSOR.is_pressed:
            CHEST_MOTOR.on_for_seconds(
                speed=100,
                seconds=1,
                brake=True,
                block=False)

            SPEAKER.play_file(
                wav_file='/home/robot/LEGO-Mindstorms/sounds/Snake hiss.wav',
                volume=100,
                play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

            CHEST_MOTOR.on_for_seconds(
                speed=-10,
                seconds=10,
                brake=True,
                block=True)
