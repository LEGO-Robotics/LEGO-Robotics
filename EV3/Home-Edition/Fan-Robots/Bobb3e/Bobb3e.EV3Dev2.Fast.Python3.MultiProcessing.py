#!/usr/bin/env python3


from bobb3e_ev3dev2 import Bobb3e

from multiprocessing import Process


BOBB3E = Bobb3e(fast=True)

BOBB3E.console.text_at(
    text='BOBB3E',
    column=3,
    row=2,
    reset_console=False,
    inverse=False,
    alignment='L')

Process(target=BOBB3E.sound_alarm_whenever_reversing,
        daemon=True).start()

BOBB3E.keep_driving_or_operating_lift_by_ir_beacon(speed=100)
