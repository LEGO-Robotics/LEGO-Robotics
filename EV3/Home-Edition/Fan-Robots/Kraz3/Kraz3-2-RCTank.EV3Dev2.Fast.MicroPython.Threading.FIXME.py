#!/usr/bin/env micropython

"""
Add the Kung-Fu manoeuvre
via the Touch Sensor and Remote Control of head and arms
"""

from threading import Thread

from kraz3_rctank_ev3dev2 import Kraz3


KRAZ3 = Kraz3(fast=True)


Thread(target=KRAZ3.kungfu_manoeuvre_whenever_touched_or_remote_controlled) \
    .start()

KRAZ3.main()
