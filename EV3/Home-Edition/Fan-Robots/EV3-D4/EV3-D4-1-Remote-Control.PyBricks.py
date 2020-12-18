#!/usr/bin/env pybricks-micropython

"""
This is a simple Remote Control loop effective for Channel 1.
Please note that the Beacon Button is not utilized.
"""

from ev3_d4_pybricks import EV3D4


ev3_d4 = EV3D4()

ev3_d4.keep_driving_by_ir_beacon()
