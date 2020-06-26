#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

from random import randint
from time import sleep


MEDIUM_MOTOR = MediumMotor(OUTPUT_A)
CHEST_MOTOR = LargeMotor(OUTPUT_D)
TAIL_MOTOR = LargeMotor(OUTPUT_B)

IR_SENSOR = InfraredSensor(INPUT_4)

LIGHTS = Leds()
SPEAKER = Sound()


CHEST_MOTOR.on_for_seconds(
    speed=-30,
    seconds=1,
    brake=True,
    block=True)

while True:
    if IR_SENSOR.proximity < 30:
        LIGHTS.set_color(
            group=Leds.LEFT,
            color=Leds.RED,
            pct=1)

        LIGHTS.set_color(
            group=Leds.RIGHT,
            color=Leds.RED,
            pct=1)

        MEDIUM_MOTOR.off(brake=True)

        TAIL_MOTOR.off(brake=True)

        SPEAKER.play_file(
            wav_file='/home/robot/sound/Snake hiss.wav',
            volume=100,
            play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

        CHEST_MOTOR.on_for_seconds(
            speed=100,
            seconds=1,
            brake=True,
            block=True)

        MEDIUM_MOTOR.on(
            speed=100,
            brake=False,
            block=False)

        TAIL_MOTOR.on(
            speed=-100,
            brake=False,
            block=False)

        CHEST_MOTOR.on_for_seconds(
            speed=-30,
            seconds=1,
            brake=True,
            block=True)

        sleep(2)

        MEDIUM_MOTOR.on_for_seconds(
            speed=-100,
            seconds=1,
            brake=True,
            block=True)

        sleep(1)

    else:
        LIGHTS.animate_flash(
            color=Leds.ORANGE,
            groups=(Leds.LEFT, Leds.RIGHT),
            block=False)

        TAIL_MOTOR.on(
            speed=100,
            brake=False,
            block=False)

        MEDIUM_MOTOR.on_for_seconds(
            speed=randint(-30,30),
            seconds=0.2,
            brake=False,
            block=True)
