#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
     Sound
)

from time import sleep


LEFT_MOTOR = LargeMotor(address=OUTPUT_B)
RIGHT_MOTOR = LargeMotor(address=OUTPUT_C)
MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)

SPEAKER = Sound()


MEDIUM_MOTOR.run_forever(speed_sp=-1000)
MEDIUM_MOTOR.stop(stop_action=Motor.STOP_ACTION_HOLD)

for i in range(2):
    LEFT_MOTOR.run_to_rel_pos(
        position_sp=2 * 360,   # degrees
        speed_sp=750,   # degrees per second
        stop_action=Motor.STOP_ACTION_BRAKE)
    RIGHT_MOTOR.run_to_rel_pos(
        position_sp=2 * 360,   # degrees
        speed_sp=750,   # degrees per second
        stop_action=Motor.STOP_ACTION_BRAKE)
    LEFT_MOTOR.wait_while(Motor.STATE_RUNNING)
    RIGHT_MOTOR.wait_while(Motor.STATE_RUNNING)

    MEDIUM_MOTOR.run_forever(speed_sp=1000)

    SPEAKER.play(wav_file='/home/robot/sound/Airbrake.wav').wait()

    sleep(0.5)

    LEFT_MOTOR.run_to_rel_pos(
        position_sp=3 * 360,   # degrees
        speed_sp=750,   # degrees per second
        stop_action=Motor.STOP_ACTION_BRAKE)
    LEFT_MOTOR.wait_while(Motor.STATE_RUNNING)
    
    MEDIUM_MOTOR.run_forever(speed_sp=-1000)

    SPEAKER.play(wav_file='/home/robot/sound/Air release.wav').wait()
   

    sleep(0.5)

    LEFT_MOTOR.run_to_rel_pos(
        position_sp=-3 * 360,   # degrees
        speed_sp=750,   # degrees per second
        stop_action=Motor.STOP_ACTION_BRAKE)
    LEFT_MOTOR.wait_while(Motor.STATE_RUNNING)

LEFT_MOTOR.run_to_rel_pos(
    position_sp=-4 * 360,   # degrees
    speed_sp=750,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
RIGHT_MOTOR.run_to_rel_pos(
    position_sp=-4 * 360,   # degrees
    speed_sp=750,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
LEFT_MOTOR.wait_while(Motor.STATE_RUNNING)
RIGHT_MOTOR.wait_while(Motor.STATE_RUNNING)

SPEAKER.play(wav_file='/home/robot/sound/Cheering.wav').wait()
