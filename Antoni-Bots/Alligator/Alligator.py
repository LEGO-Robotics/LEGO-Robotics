#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_3
from ev3dev2.sensor.lego import InfraredSensor, TouchSensor, ColorSensor
from ev3dev2.sound import Sound


MEDIUM_MOTOR = MediumMotor(OUTPUT_A)
TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)
STEER_DRIVER = MoveSteering(left_motor_port=OUTPUT_B,
                            right_motor_port=OUTPUT_C,
                            motor_class=LargeMotor)

TOUCH_SENSOR = TouchSensor(INPUT_1)
IR_SENSOR = InfraredSensor(INPUT_4)
COLOR_SENSOR = ColorSensor(INPUT_3)

SPEAKER = Sound()


def drive_by_ir_beacon(channel: int = 1, speed: float = 100):
    if IR_SENSOR.top_left(channel) and IR_SENSOR.top_right(channel):
        # go forward
        TANK_DRIVER.on(
            left_speed=speed,
            right_speed=speed)

    elif IR_SENSOR.bottom_left(channel) and IR_SENSOR.bottom_right(channel):
        # go backward
        TANK_DRIVER.on(
            left_speed=-speed,
            right_speed=-speed)

    elif IR_SENSOR.top_left(channel) and IR_SENSOR.bottom_right(channel):
        # turn around left
        TANK_DRIVER.on(
            left_speed=-speed,
            right_speed=speed)

    elif IR_SENSOR.top_right(channel) and IR_SENSOR.bottom_left(channel):
        # turn around right
        TANK_DRIVER.on(
            left_speed=speed,
            right_speed=-speed)

    elif IR_SENSOR.top_left(channel):
        # turn left
        TANK_DRIVER.on(
            left_speed=0,
            right_speed=speed)

    elif IR_SENSOR.top_right(channel):
        # turn right
        TANK_DRIVER.on(
            left_speed=speed,
            right_speed=0)

    elif IR_SENSOR.bottom_left(channel):
        # left backward
        TANK_DRIVER.on(
            left_speed=0,
            right_speed=-speed)

    elif IR_SENSOR.bottom_right(channel):
        # right backward
        TANK_DRIVER.on(
            left_speed=-speed,
            right_speed=0)

    else:
        TANK_DRIVER.off(brake=False)


while True:
    drive_by_ir_beacon(
        channel=1,
        speed=100)

    if IR_SENSOR.proximity < 30:
        MEDIUM_MOTOR.on_for_seconds(
            speed=50,
            seconds=0.9,
            block=True,
            brake=True)

    if COLOR_SENSOR.reflected_light_intensity > 30:
        TANK_DRIVER.on(
            left_speed=50,
            right_speed=50)
    else:
        TANK_DRIVER.off(brake=False)

    if TOUCH_SENSOR.is_pressed:
        for i in range(3):
            SPEAKER.play_file(
                wav_file='/home/robot/sound/Okey-dokey.wav',
                volume=100,
                play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

            TANK_DRIVER.on_for_seconds(
                left_speed=-50,
                right_speed=50,
                seconds=0.6,
                brake=True,
                block=True)
            
            TANK_DRIVER.on_for_seconds(
                left_speed=50,
                right_speed=-50,
                seconds=0.6,
                brake=True,
                block=True)
