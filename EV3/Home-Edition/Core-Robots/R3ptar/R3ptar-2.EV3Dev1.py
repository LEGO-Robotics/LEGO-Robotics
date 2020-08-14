#!/usr/bin/env python3


from ev3dev.ev3 import(
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_D,
    INPUT_4, InfraredSensor,
    Sound
) 
   

from time import sleep


LARGE_MOTOR = LargeMotor(address=OUTPUT_D)
MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)

IR_SENSOR = InfraredSensor(address=INPUT_4)

SPEAKER = Sound()


def rattle():
    MEDIUM_MOTOR.run_timed(
        speed_sp=100,
        time_sp=1000,
        stop_action=Motor.STOP_ACTION_COAST)
    MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

    SPEAKER.play(wav_file='/home/robot/sound/Snake rattle.wav').wait()

    MEDIUM_MOTOR.run_timed(
        speed_sp=-100,
        time_sp=1000,
        stop_action=Motor.STOP_ACTION_COAST)
    MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

    sleep(1)


def scare_people():
    if IR_SENSOR.proximity < 30:
        SPEAKER.play(wav_file='/home/robot/sound/Snake hiss.wav').wait()

        LARGE_MOTOR.run_timed(
            speed_sp=1000,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_COAST)
        LARGE_MOTOR.wait_while(Motor.STATE_RUNNING)

    else:
        LARGE_MOTOR.run_timed(
            speed_sp=-300,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_COAST)
        LARGE_MOTOR.wait_while(Motor.STATE_RUNNING)


while True:
    scare_people()

    rattle()
