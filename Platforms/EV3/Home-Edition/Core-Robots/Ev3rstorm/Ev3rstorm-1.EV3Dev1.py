#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, OUTPUT_B, OUTPUT_C,
    Screen
)

from PIL import Image


LEFT_FOOT_MOTOR = LargeMotor(address=OUTPUT_B)
RIGHT_FOOT_MOTOR = LargeMotor(address=OUTPUT_C)

SCREEN = Screen()


SCREEN.image.paste(
    im=Image.open('/home/robot/image/Neutral.bmp'),
    box=(0, 0))
SCREEN.update()

LEFT_FOOT_MOTOR.run_to_rel_pos(
    position_sp=5 * 360,   # degrees
    speed_sp=750,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
RIGHT_FOOT_MOTOR.run_to_rel_pos(
    position_sp=5 * 360,   # degrees
    speed_sp=750,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
LEFT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)
RIGHT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)

SCREEN.image.paste(
    im=Image.open('/home/robot/image/Middle left.bmp'),
    box=(0, 0))
SCREEN.update()
    
LEFT_FOOT_MOTOR.run_to_rel_pos(
    position_sp=5 * 360,   # degrees
    speed_sp=750,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
LEFT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)

SCREEN.image.paste(
    im=Image.open('/home/robot/image/Neutral.bmp'),
    box=(0, 0))
SCREEN.update()

LEFT_FOOT_MOTOR.run_to_rel_pos(
    position_sp=5 * 360,   # degrees
    speed_sp=750,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
RIGHT_FOOT_MOTOR.run_to_rel_pos(
    position_sp=5 * 360,   # degrees
    speed_sp=750,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
LEFT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)
RIGHT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)

SCREEN.image.paste(
    im=Image.open('/home/robot/image/Middle right.bmp'),
    box=(0, 0))
SCREEN.update()
    
RIGHT_FOOT_MOTOR.run_to_rel_pos(
    position_sp=5 * 360,   # degrees
    speed_sp=750,   # degrees per second
    stop_action=Motor.STOP_ACTION_BRAKE)
RIGHT_FOOT_MOTOR.wait_while(Motor.STATE_RUNNING)
