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
    
    else:
        TANK_DRIVE.off(brake=False)


while True:
    drive_by_beacon()
