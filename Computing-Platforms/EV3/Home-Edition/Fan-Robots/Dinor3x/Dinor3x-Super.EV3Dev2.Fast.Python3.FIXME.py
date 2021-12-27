#!/usr/bin/env python3


from dinor3x_ev3dev2 import Dinor3x


DINOR3X = Dinor3x(fast=True)

DINOR3X.close_mouth()

# FIXME: FastTouchSensor doesn't seem to detect press/release

while True:
    DINOR3X.roar_by_ir_beacon()
    DINOR3X.change_speed_by_color()
    DINOR3X.walk_by_ir_beacon()
