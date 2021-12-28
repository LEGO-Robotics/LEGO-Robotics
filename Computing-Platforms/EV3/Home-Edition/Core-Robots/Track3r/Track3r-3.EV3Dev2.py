#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sound import Sound

from time import sleep


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)
STEER_DRIVER = MoveSteering(left_motor_port=OUTPUT_B,
                            right_motor_port=OUTPUT_C,
                            motor_class=LargeMotor)

SPEAKER = Sound()


MEDIUM_MOTOR.on(
    speed=-100,
    brake=False,
    block=False)

for i in range(2):
    TANK_DRIVER.on_for_rotations(
        left_speed=75,
        right_speed=75,
        rotations=2,
        brake=True,
        block=True)

    MEDIUM_MOTOR.on(
        speed=100,
        brake=False,
        block=False)

    SPEAKER.play_file(
        wav_file='/home/robot/sound/Airbrake.wav',
        volume=100,
        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    sleep(0.5)

    STEER_DRIVER.on_for_rotations(
        steering=35,
        speed=75,
        rotations=3,
        brake=True,
        block=True)

    MEDIUM_MOTOR.on(
        speed=-100,
        block=False,
        brake=False)

    SPEAKER.play_file(
        wav_file='/home/robot/sound/Air release.wav',
        volume=100,
        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    sleep(0.5)

    STEER_DRIVER.on_for_rotations(
        steering=35,
        speed=75,
        rotations=-3,
        brake=True,
        block=True)

TANK_DRIVER.on_for_rotations(
    left_speed=-75,
    right_speed=-75,
    rotations=4,
    brake=True,
    block=True)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Cheering.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
