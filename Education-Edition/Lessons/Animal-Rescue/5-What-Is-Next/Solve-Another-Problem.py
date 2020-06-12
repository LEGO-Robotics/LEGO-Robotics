#!/usr/bin/env micropython


# program your Turtle to perform different actions based on the color it detects


from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.sound import Sound


LEG_MOTOR_RIGHT = LargeMotor(OUTPUT_C)
LEG_MOTOR_LEFT = LargeMotor(OUTPUT_B)
MEDIUM_MOTOR = MediumMotor(OUTPUT_A)

TOUCH_SENSOR = TouchSensor(INPUT_1)
COLOR_SENSOR = ColorSensor(INPUT_2)
IR_SENSOR = InfraredSensor(INPUT_4)

SPEAKER = Sound()


while True: 
    if COLOR_SENSOR.color == ColorSensor.COLOR_RED:
        MEDIUM_MOTOR.on_for_rotations(
            speed=100,
            rotations=3,
            block=True,
            brake=True)

    elif COLOR_SENSOR.color == ColorSensor.COLOR_BLACK:
        LEG_MOTOR_RIGHT.on_for_rotations(
            speed=100,
            rotations=3,
            block=True,
            brake=True)

        SPEAKER.play_file(
            wav_file='/home/robot/sound/Error alarm.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    elif COLOR_SENSOR.color == ColorSensor.COLOR_BROWN:
        if IR_SENSOR.proximity <= 10:
            LEG_MOTOR_LEFT.on_for_seconds(
                speed=-91,
                seconds=1,
                brake=True,
                block=True)
