#!/usr/bin/env python3


from dinor3x_ev3dev2 import Dinor3x

from multiprocessing import Process


DINOR3X = Dinor3x(fast=True)

# FIXME: FastTouchSensor doesn't seem to detect press/release
Process(target=DINOR3X.keep_changing_speed_by_color,
        daemon=True).start()

Process(target=DINOR3X.keep_roaring_by_ir_beacon,
        daemon=True).start()

DINOR3X.keep_walking_by_ir_beacon()
