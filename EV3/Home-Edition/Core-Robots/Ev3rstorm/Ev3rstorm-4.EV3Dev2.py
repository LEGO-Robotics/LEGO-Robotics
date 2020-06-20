#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, InfraredSensor
from ev3dev2.sound import Sound
from ev3dev2.led import Leds

from time import time


TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)

MEDIUM_MOTOR = MediumMotor(OUTPUT_A)

COLOR_SENSOR = ColorSensor(INPUT_2)
TOUCH_SENSOR = TouchSensor(INPUT_1)
IR_SENSOR = InfraredSensor(INPUT_4)

SPEAKER = Sound()
LEDS = Leds()


while True:
    if IR_SENSOR.proximity < 25: 
        TANK_DRIVER.off(brake=True)

        LEDS.animate_police_lights(
            color1='ORANGE',
            color2='RED',
            group1='LEFT',
            group2='RIGHT',
            sleeptime=0.5,
            duration=5,
            block=True)
        
        SPEAKER.play_file(
            wav_file='/home/robot/sound/Object.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        SPEAKER.play_file(                                  
            wav_file='/home/robot/sound/Detected.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        SPEAKER.play_file(
            wav_file='/home/robot/sound/Error alarm.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        MEDIUM_MOTOR.on(
            speed=100,
            block=False,
            brake=False)

        TANK_DRIVER.on_for_rotations(
            left_speed=100,
            right_speed=80,
            rotations=1,
            brake=True,
            block=True)

        MEDIUM_MOTOR.on(
            speed=-100,
            block=False,
            brake=False)

        TANK_DRIVER.on_for_rotations(
            left_speed=-100,
            right_speed=-80,
            rotations=1,
            brake=True,
            block=True)

        MEDIUM_MOTOR.off(brake=True)

        TANK_DRIVER.on_for_rotations(
            left_speed=100,
            right_speed=-100,
            rotations=2,
            brake=True,
            block=True)

        TANK_DRIVER.on_for_rotations(
            left_speed=0,
            right_speed=100,
            rotations=1,
            brake=True,
            block=True)

    else:
        LEDS.animate_police_lights(
            color1='YELLOW',
            color2='GREEN',
            group1='LEFT',
            group2='RIGHT',
            sleeptime=0.5,
            duration=5,
            block=True)
           
        if time() % 3 < 1.5:
            TANK_DRIVER.on(
                left_speed=50,
                right_speed=100)

        else:
            TANK_DRIVER.on(
                left_speed=100,
                right_speed=50)
