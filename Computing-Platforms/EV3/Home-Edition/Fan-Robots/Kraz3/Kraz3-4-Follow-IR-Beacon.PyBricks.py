#!/usr/bin/env pybricks-micropython

"""
A simple "Follow Me" loop (built by NeXTSTORM and first used in EV3-D4 project)
"""

from kraz3_pybricks import Kraz3


KRAZ3 = Kraz3(debug=True)

KRAZ3.keep_following_ir_beacon()
