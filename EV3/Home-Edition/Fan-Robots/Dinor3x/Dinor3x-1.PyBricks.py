#!/usr/bin/env pybricks-micropython


from pybricks.parameters import Button

from dinor3x_pybricks import Dinor3x


DINOR3X = Dinor3x()

DINOR3X.calibrate_legs()

DINOR3X.left_motor.run(speed=-400)
DINOR3X.right_motor.run(speed=-400)

while not {Button.LEFT, Button.RIGHT,
           Button.UP, Button.DOWN,
           Button.CENTER}.intersection(DINOR3X.buttons.pressed()):
    pass
