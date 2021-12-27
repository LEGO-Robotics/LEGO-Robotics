#!/usr/bin/env python3


from threading import Thread

from dinor3x_ev3dev1 import Dinor3x


DINOR3X = Dinor3x()


DINOR3X.calibrate_legs()

DINOR3X.open_mouth()

# main loop
while True:
    # recalibrate legs so that the legs don't get too tired
    DINOR3X.calibrate_legs()

    DINOR3X.walk_until_blocked()

    Thread(target=DINOR3X.roar).start()

    DINOR3X.back_away()
