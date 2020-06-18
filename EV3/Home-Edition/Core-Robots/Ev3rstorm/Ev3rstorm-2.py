#!/usr/bin/env python3
# (Display not yet working in MicroPython as of June 2020)


from ev3dev2.motor import LargeMotor, MoveSteering, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.sound import Sound
from ev3dev2.led import Leds
from ev3dev2.display import Display


STEER_DRIVER = MoveSteering(left_motor_port=OUTPUT_B,
                            right_motor_port=OUTPUT_C,
                            motor_class=LargeMotor)

TOUCH_SENSOR = TouchSensor(INPUT_1)

SPEAKER = Sound()
SCREEN = Display()
LEDS = Leds()


while True:
    SCREEN.image_filename(
        filename='/home/robot/image/ZZZ.bmp',
        clear_screen=True)

    LEDS.set_color(
        group='LEFT',
        color='ORANGE',
        pct=1)

    LEDS.set_color(
        group='RIGHT',
        color='ORANGE',
        pct=1)

    while not TOUCH_SENSOR.is_pressed:
        SPEAKER.play_file(
            wav_file='/home/robot/sound/Snoring.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    SCREEN.image_filename(
        filename='/home/robot/image/Winking.bmp',
        clear_screen=True)
        
    SPEAKER.play_file(
        wav_file='/home/robot/sound/Activate.wav',
        volume=100,
        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    SPEAKER.play_file(
        wav_file='/home/robot/sound/EV3.wav',
        volume=100,
        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    SCREEN.image_filename(
        filename='/home/robot/image/Neutral.bmp',
        clear_screen=True)

    LEDS.animate_police_lights(
        color1='GREEN',
        color2='RED',
        group1='LEFT',
        group2='RIGHT',
        sleeptime=0.5,
        duration=5,
        block=True)

    STEER_DRIVER.on_for_rotations(
        steering=100,
        speed=75,
        rotations=1,
        brake=True,
        block=True)

    STEER_DRIVER.on_for_rotations(
        steering=-100,
        speed=75,
        rotations=1,
        brake=True,
        block=True)

    TOUCH_SENSOR.wait_for_pressed()

    SCREEN.image_filename(
        filename='/home/robot/image/Tired middle.bmp',
        clear_screen=True)

    SPEAKER.play_file(
        wav_file='/home/robot/sound/Goodbye.wav',
        volume=100,
        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
    