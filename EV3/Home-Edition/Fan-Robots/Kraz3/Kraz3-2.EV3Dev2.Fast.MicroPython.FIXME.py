#!/usr/bin/env micropython

"""
Add the Kung-Fu manoeuvre
via the Touch Sensor and Remote Control of head and arms
"""

from kraz3_ev3dev2 import Kraz3


KRAZ3 = Kraz3(fast=True)

while True:
    KRAZ3.drive_once_by_ir_beacon()

    KRAZ3.kungfu_manoeuvre_if_touched_or_remote_controlled()
