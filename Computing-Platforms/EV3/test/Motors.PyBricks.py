#!/usr/bin/env pybricks-micropython


from pybricks.ev3devices import Motor
from pybricks.parameters import Port


MOTOR_0 = Motor(port=Port.B)
MOTOR_1 = Motor(port=Port.C)

MOTOR_0.run(speed=100)
MOTOR_1.run(speed=100)

while True:
    pass
