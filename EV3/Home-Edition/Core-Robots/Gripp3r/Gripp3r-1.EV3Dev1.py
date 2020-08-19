#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A,
    Sound
)

from time import sleep


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
SPEAKER = Sound()


MEDIUM_MOTOR.run_timed(
    speed_sp=-500,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)


SPEAKER.play(wav_file='/home/robot/sound/Airbrake.wav')

MEDIUM_MOTOR.run_timed(
    speed_sp=500,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

sleep(1)

SPEAKER.play(wav_file='/home/robot/sound/Air release.wav')

MEDIUM_MOTOR.run_timed(
    speed_sp=-500,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)
