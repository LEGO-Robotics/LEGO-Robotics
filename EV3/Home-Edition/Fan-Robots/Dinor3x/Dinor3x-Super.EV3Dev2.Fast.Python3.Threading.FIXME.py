#!/usr/bin/env python3


from dinor3x_ev3dev2 import Dinor3x

from threading import Thread


DINOR3X = Dinor3x(fast=True)

# FIXME: ValueError: invalid syntax for integer with base 10: ''
Thread(target=DINOR3X.keep_changing_speed_by_color,
       daemon=True).start()

Thread(target=DINOR3X.keep_roaring_by_ir_beacon,
       daemon=True).start()

DINOR3X.keep_walking_by_ir_beacon()
