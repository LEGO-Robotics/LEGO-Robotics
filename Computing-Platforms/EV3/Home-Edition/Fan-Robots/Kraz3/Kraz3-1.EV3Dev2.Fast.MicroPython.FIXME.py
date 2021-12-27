#!/usr/bin/env micropython

"""
Control the left and right tracks using the Remote Control
"""

from kraz3_ev3dev2 import Kraz3


KRAZ3 = Kraz3(fast=True)

KRAZ3.keep_driving_by_ir_beacon()
