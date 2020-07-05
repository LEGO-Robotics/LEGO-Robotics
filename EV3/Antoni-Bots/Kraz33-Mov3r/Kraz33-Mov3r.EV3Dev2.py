#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound


FRONT_MOTOR = LargeMotor(address=OUTPUT_B)
BACK_MOTOR = LargeMotor(address=OUTPUT_C)
GEAR_MOTOR = MediumMotor(address=OUTPUT_A)
TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_C,
                       right_motor_port=OUTPUT_B)

TOUCH_SENSOR = TouchSensor(address=INPUT_1)
COLOR_SENSOR = ColorSensor(address=INPUT_3)
IR_SENSOR = InfraredSensor(address=INPUT_4)

SPEAKER = Sound()

LEDS = Leds()

while True:
    if IR_SENSOR.proximity <= 5:
        TANK_DRIVER.on_for_rotations(
            left_speed=-100,
            right_speed=100,
            rotations=2,
            brake=True,
            block=True)
