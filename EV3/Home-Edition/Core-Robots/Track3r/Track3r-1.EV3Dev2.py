#!/usr/bin/env python3
# (MicroPython does not yet support Display as of 2020)


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_B, OUTPUT_C, OUTPUT_A
from ev3dev2.display import Display
from ev3dev2.sound import Sound
  

MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)

SCREEN = Display()
SPEAKER = Sound()


SCREEN.image_filename(
    filename='/home/robot/image/Pinch left.bmp',
    clear_screen=True)
SCREEN.update()

TANK_DRIVER.on_for_rotations(
    left_speed=75,
    right_speed=75,
    rotations=2,
    brake=True,
    block=True)

MEDIUM_MOTOR.on_for_rotations(
    speed=75,
    rotations=3,
    brake=True,
    block=True)

TANK_DRIVER.on_for_rotations(
    left_speed=-75,
    right_speed=-75,
    rotations=2,
    brake=True,
    block=True)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Fanfare.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
