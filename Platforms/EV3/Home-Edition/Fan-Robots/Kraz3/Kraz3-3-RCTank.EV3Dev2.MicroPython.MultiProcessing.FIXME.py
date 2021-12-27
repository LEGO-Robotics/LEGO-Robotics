#!/usr/bin/env micropython


from multiprocessing import Process

from kraz3_rctank_ev3dev2 import Kraz3


KRAZ3 = Kraz3()

Process(target=KRAZ3.react_to_color).start()

KRAZ3.main()
