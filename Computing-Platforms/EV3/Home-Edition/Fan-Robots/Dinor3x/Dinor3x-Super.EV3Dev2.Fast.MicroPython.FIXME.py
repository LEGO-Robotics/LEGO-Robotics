#!/usr/bin/env micropython


from dinor3x_ev3dev2 import Dinor3x


DINOR3X = Dinor3x(fast=True)

# FIXME: AttributeError: 'module' object has no attribute 'lseek'
DINOR3X.close_mouth()

while True:
    DINOR3X.roar_by_ir_beacon()
    DINOR3X.change_speed_by_color()
    DINOR3X.walk_by_ir_beacon()
