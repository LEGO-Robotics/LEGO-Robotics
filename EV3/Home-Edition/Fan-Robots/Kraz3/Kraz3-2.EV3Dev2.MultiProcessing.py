#!/usr/bin/env micropython


from kraz3_ev3dev2 import Kraz3

from multiprocessing import Process


KRAZ3 = Kraz3()


Process(target=KRAZ3.kungfu_maneouver_whenever_touched_or_remote_controlled) \
    .start()

KRAZ3.keep_driving_by_ir_beacon()
