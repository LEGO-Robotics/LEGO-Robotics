#!/usr/bin/env pybricks-micropython


from pybricks.experimental import run_parallel

from kraz3_pybricks import Kraz3


KRAZ3 = Kraz3()


run_parallel(
    KRAZ3.kungfu_maneouver_whenever_touched_or_remote_controlled,
    KRAZ3.keep_driving_by_ir_beacon)
