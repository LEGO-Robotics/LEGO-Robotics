#!/usr/bin/env python3


from multiprocessing import Process

from dinor3x_ev3dev1 import Dinor3x


DINOR3X = Dinor3x(fast=True)


DINOR3X.calibrate_legs()

DINOR3X.open_mouth()

while True:
    # recalibrate legs so that the legs don't get too tired
    DINOR3X.calibrate_legs()

    DINOR3X.walk_until_blocked()

    Process(target=DINOR3X.roar).start()

    DINOR3X.run_away()
