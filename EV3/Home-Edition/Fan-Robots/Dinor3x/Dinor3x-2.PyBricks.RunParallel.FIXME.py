#!/usr/bin/env pybricks-micropython


from pybricks.experimental import run_parallel

from dinor3x_pybricks import Dinor3x


DINOR3X = Dinor3x()


DINOR3X.calibrate_legs()

DINOR3X.open_mouth()

while True:
    # recalibrate legs so that the legs don't get too tired
    DINOR3X.calibrate_legs()

    DINOR3X.walk_until_blocked()

    # FIXME: TypeError: unsupported type for __hash__: 'bound_method'
    run_parallel(
        DINOR3X.roar,
        DINOR3X.run_away)
