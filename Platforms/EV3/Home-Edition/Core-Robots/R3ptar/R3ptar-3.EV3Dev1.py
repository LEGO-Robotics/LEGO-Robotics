#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D, 
    InfraredSensor, INPUT_4, 
    Leds, Sound
)

from random import randint
from time import sleep


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
TAIL_MOTOR = LargeMotor(address=OUTPUT_B)
CHEST_MOTOR = LargeMotor(address=OUTPUT_D)

IR_SENSOR = InfraredSensor(address=INPUT_4)

LIGHTS = Leds()
SPEAKER = Sound()


CHEST_MOTOR.run_timed(
    speed_sp=-300,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
CHEST_MOTOR.wait_while(Motor.STATE_RUNNING) 

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

        MEDIUM_MOTOR.stop(stop_action=Motor.STOP_ACTION_HOLD)

        TAIL_MOTOR.stop(stop_action=Motor.STOP_ACTION_BRAKE)

        SPEAKER.play(wav_file='/home/robot/sound/Snake hiss.wav')

        CHEST_MOTOR.run_timed(
            speed_sp=1000,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_BRAKE)
        CHEST_MOTOR.wait_while(Motor.STATE_RUNNING)

        MEDIUM_MOTOR.run_forever(speed_sp=1000)

        TAIL_MOTOR.run_forever(speed_sp=-1000)

        CHEST_MOTOR.run_timed(
            speed_sp=-300,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_BRAKE)
        CHEST_MOTOR.wait_while(Motor.STATE_RUNNING)

        sleep(2)

        MEDIUM_MOTOR.run_timed(
            speed_sp=-1000,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_HOLD)
        MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

        sleep(1)

    else:
        LIGHTS.set_color(
            group=Leds.LEFT,
            color=Leds.ORANGE,
            pct=1)

        LIGHTS.set_color(
            group=Leds.RIGHT,
            color=Leds.ORANGE,
            pct=1)

        TAIL_MOTOR.run_forever(speed_sp=1000)

        MEDIUM_MOTOR.run_timed(
            speed_sp=randint(-30, 30),
            time_sp=0.2 * 1000,
            stop_action=Motor.STOP_ACTION_COAST)
        MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)
