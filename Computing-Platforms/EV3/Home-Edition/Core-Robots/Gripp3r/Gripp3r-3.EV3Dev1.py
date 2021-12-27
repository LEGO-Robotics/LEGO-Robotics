#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    InfraredSensor, INPUT_4,
    Sound
)


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
LEFT_MOTOR = Motor(address=OUTPUT_B)
RIGHT_MOTOR = Motor(address=OUTPUT_C)

IR_SENSOR = InfraredSensor(address=INPUT_4)

SPEAKER = Sound()


MEDIUM_MOTOR.run_timed(
    speed_sp=-500,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

while IR_SENSOR.proximity >= 25:
    LEFT_MOTOR.run_forever(speed_sp=750)
    RIGHT_MOTOR.run_forever(speed_sp=750)

LEFT_MOTOR.stop(stop_action=Motor.STOP_ACTION_BRAKE)
RIGHT_MOTOR.stop(stop_action=Motor.STOP_ACTION_BRAKE)

SPEAKER.play(wav_file='/home/robot/sound/Airbrake.wav')

MEDIUM_MOTOR.run_timed(
    speed_sp=500,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_BRAKE)
MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)
 
LEFT_MOTOR.run_to_rel_pos(
    position_sp=1000,   
    speed_sp=750,   
    stop_action=Motor.STOP_ACTION_BRAKE)
RIGHT_MOTOR.run_to_rel_pos(
    position_sp=-1000,   
    speed_sp=750,   
    stop_action=Motor.STOP_ACTION_BRAKE)
LEFT_MOTOR.wait_while(Motor.STATE_RUNNING)
RIGHT_MOTOR.wait_while(Motor.STATE_RUNNING)

while IR_SENSOR.proximity >= 25:
    LEFT_MOTOR.run_forever(speed_sp=750)
    RIGHT_MOTOR.run_forever(speed_sp=750)

LEFT_MOTOR.stop(stop_action=Motor.STOP_ACTION_BRAKE)
RIGHT_MOTOR.stop(stop_action=Motor.STOP_ACTION_BRAKE)

MEDIUM_MOTOR.run_forever(speed_sp=-500)

SPEAKER.play(wav_file='/home/robot/sound/Air release.wav').wait()
