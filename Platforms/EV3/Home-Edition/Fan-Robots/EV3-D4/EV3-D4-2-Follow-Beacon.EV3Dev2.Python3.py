#!/usr/bin/env python3

"""
This is a simple follow-me loop.
Turn on the Beacon Button of your Remote Control and EV3-D4 will follow you.
"""

from ev3_d4_ev3dev2 import EV3D4


ev3_d4 = EV3D4(debug=True)

ev3_d4.keep_following_ir_beacon()
