#!/usr/bin/env micropython

"""
A simple "Follow Me" loop (built by NeXTSTORM and first used in EV3-D4 project)
"""

from kraz3_ev3dev2 import Kraz3


KRAZ3 = Kraz3(debug=True)

KRAZ3.keep_following_ir_beacon()
