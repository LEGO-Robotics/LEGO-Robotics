#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4, INPUT_1
from ev3dev2.sensor.lego import InfraredSensor, TouchSensor
from ev3dev2.sound import Sound


MEDIUM_MOTOR = MediumMotor(OUTPUT_A)
TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)

IR_SENSOR = InfraredSensor(INPUT_4)
TOUCH_SENSOR = TouchSensor(INPUT_1)

SPEAKER = Sound()


def drive_by_ir_beacon(channel: int = 1, speed: float = 100):
    if IR_SENSOR.top_left(channel) and IR_SENSOR.top_right(channel):
        # go forward
        TANK_DRIVER.on_for_seconds(
            left_speed=-speed,
            right_speed=0,
            seconds=1,
            brake=True,
            block=True)

        TANK_DRIVER.on_for_seconds(
            left_speed=0,
            right_speed=-speed,
            seconds=1,
            brake=True,
            block=True)

    elif IR_SENSOR.bottom_left(channel) and IR_SENSOR.bottom_right(channel):
        # go backward
        TANK_DRIVER.on_for_seconds(
            left_speed=speed,
            right_speed=0,
            seconds=1,
            brake=True,
            block=True)

        TANK_DRIVER.on_for_seconds(
            left_speed=0,
            right_speed=speed,
            seconds=1,
            brake=True,
            block=True)

    elif IR_SENSOR.top_left(channel) and IR_SENSOR.bottom_right(channel):
        # turn around left
        TANK_DRIVER.on_for_seconds(
            left_speed=0,
            right_speed=-speed,
            seconds=1,
            brake=True,
            block=True)

        TANK_DRIVER.on_for_seconds(
            left_speed=speed,
            right_speed=0,
            seconds=1,
            brake=True,
            block=True)

    elif IR_SENSOR.top_right(channel) and IR_SENSOR.bottom_left(channel):
        # turn around right
        TANK_DRIVER.on_for_seconds(
            left_speed=-speed,
            right_speed=0,
            seconds=1,
            brake=True,
            block=True)

        TANK_DRIVER.on_for_seconds(
            left_speed=0,
            right_speed=speed,
            seconds=1,
            brake=True,
            block=True)

    elif IR_SENSOR.top_left(channel):
        # turn left
        TANK_DRIVER.on(
            left_speed=0,
            right_speed=-speed)

    elif IR_SENSOR.top_right(channel):
        # turn right
        TANK_DRIVER.on(
            left_speed=-speed,
            right_speed=0)

    elif IR_SENSOR.bottom_left(channel):
        # left backward
        TANK_DRIVER.on(
            left_speed=0,
            right_speed=speed)

    elif IR_SENSOR.bottom_right(channel):
        # right backward
        TANK_DRIVER.on(
            left_speed=speed,
            right_speed=0)

    else:
        TANK_DRIVER.off(brake=False)


def shoot_objects_by_ir_beacon(channel: int = 1, speed: float = 1):
    if IR_SENSOR.beacon(channel=channel):
        MEDIUM_MOTOR.on_for_rotations(
            speed=speed,
            rotations=3,
            block=True,
            brake=True)

        while IR_SENSOR.beacon(channel=channel):
            pass

    else:
        MEDIUM_MOTOR.off(brake=False)


def seek_the_fruit(distance: float = 20):
    if IR_SENSOR.proximity <= distance:
        SPEAKER.play_file(
            wav_file='/home/robot/sound/Fanfare.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)


def run_if_chased(speed: float = 100):
    if TOUCH_SENSOR.is_pressed:
        # go forward
        for i in range(3):
            TANK_DRIVER.on_for_seconds(
                left_speed=-speed,
                right_speed=0,
                seconds=1,
                brake=True,
                block=True)

            TANK_DRIVER.on_for_seconds(
                left_speed=0,
                right_speed=-speed,
                seconds=1,
                brake=True,
                block=True)

while True:
    drive_by_ir_beacon(
        channel=1,
        speed=100)

    shoot_objects_by_ir_beacon(
        channel=1,
        speed=100)

    seek_the_fruit(distance=20)

    run_if_chased(speed=100)
