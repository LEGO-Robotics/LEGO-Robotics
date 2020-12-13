#!/usr/bin/env micropython


from multiprocessing import Process

from kraz3_ev3dev2 import Kraz3


KRAZ3 = Kraz3(fast=True)

Process(target=KRAZ3.react_to_color).start()

KRAZ3.keep_driving_by_ir_beacon()
