#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, OUTPUT_D,
    Sound
)


LARGE_MOTOR = LargeMotor(address=OUTPUT_D)

SPEAKER = Sound()


LARGE_MOTOR.run_timed(
    speed_sp=400,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
LARGE_MOTOR.wait_while(Motor.STATE_RUNNING)

LARGE_MOTOR.run_to_rel_pos(
    speed_sp=750,
    position_sp=-220,
    stop_action=Motor.STOP_ACTION_BRAKE)
LARGE_MOTOR.wait_while(Motor.STATE_RUNNING)

SPEAKER.play(wav_file='/home/robot/sound/Blip 3.wav').wait()

LARGE_MOTOR.run_timed(
    speed_sp=-1000,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
LARGE_MOTOR.wait_while(Motor.STATE_RUNNING)

LARGE_MOTOR.run_timed(
    speed_sp=1000,   # 400 too weak
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
LARGE_MOTOR.wait_while(Motor.STATE_RUNNING)
