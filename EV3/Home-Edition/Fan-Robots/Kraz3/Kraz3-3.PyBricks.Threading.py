#!/usr/bin/env pybricks-micropython


from threading import Thread

from kraz3_pybricks import Kraz3


KRAZ3 = Kraz3()

Thread(target=KRAZ3.react_to_color).start()

KRAZ3.keep_driving_by_ir_beacon()
