#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sound import Sound


MEDIUM_MOTOR = MediumMotor(OUTPUT_A)
TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)
STEER_DRIVER = MoveSteering(left_motor_port=OUTPUT_B,
                            right_motor_port=OUTPUT_C,
                            motor_class=LargeMotor)

SPEAKER = Sound()


MEDIUM_MOTOR.on_for_seconds(
    speed=-50,
    seconds=1,
    brake=True,
    block=True)

TANK_DRIVER.on_for_rotations(
    left_speed=75,
    right_speed=75,
    rotations=3,
    brake=True,
    block=True)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Airbrake.wav',
    volume=100,
    play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

MEDIUM_MOTOR.on_for_seconds(
    speed=50,
    seconds=1,
    brake=True,
    block=True)
 
STEER_DRIVER.on_for_degrees(
    steering=100,
    speed=75,
    degrees=850,
    brake=True,
    block=True)

TANK_DRIVER.on_for_rotations(
    left_speed=75,
    right_speed=75,
    rotations=3,
    brake=True,
    block=True)

MEDIUM_MOTOR.on(
    speed=-50,
    brake=False,
    block=False)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Air release.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
