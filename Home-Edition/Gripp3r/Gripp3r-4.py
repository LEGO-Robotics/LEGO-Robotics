#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, MoveSteering, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sound import Sound


MEDIUM_MOTOR = MediumMotor(OUTPUT_A)
SPEAKER = Sound()

TANK_DRIVE = MoveTank(left_motor_port=OUTPUT_B, right_motor_port=OUTPUT_C)
STEER_DRIVE = MoveSteering(left_motor_port=OUTPUT_B, right_motor_port=OUTPUT_C)

IR_SENSOR = InfraredSensor(INPUT_4)


def drive_by_beacon(channel: int = 1, speed: float = 100):
    if IR_SENSOR.top_left(channel) and IR_SENSOR.top_right(channel):
        TANK_DRIVE.on(
            left_speed=speed,
            right_speed=speed)
    
    elif IR_SENSOR.bottom_left(channel) and IR_SENSOR.bottom_right(channel):
        TANK_DRIVE.on(
            left_speed=-speed,
            right_speed=-speed)

    elif IR_SENSOR.top_left(channel) and IR_SENSOR.bottom_left(channel):
        STEER_DRIVE.on(
            steering=-100,
            speed=speed)

    elif IR_SENSOR.top_right(channel) and IR_SENSOR.bottom_right(channel):
        STEER_DRIVE.on(
            steering=100,
            speed=speed)

    elif IR_SENSOR.top_left(channel):
        STEER_DRIVE.on(
            steering=-50,
            speed=speed)

    elif IR_SENSOR.top_right(channel):
        STEER_DRIVE.on(
            steering=50,
            speed=speed)

    elif IR_SENSOR.bottom_left(channel):
        TANK_DRIVE.on(
            left_speed=0,
            right_speed=-speed)

    elif IR_SENSOR.bottom_right(channel):
        TANK_DRIVE.on(
            left_speed=-speed,
            right_speed=0)

    else:
        TANK_DRIVE.off(brake=False)


while True:
    drive_by_beacon(
        channel=1,
        speed=100)
