#!/usr/bin/env pybricks-micropython

"""
This is a simple follow-me loop.
Turn on the Beacon Button of your Remote Control and EV3-D4 will follow you.
"""

from ev3_d4_pybricks import EV3D4


ev3_d4 = EV3D4()

ev3_d4.keep_following_ir_beacon()
