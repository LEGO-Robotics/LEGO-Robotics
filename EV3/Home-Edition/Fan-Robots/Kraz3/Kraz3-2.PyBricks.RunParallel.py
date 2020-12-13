#!/usr/bin/env pybricks-micropython

"""
Add the Kung-Fu manoeuvre
via the Touch Sensor and Remote Control of head and arms
"""

from pybricks.experimental import run_parallel

from kraz3_pybricks import Kraz3


KRAZ3 = Kraz3()


run_parallel(
    KRAZ3.kungfu_manoeuvre_whenever_touched_or_remote_controlled,
    KRAZ3.keep_driving_by_ir_beacon)
