#!/usr/bin/env python3


from kraz3_ev3dev1 import Kraz3


KRAZ3 = Kraz3(fast=True)

while True:
    KRAZ3.drive_once_by_ir_beacon()

    KRAZ3.react_to_color()
