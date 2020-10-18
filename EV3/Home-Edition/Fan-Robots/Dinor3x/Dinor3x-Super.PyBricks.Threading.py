#!/usr/bin/env pybricks-micropython


from dinor3x_pybricks import Dinor3x

from threading import Thread


DINOR3X = Dinor3x()

Thread(target=DINOR3X.keep_changing_speed_by_color).start()
Thread(target=DINOR3X.keep_roaring_by_ir_beacon).start()
DINOR3X.keep_walking_by_ir_beacon()
