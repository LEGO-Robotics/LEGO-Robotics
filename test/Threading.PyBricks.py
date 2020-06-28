#!/usr/bin/env pybricks-micropython


from pybricks.ev3devices import TouchSensor, Motor
from pybricks.parameters import Port, Stop

from threading import Thread


TOUCH_SENSOR = TouchSensor(port=Port.S1)
MOTOR = Motor(port=Port.A)


def motor_on_when_touched():
    while True:
        if TOUCH_SENSOR.pressed():
            MOTOR.run_time(
                speed=1000,   # deg/s
                time=1000,   # ms
                then=Stop.COAST,
                wait=True)


Thread(target=motor_on_when_touched).start()


while True:
    pass
