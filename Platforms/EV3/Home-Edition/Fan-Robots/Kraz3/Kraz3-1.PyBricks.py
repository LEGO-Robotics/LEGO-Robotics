#!/usr/bin/env pybricks-micropython

"""
Control the left and right tracks using the Remote Control
"""

from kraz3_pybricks import Kraz3


KRAZ3 = Kraz3()

KRAZ3.keep_driving_by_ir_beacon()
