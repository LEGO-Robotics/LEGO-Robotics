#!/usr/bin/env python3


from bobb3e_ev3dev1 import Bobb3e

from multiprocessing import Process


BOBB3E = Bobb3e()

BOBB3E.screen.draw.text(
    xy=(3, 2),
    text='BOBB3E',
    fill=None,
    font=None,
    anchor=None,
    spacing=4,
    align='left',
    direction=None,
    features=None,
    language=None,
    stroke_width=0,
    stroke_fill=None)
BOBB3E.screen.update()

Process(target=BOBB3E.sound_alarm_whenever_reversing,
        daemon=True).start()

BOBB3E.keep_driving_or_operating_lift_by_ir_beacon(speed=1000)
