#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D,
    InfraredSensor, INPUT_4,
    Sound
)   


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
GO_MOTOR = LargeMotor(address=OUTPUT_B)
STING_MOTOR = LargeMotor(address=OUTPUT_D)

INFRARED_SENSOR = InfraredSensor(address=INPUT_4)

SPEAKER = Sound()


MEDIUM_MOTOR.run_timed(
    speed_sp=500,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_HOLD)
MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

MEDIUM_MOTOR.run_timed(
    speed_sp=-500,
    time_sp=0.3 * 1000,
    stop_action=Motor.STOP_ACTION_HOLD)
MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

STING_MOTOR.run_timed(
    speed_sp=400,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_HOLD)
STING_MOTOR.wait_while(Motor.STATE_RUNNING)

for i in range(3):
    GO_MOTOR.run_forever(speed_sp=-1000)

    SPEAKER.play(wav_file='/home/robot/sound/Blip 2.wav').wait()

    while INFRARED_SENSOR.proximity >= 40:
        pass

    GO_MOTOR.run_forever(speed_sp=250)

    SPEAKER.play(wav_file='/home/robot/sound/Blip 4.wav').wait()

    STING_MOTOR.run_to_rel_pos(
        speed_sp=750,
        position_sp=-220,
        stop_action=Motor.STOP_ACTION_HOLD)
    STING_MOTOR.wait_while(Motor.STATE_RUNNING)

    SPEAKER.play(wav_file='/home/robot/sound/Blip 3.wav').wait()
    
    STING_MOTOR.run_timed(
        speed_sp=-1000,
        time_sp=1000,
        stop_action=Motor.STOP_ACTION_HOLD)
    STING_MOTOR.wait_while(Motor.STATE_RUNNING)

    SPEAKER.play(wav_file='/home/robot/sound/Blip 1.wav').wait()

    MEDIUM_MOTOR.run_timed(
        speed_sp=750,
        time_sp=0.2 * 1000,
        stop_action=Motor.STOP_ACTION_HOLD)
    MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

    MEDIUM_MOTOR.run_timed(
        speed_sp=-750,
        time_sp=0.2 * 1000,
        stop_action=Motor.STOP_ACTION_HOLD)
    MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

    GO_MOTOR.run_to_rel_pos(
        speed_sp=1000,
        position_sp=-2 * 360,
        stop_action=Motor.STOP_ACTION_HOLD)
    GO_MOTOR.wait_while(Motor.STATE_RUNNING)

    STING_MOTOR.run_timed(
        speed_sp=400,
        time_sp=1000,
        stop_action=Motor.STOP_ACTION_HOLD)
    STING_MOTOR.wait_while(Motor.STATE_RUNNING)

    GO_MOTOR.run_to_rel_pos(
        speed_sp=1000,
        position_sp=2 * 360,
        stop_action=Motor.STOP_ACTION_HOLD)
    GO_MOTOR.wait_while(Motor.STATE_RUNNING)
