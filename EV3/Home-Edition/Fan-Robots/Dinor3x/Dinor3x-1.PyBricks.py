#!/usr/bin/env pybricks-micropython


from pybricks.parameters import Button, Stop

from dinor3x_pybricks import Dinor3x


DINOR3X = Dinor3x()

while not {Button.LEFT, Button.RIGHT,
           Button.UP, Button.DOWN,
           Button.CENTER}.intersection(DINOR3X.buttons.pressed()):
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
