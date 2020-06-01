#!/usr/bin/env python3
# (MicroPython does not yet support Display as of May 2020)


from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.display import Display
from ev3dev2.sound import Sound


MEDIUM_MOTOR = MediumMotor(OUTPUT_A)
STEER_DRIVER = MoveSteering(left_motor_port=OUTPUT_B,
                            right_motor_port=OUTPUT_C,
                            motor_class=LargeMotor)

SCREEN = Display()
SPEAKER = Sound()


SCREEN.image_filename(
    filename='/home/robot/image/Pinch right.bmp',
    clear_screen=True)

STEER_DRIVER.on_for_degrees(
    steering=-100,
    speed=25,
    degrees=50,
    brake=True,
    block=True)

MEDIUM_MOTOR.on_for_rotations(
    speed=100,
    rotations=3,
    block=True,
    brake=True)

SCREEN.image_filename(
    filename='/home/robot/image/Pinch left.bmp',
    clear_screen=True)

STEER_DRIVER.on_for_degrees(
    steering=100,
    speed=25,
    degrees=100,
    brake=True,
    block=True)

MEDIUM_MOTOR.on_for_rotations(
    speed=100,
    rotations=6,
    block=True,
    brake=True)

SCREEN.image_filename(
    filename='/home/robot/image/Pinch middle.bmp',
    clear_screen=True)

STEER_DRIVER.on_for_degrees(
    steering=-100,
    speed=25,
    degrees=50,
    brake=True,
    block=True)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Laughing 1.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
