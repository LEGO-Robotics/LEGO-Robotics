#!/usr/bin/env python3


from kraz3_rctank_ev3dev1 import Kraz3

from threading import Thread


KRAZ3 = Kraz3()


Thread(
    target=KRAZ3.kungfu_maneouver_whenever_touched_or_remote_controlled,
    daemon=True).start()

KRAZ3.main()
