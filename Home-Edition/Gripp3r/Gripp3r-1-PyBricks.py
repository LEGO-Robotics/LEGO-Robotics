#!/usr/bin/env pybricks-micropython


from pybricks import ev3brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop

from time import sleep


MEDIUM_MOTOR = Motor(port=Port.A)


MEDIUM_MOTOR.run_time(
    -50,
    1,
    Stop.BRAKE,
    wait=True)

MEDIUM_MOTOR.run_time(
    50,
    1,
    Stop.BRAKE,
    wait=True)

sleep(1)

MEDIUM_MOTOR.run_time(
    -50,
    1,
    Stop.BRAKE,
    wait=True)
