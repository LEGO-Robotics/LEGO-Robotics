#!/usr/bin/env micropython


from bobb3e_ev3dev2 import Bobb3e

from threading import Thread


BOBB3E = Bobb3e(fast=True)

BOBB3E.console.text_at(
    text='BOBB3E',
    column=3,
    row=2,
    reset_console=False,
    inverse=False,
    alignment='L')

Thread(target=BOBB3E.sound_alarm_whenever_reversing).start()

BOBB3E.keep_driving_or_operating_lift_by_ir_beacon(speed=100)
