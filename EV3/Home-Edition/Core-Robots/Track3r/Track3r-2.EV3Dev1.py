#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    Screen, Sound
)

from PIL import Image
  

MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
LEFT_MOTOR = LargeMotor(address=OUTPUT_B)
RIGHT_MOTOR = LargeMotor(address=OUTPUT_C)

SCREEN = Screen()
SPEAKER = Sound()


SCREEN.image.paste(im=Image.open('/home/robot/image/Pinch right.bmp'))
SCREEN.update()

LEFT_MOTOR.run_to_rel_pos(
    position_sp=-0.5 * 360,   # degrees
    speed_sp=250,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
RIGHT_MOTOR.run_to_rel_pos(
    position_sp=0.5 * 360,   # degrees
    speed_sp=250,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
LEFT_MOTOR.wait_while(Motor.STATE_RUNNING)
RIGHT_MOTOR.wait_while(Motor.STATE_RUNNING)

MEDIUM_MOTOR.run_to_rel_pos(
    position_sp=3 * 360,   # degrees
    speed_sp=1000,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

SCREEN.image.paste(im=Image.open('/home/robot/image/Pinch left.bmp'))
SCREEN.update()


LEFT_MOTOR.run_to_rel_pos(
    position_sp=1 * 360,   # degrees
    speed_sp=250,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
RIGHT_MOTOR.run_to_rel_pos(
    position_sp=-1 * 360,   # degrees
    speed_sp=250,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
LEFT_MOTOR.wait_while(Motor.STATE_RUNNING)
RIGHT_MOTOR.wait_while(Motor.STATE_RUNNING)

MEDIUM_MOTOR.run_to_rel_pos(
    position_sp=6 * 360,   # degrees
    speed_sp=1000,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

SCREEN.image.paste(im=Image.open('/home/robot/image/Pinch middle.bmp'))
SCREEN.update()

LEFT_MOTOR.run_to_rel_pos(
    position_sp=-0.5 * 360,   # degrees
    speed_sp=250,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
RIGHT_MOTOR.run_to_rel_pos(
    position_sp=0.5 * 360,   # degrees
    speed_sp=250,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
LEFT_MOTOR.wait_while(Motor.STATE_RUNNING)
RIGHT_MOTOR.wait_while(Motor.STATE_RUNNING)

SPEAKER.play(wav_file='/home/robot/sound/Laughing 1.wav').wait()
