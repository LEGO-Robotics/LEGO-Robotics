#!/usr/bin/env micropython


from dinor3x_ev3dev2 import Dinor3x

from threading import Thread


DINOR3X = Dinor3x()

DINOR3X.close_mouth()

# FIXME: ValueError: invalid syntax for integer with base 10: ''
Thread(target=DINOR3X.keep_changing_speed_by_color).start()

Thread(target=DINOR3X.keep_roaring_by_ir_beacon).start()

DINOR3X.keep_walking_by_ir_beacon()
