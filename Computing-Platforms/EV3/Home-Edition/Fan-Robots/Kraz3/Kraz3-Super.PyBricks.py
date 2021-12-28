#!/usr/bin/env pybricks-micropython


from kraz3_pybricks import Kraz3


KRAZ3 = Kraz3()

while True:
    KRAZ3.drive_once_by_ir_beacon()

    KRAZ3.kungfu_manoeuvre_if_touched_or_remote_controlled()

    KRAZ3.react_to_color()