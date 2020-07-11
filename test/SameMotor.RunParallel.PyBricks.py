#!/usr/bin/env pybricks-micropython


from pybricks.ev3devices import TouchSensor, InfraredSensor, Motor
from pybricks.parameters import Port, Stop

from pybricks.experimental import run_parallel


TOUCH_SENSOR = TouchSensor(port=Port.S1)
IR_SENSOR = InfraredSensor(port=Port.S4)
MOTOR = Motor(port=Port.A)


def touch_to_turn_motor_clockwise():
    while True:
        if TOUCH_SENSOR.pressed():
            MOTOR.run_time(
                speed=1000,   # deg/s
                time=1000,   # ms
                then=Stop.HOLD,
                wait=True)


def press_any_ir_remote_button_to_turn_motor_counterclockwise():
    while True:
        if IR_SENSOR.buttons(channel=1):
            MOTOR.run_time(
                speed=-1000,   # deg/s
                time=1000,   # ms
                then=Stop.HOLD,
                wait=True)


run_parallel(
    touch_to_turn_motor_clockwise,
    press_any_ir_remote_button_to_turn_motor_counterclockwise)

# observation: both threads run successfully BUT WITH mutual blocking
# i.e. 1 thread CANNOT interrupt the other thread's Motor movement mid-stream
