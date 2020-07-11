#!/usr/bin/env python3


# BUG: https://github.com/ev3dev/ev3dev/issues/1422


from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor

from multiprocessing import Process


TOUCH_SENSOR = TouchSensor(address=INPUT_1)
IR_SENSOR = InfraredSensor(address=INPUT_4)
MOTOR = MediumMotor(address=OUTPUT_A)


def touch_to_turn_motor_clockwise():
    while True:
        if TOUCH_SENSOR.is_pressed:
            MOTOR.on_for_seconds(
                speed=100,
                seconds=1,
                brake=True,
                block=True)


def press_any_ir_remote_button_to_turn_motor_counterclockwise():
    while True:
        if IR_SENSOR.buttons_pressed(channel=1):
            MOTOR.on_for_seconds(
                speed=-100,
                seconds=1,
                brake=True,
                block=True)


Process(target=touch_to_turn_motor_clockwise,
        daemon=True).start()

press_any_ir_remote_button_to_turn_motor_counterclockwise()

# observation: both processes run successfully BUT WITH mutual blocking
# i.e. 1 process CANNOT interrupt the other process's Motor movement mid-stream
