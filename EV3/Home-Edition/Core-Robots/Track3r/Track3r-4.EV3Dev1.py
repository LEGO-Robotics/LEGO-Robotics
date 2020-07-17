#!/usr/bin/env python3
# (MicroPython does not yet support Display as of 2020)


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, 
    InfraredSensor, INPUT_4,
    Screen, Sound
)

from PIL import Image
from time import sleep


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
LEFT_MOTOR = LargeMotor(address=OUTPUT_B)
RIGHT_MOTOR = LargeMotor(address=OUTPUT_C)

IR_SENSOR = InfraredSensor(address=INPUT_4)

SCREEN = Screen()
SPEAKER = Sound()


MEDIUM_MOTOR.run_timed(
    speed_sp=-200,   # deg/s
    time_sp=1000,   # ms 
    stop_action=Motor.STOP_ACTION_HOLD)
MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)


while True:
    if IR_SENSOR.proximity < 25:
        SCREEN.image.paste(im=Image.open('/home/robot/image/Pinch right.bmp'))
        SCREEN.update()

        LEFT_MOTOR.run_to_rel_pos(
            speed_sp=750,   # degrees/second
            position_sp=-1000,   # degrees
            stop_action=Motor.STOP_ACTION_HOLD)
        RIGHT_MOTOR.run_to_rel_pos(
            speed_sp=750,   # degrees/second
            position_sp=1000,   # degrees
            stop_action=Motor.STOP_ACTION_HOLD)
        LEFT_MOTOR.wait_while(Motor.STATE_RUNNING)
        RIGHT_MOTOR.wait_while(Motor.STATE_RUNNING)

        SCREEN.image.paste(im=Image.open('/home/robot/image/Angry.bmp'))
        SCREEN.update()
      
        MEDIUM_MOTOR.run_timed(
            speed_sp=1000,   # deg/s
            time_sp=0.3 * 1000,   # ms 
            stop_action=Motor.STOP_ACTION_HOLD)
        MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

        SPEAKER.play(wav_file='/home/robot/sound/Laughing 2.wav').wait()

        MEDIUM_MOTOR.run_timed(
            speed_sp=-200,   # deg/s
            time_sp=1000,   # ms 
            stop_action=Motor.STOP_ACTION_HOLD)
        MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

    else:
        SCREEN.image.paste(im=Image.open('/home/robot/image/Crazy 1.bmp'))
        SCREEN.update()
        
        LEFT_MOTOR.run_forever(speed_sp=750)
        RIGHT_MOTOR.run_forever(speed_sp=750)

        MEDIUM_MOTOR.run_timed(
            speed_sp=750,   # deg/s
            time_sp=0.1 * 1000,   # ms 
            stop_action=Motor.STOP_ACTION_HOLD)
        MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)

        sleep(0.1)

        SCREEN.image.paste(im=Image.open('/home/robot/image/Crazy 2.bmp'))
        SCREEN.update()

        # LEFT_MOTOR.run_forever(speed_sp=750)
        RIGHT_MOTOR.stop(stop_action=Motor.STOP_ACTION_HOLD)

        MEDIUM_MOTOR.run_timed(
            speed_sp=-300,   # deg/s (-100 too soft)
            time_sp=0.2 * 1000,   # ms 
            stop_action=Motor.STOP_ACTION_COAST)
        MEDIUM_MOTOR.wait_while(Motor.STATE_RUNNING)
