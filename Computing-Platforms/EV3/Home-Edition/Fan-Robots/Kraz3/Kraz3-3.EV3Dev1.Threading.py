#!/usr/bin/env python3


from threading import Thread

from kraz3_ev3dev1 import Kraz3


KRAZ3 = Kraz3()

Thread(
    target=KRAZ3.react_to_color,
    daemon=True).start()

KRAZ3.keep_driving_by_ir_beacon()
