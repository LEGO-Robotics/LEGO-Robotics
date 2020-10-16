#!/usr/bin/env python3


from dinor3x_ev3dev1 import Dinor3x


DINOR3X = Dinor3x()

DINOR3X.calibrate_legs()

DINOR3X.left_motor.run_forever(speed_sp=-400)
DINOR3X.right_motor.run_forever(speed_sp=-400)

while not DINOR3X.button.any():
    pass
