#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, OUTPUT_B, OUTPUT_D,
    Sound
)


STING_MOTOR = LargeMotor(address=OUTPUT_D)

GO_MOTOR = LargeMotor(address=OUTPUT_B)

SPEAKER = Sound()


STING_MOTOR.run_timed(
    speed_sp=400,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
STING_MOTOR.wait_while(Motor.STATE_RUNNING)

GO_MOTOR.run_to_rel_pos(
    speed_sp=1000,
    position_sp=3 * 360,
    stop_action=Motor.STOP_ACTION_HOLD)
GO_MOTOR.wait_while(Motor.STATE_RUNNING)

SPEAKER.play(wav_file='/home/robot/sound/Blip 2.wav').wait()

GO_MOTOR.run_to_rel_pos(
    speed_sp=1000,
    position_sp=-2 * 360,
    stop_action=Motor.STOP_ACTION_HOLD)
GO_MOTOR.wait_while(Motor.STATE_RUNNING)

SPEAKER.play(wav_file='/home/robot/sound/Blip 4.wav').wait()

STING_MOTOR.run_to_rel_pos(
    speed_sp=750,
    position_sp=-220,
    stop_action=Motor.STOP_ACTION_BRAKE)
STING_MOTOR.wait_while(Motor.STATE_RUNNING)

SPEAKER.play(wav_file='/home/robot/sound/Blip 3.wav').wait()

STING_MOTOR.run_timed(
    speed_sp=-1000,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
STING_MOTOR.wait_while(Motor.STATE_RUNNING)

STING_MOTOR.run_timed(
    speed_sp=1000,   # 400 too weak
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
STING_MOTOR.wait_while(Motor.STATE_RUNNING)
