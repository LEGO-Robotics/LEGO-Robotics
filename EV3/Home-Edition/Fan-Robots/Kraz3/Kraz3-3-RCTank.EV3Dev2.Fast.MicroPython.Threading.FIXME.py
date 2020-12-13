#!/usr/bin/env micropython


from threading import Thread

from kraz3_rctank_ev3dev2 import Kraz3


KRAZ3 = Kraz3(fast=True)

Thread(target=KRAZ3.react_to_color).start()

KRAZ3.main()
