#!/usr/bin/env micropython


from kraz3_ev3dev2 import Kraz3

from threading import Thread


KRAZ3 = Kraz3()


Thread(target=KRAZ3.kungfu_maneouver_whenever_touched_or_remote_controlled) \
    .start()

KRAZ3.keep_driving_by_ir_beacon()
