#!/usr/bin/env pybricks-micropython


from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction, Stop 


LARGE_MOTOR = Motor(port=Port.B,
                    positive_direction=Direction.CLOCKWISE)

MEDIUM_MOTOR = Motor(port=Port.A,
                     positive_direction=Direction.CLOCKWISE)


LARGE_MOTOR.run(speed=1000)

for i in range(3):
    MEDIUM_MOTOR.run_time(
        speed=100,
        time=1000,
        then=Stop.COAST,
        wait=True)

    MEDIUM_MOTOR.run_time(
        speed=-100,
        time=1000,
        then=Stop.COAST,
        wait=True)
