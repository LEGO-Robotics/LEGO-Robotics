#!/usr/bin/env micropython


from dinor3x_ev3dev2 import Dinor3x

from multiprocessing import Process


DINOR3X = Dinor3x(fast=True)

DINOR3X.close_mouth()

# FIXME: AttributeError: 'module' object has no attribute 'lseek'

Process(target=DINOR3X.keep_changing_speed_by_color).start()

Process(target=DINOR3X.keep_roaring_by_ir_beacon).start()

DINOR3X.keep_walking_by_ir_beacon()
