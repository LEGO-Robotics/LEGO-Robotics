#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor

from threading import Thread


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


Thread(target=touch_to_turn_motor_clockwise).start()

press_any_ir_remote_button_to_turn_motor_counterclockwise()
# *** BUG as of 2020 ***
# *** just the presence of the above parallel Thread makes this main thread crash ***
# Traceback (most recent call last):
#   File "/home/robot/test/BUG.SameMotor.Threading.EV3Dev2.MicroPython.py", line 38, in <module>
#   File "/home/robot/test/BUG.SameMotor.Threading.EV3Dev2.MicroPython.py", line 29, in press_any_ir_remote_button_to_turn_motor_counterclockwise
#   File "ev3dev2/motor.py", line 1048, in on_for_seconds
#   File "ev3dev2/motor.py", line 928, in wait_until_not_moving
#   File "ev3dev2/motor.py", line 908, in wait
# OSError: 4
