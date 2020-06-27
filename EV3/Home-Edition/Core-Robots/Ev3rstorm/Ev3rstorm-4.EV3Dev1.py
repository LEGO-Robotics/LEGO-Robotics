#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    InfraredSensor, INPUT_4,
    Leds, Sound
)

from time import time


LEFT_FOOT_MOTOR = LargeMotor(address=OUTPUT_B)
RIGHT_FOOT_MOTOR = LargeMotor(address=OUTPUT_C)
MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)

IR_SENSOR = InfraredSensor(address=INPUT_4)

LEDS = Leds()
SPEAKER = Sound()


while True:
    if IR_SENSOR.proximity < 25:
        LEFT_FOOT_MOTOR.stop(stop_action=Motor.STOP_ACTION_BRAKE)
        RIGHT_FOOT_MOTOR.stop(stop_action=Motor.STOP_ACTION_BRAKE)

        LEDS.set_color(
            group=Leds.LEFT,
            color=Leds.RED,
            pct=1)
        LEDS.set_color(
            group=Leds.RIGHT,
            color=Leds.RED,
            pct=1)

        SPEAKER.play(wav_file='/home/robot/sound/Object.wav').wait()
        SPEAKER.play(wav_file='/home/robot/sound/Detected.wav').wait()
        SPEAKER.play(wav_file='/home/robot/sound/Error alarm.wav').wait()

        MEDIUM_MOTOR.run_forever(speed_sp=1000)

        LEFT_FOOT_MOTOR.run_to_rel_pos(
            position_sp=360,
            speed_sp=1000,
            stop_action=Motor.STOP_ACTION_BRAKE)
        RIGHT_FOOT_MOTOR.run_to_rel_pos(
            position_sp=360,
            speed_sp=800,
            stop_action=Motor.STOP_ACTION_BRAKE)
        LEFT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)
        RIGHT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)

        MEDIUM_MOTOR.run_forever(speed_sp=-1000)

        LEFT_FOOT_MOTOR.run_to_rel_pos(
            position_sp=-360,
            speed_sp=1000,
            stop_action=Motor.STOP_ACTION_BRAKE)
        RIGHT_FOOT_MOTOR.run_to_rel_pos(
            position_sp=-360,
            speed_sp=800,
            stop_action=Motor.STOP_ACTION_BRAKE)
        LEFT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)
        RIGHT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)

        MEDIUM_MOTOR.stop(stop_action=Motor.STOP_ACTION_HOLD)

        LEFT_FOOT_MOTOR.run_to_rel_pos(
            position_sp=720,
            speed_sp=1000,
            stop_action=Motor.STOP_ACTION_BRAKE)
        RIGHT_FOOT_MOTOR.run_to_rel_pos(
            position_sp=-720,
            speed_sp=1000,
            stop_action=Motor.STOP_ACTION_BRAKE)
        LEFT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)
        RIGHT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)

        RIGHT_FOOT_MOTOR.run_to_rel_pos(
            position_sp=360,
            speed_sp=1000,
            stop_action=Motor.STOP_ACTION_BRAKE)
        RIGHT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)

    else:
        LEDS.set_color(
            group=Leds.LEFT,
            color=Leds.GREEN,
            pct=1)
        LEDS.set_color(
            group=Leds.RIGHT,
            color=Leds.GREEN,
            pct=1)

        if time() % 3 < 1.5:
            LEFT_FOOT_MOTOR.run_forever(speed_sp=500)
            RIGHT_FOOT_MOTOR.run_forever(speed_sp=1000)

        else:
            LEFT_FOOT_MOTOR.run_forever(speed_sp=1000)
            RIGHT_FOOT_MOTOR.run_forever(speed_sp=500)
