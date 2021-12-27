#!/usr/bin/env python3


from multiprocessing import Process

from kraz3_ev3dev1 import Kraz3


KRAZ3 = Kraz3()

Process(
    target=KRAZ3.react_to_color,
    daemon=True).start()

KRAZ3.keep_driving_by_ir_beacon()
