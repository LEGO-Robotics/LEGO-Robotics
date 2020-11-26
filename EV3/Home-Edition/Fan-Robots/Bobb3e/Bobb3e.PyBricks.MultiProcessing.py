#!/usr/bin/env pybricks-micropython


from bobb3e_pybricks import Bobb3e

from multiprocessing import Process


BOBB3E = Bobb3e()

BOBB3E.screen.print('BOBB3E')

Process(target=BOBB3E.sound_alarm_whenever_reversing).start()

BOBB3E.keep_driving_or_operating_lift_by_ir_beacon(speed=1000)
