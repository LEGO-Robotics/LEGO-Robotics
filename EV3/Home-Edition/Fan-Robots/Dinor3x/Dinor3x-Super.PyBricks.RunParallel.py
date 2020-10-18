#!/usr/bin/env pybricks-micropython


from dinor3x_pybricks import Dinor3x

from pybricks.experimental import run_parallel


DINOR3X = Dinor3x()

run_parallel(
    DINOR3X.keep_changing_speed_by_color,
    DINOR3X.keep_roaring_by_ir_beacon,
    DINOR3X.keep_walking_by_ir_beacon)
