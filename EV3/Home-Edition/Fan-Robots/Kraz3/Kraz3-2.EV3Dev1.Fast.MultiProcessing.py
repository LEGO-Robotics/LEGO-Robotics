#!/usr/bin/env python3

"""
Add the Kung-Fu Maneouver
via the Touch Sensor and Remote Control of head and arms
"""

from kraz3_ev3dev1 import Kraz3

from multiprocessing import Process


KRAZ3 = Kraz3(fast=True)


Process(
    target=KRAZ3.kungfu_maneouver_whenever_touched_or_remote_controlled,
    daemon=True).start()

KRAZ3.keep_driving_by_ir_beacon()
