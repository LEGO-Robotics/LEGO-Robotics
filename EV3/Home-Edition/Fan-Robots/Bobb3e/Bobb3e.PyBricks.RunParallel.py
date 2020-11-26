#!/usr/bin/env pybricks-micropython


from bobb3e_pybricks import Bobb3e

from pybricks.experimental import run_parallel


BOBB3E = Bobb3e()

BOBB3E.screen.print('BOBB3E')

run_parallel(
    BOBB3E.keep_driving_or_operating_forks_by_ir_beacon,
    BOBB3E.sound_alarm_whenever_reversing)
