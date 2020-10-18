#!/usr/bin/env python3


from dinor3x_ev3dev1 import Dinor3x

from threading import Thread


DINOR3X = Dinor3x()

DINOR3X.close_mouth()

Thread(target=DINOR3X.keep_changing_speed_by_color,
       daemon=True).start()

Thread(target=DINOR3X.keep_roaring_by_ir_beacon,
       daemon=True).start()
       
DINOR3X.keep_walking_by_ir_beacon()
