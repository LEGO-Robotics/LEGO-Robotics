#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, LargeMotor, OUTPUT_B, OUTPUT_A, OUTPUT_D,
    INPUT_4, InfraredSensor, BeaconSeeker,
    Sound
)

from time import sleep


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
GO_MOTOR = LargeMotor(address=OUTPUT_B)
STING_MOTOR = LargeMotor(address=OUTPUT_D)

INFRARED_SENSOR = InfraredSensor(address=INPUT_4)
BEACON_SEEKER = BeaconSeeker(sensor=INFRARED_SENSOR,
                             channel=1)

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

GO_MOTOR.run_forever(speed_sp=-500)

SPEAKER.play(wav_file='/home/robot/sound/Blip 2.wav').wait()

assert BEACON_SEEKER.distance > -128

while BEACON_SEEKER.distance >= 30:
    pass

while BEACON_SEEKER.heading <= 5:
    pass

GO_MOTOR.run_forever(speed_sp=-200)

while BEACON_SEEKER.heading >= 3:
    pass

# FIXME: Spik3r doesn't stop at the correct angle
GO_MOTOR.stop(stop_action=Motor.STOP_ACTION_HOLD)

SPEAKER.play(wav_file='/home/robot/sound/Blip 4.wav').wait()

# FIXME: the following doesn't run
for i in range(3):
    GO_MOTOR.run_to_rel_pos(
        speed_sp=1000,
        position=-10,
        stop_action=Motor.STOP_ACTION_HOLD)
    GO_MOTOR.wait_while(Motor.STATE_RUNNING)

    STING_MOTOR.run_to_rel_pos(
        speed_sp=750,
        position=-220,
        stop_action=Motor.STOP_ACTION_HOLD)
    STING_MOTOR.wait_while(Motor.STATE_RUNNING)

    sleep(0.1)

    STING_MOTOR.run_timed(
        speed_sp=-1000,
        time_sp=1000,
        stop_action=Motor.STOP_ACTION_HOLD)
    STING_MOTOR.wait_while(Motor.STATE_RUNNING)

    STING_MOTOR.run_timed(
        speed_sp=400,
        time_sp=1000,
        stop_action=Motor.STOP_ACTION_HOLD)
    STING_MOTOR.wait_while(Motor.STATE_RUNNING)

    # to avoid jerking
    sleep(1)

GO_MOTOR.run_forever(speed_sp=1000)

SPEAKER.play(wav_file='/home/robot/sound/Blip 1.wav').wait()

for i in range(5):
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

SPEAKER.play(wav_file='/home/robot/sound/Blip 3.wav').wait()

GO_MOTOR.run_to_rel_pos(
    speed_sp=1000,
    positon=-2 * 360,
    brake=True,
    block=True)

GO_MOTOR.run_to_rel_pos(
    speed_sp=1000,
    positon=2 * 360,
    brake=True,
    block=True)
