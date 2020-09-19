#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Stop
from dinor3x_pybricks import Dinor3x

DINOR3X = Dinor3x()

while True:
    DINOR3X.calibrate_legs()

    DINOR3X.left_motor.run_time(
        speed=-400,
        time=5000,
        then=Stop.BRAKE,
        wait=False)

    DINOR3X.right_motor.run_time(
        speed=-400,
        time=5000,
        then=Stop.BRAKE,
        wait=True)

    # TODO: terminate by Brick buttons
