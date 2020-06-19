#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, InfraredSensor
from ev3dev2.display import Display
from ev3dev2.sound import Sound


TANK_DRIVER = MoveTank(left_motor_port=OUTPUT_B,
                       right_motor_port=OUTPUT_C,
                       motor_class=LargeMotor)

MEDIUM_MOTOR = MediumMotor(OUTPUT_A)

COLOR_SENSOR = ColorSensor(INPUT_2)
TOUCH_SENSOR = TouchSensor(INPUT_1)
IR_SENSOR = InfraredSensor(INPUT_4)

SCREEN = Display()
SPEAKER = Sound()


while True:
    ...
