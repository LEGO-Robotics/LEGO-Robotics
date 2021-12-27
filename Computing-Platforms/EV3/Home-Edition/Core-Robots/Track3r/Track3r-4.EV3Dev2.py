#!/usr/bin/env python3
# (MicroPython does not yet support Display as of 2020)


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.display import Display
from ev3dev2.sound import Sound

from time import sleep


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)
STEER_DRIVER = MoveSteering(left_motor_port=OUTPUT_B,
                            right_motor_port=OUTPUT_C,
                            motor_class=LargeMotor)
                        
IR_SENSOR = InfraredSensor(address=INPUT_4)

SCREEN = Display()
SPEAKER = Sound()


MEDIUM_MOTOR.on_for_seconds(
    speed=-20,
    seconds=1, 
    block=True,
    brake=True)

while True:
    if IR_SENSOR.proximity < 25:
        SCREEN.image_filename(
            filename='/home/robot/image/Pinch right.bmp',
            clear_screen=True)
        SCREEN.update()

        STEER_DRIVER.on_for_degrees(
            steering=-100,
            speed=75,
            degrees=1000,
            brake=True,
            block=True)

        SCREEN.image_filename(
            filename='/home/robot/image/Angry.bmp',
            clear_screen=True)
        SCREEN.update()
      
        MEDIUM_MOTOR.on_for_seconds(
            seconds=0.3,
            speed=100,
            block=True,
            brake=True)

        SPEAKER.play_file(
            wav_file='/home/robot/sound/Laughing 2.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        MEDIUM_MOTOR.on_for_seconds(
            speed=-20,
            seconds=1, 
            block=True,
            brake=True)

    else:
        SCREEN.image_filename(
            filename='/home/robot/image/Crazy 1.bmp',
            clear_screen=True)
        SCREEN.update()
        
        TANK_DRIVER.on(
            left_speed=75,
            right_speed=75)

        MEDIUM_MOTOR.on_for_seconds(
            speed=75,
            seconds=0.1,
            block=True,
            brake=True)

        sleep(0.1)

        SCREEN.image_filename(
            filename='/home/robot/image/Crazy 2.bmp',
            clear_screen=True)
        SCREEN.update()
 
        STEER_DRIVER.on(
            steering=50,
            speed=75)

        MEDIUM_MOTOR.on_for_seconds(
            speed=-30,   # -10 too soft
            seconds=0.2,
            brake=False,
            block=True)
