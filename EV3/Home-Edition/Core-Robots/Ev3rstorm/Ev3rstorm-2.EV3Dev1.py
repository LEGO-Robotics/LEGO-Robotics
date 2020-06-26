#!/usr/bin/env python3


from ev3dev.ev3 import (
    LargeMotor, OUTPUT_B, OUTPUT_C,
    TouchSensor, INPUT_1,
    Leds, Screen, Sound
)

from PIL import Image


LEFT_FOOT_MOTOR = LargeMotor(address=OUTPUT_B)
RIGHT_FOOT_MOTOR = LargeMotor(address=OUTPUT_C)

TOUCH_SENSOR = TouchSensor(address=INPUT_1)

LEDS = Leds()
SCREEN = Screen()
SPEAKER = Sound()


while True:
    SCREEN.image.paste(
        im=Image.open('/home/robot/image/ZZZ.bmp'),
        box=(0, 0))

    LEDS.set_color(
        group=Leds.LEFT,
        color=Leds.ORANGE,
        pct=1)
    LEDS.set_color(
        group=Leds.RIGHT,
        color=Leds.ORANGE,
        pct=1)

    while not TOUCH_SENSOR.is_pressed:
        SPEAKER.play(wav_file='/home/robot/sound/Snoring.wav').wait()

    SCREEN.image.paste(
        im=Image.open('/home/robot/image/Winking.bmp'),
        box=(0, 0))
        
    SPEAKER.play(wav_file='/home/robot/sound/Activate.wav').wait()
    SPEAKER.play(wav_file='/home/robot/sound/EV3.wav').wait()

    SCREEN.image.paste(
        im=Image.open('/home/robot/image/Neutral.bmp'),
        box=(0, 0))

    LEDS.set_color(
        group=Leds.LEFT,
        color=Leds.GREEN,
        pct=1)
    LEDS.set_color(
        group=Leds.RIGHT,
        color=Leds.GREEN,
        pct=1)

    LEFT_FOOT_MOTOR.run_to_rel_pos(
        position_sp=360,   # degrees
        speed_sp=750,
        stop_action=LargeMotor.STOP_ACTION_BRAKE)
    LEFT_FOOT_MOTOR.wait_while('running')
    RIGHT_FOOT_MOTOR.run_to_rel_pos(
        position_sp=1 * 360,   # degrees
        speed_sp=750,
        stop_action=LargeMotor.STOP_ACTION_BRAKE)
    RIGHT_FOOT_MOTOR.wait_while('running')

    while not TOUCH_SENSOR.is_pressed:
        pass

    SCREEN.image.paste(
        im=Image.open('/home/robot/image/Tired middle.bmp'),
        box=(0, 0))

    SPEAKER.play(wav_file='/home/robot/sound/Goodbye.wav').wait()
