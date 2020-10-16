#!/usr/bin/env micropython


from dinor3x_ev3dev2 import Dinor3x


DINOR3X = Dinor3x()

DINOR3X.calibrate_legs()

DINOR3X.steer_driver.on(
    steering=0,
    speed=-40)

while not DINOR3X.button.any():
    pass
