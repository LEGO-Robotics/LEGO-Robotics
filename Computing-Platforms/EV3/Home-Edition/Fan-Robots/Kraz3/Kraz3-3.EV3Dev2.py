#!/usr/bin/env micropython


from kraz3_ev3dev2 import Kraz3


KRAZ3 = Kraz3()

while True:
    KRAZ3.drive_once_by_ir_beacon()

    KRAZ3.react_to_color()