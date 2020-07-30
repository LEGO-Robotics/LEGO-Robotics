#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_B, OUTPUT_D, OUTPUT_A,
    Sound
)


STING_MOTOR = LargeMotor(address=OUTPUT_D)

GO_MOTOR = LargeMotor(address=OUTPUT_B)

SPEAKER = Sound()

MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)


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

for i in range(2):
    for i in range(3):
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

    GO_MOTOR.run_forever(speed_sp=250)
    
    SPEAKER.play(wav_file='/home/robot/sound/Blip 1.wav').wait()
