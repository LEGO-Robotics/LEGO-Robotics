#!/usr/bin/env python3


from kraz3_ev3dev1 import Kraz3


KRAZ3 = Kraz3()

while True:
    KRAZ3.drive_once_by_ir_beacon()

    KRAZ3.kungfu_maneouver_if_touched_or_remote_controlled()
