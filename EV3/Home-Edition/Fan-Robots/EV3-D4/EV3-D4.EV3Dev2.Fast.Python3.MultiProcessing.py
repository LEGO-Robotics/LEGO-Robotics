#!/usr/bin/env python3


from multiprocessing import Process

from ev3_d4_ev3dev2 import EV3D4


ev3_d4 = EV3D4(fast=True)

Process(
    target=ev3_d4.color_sensor_loop,
    daemon=True).start()

Process(
    target=ev3_d4.touch_sensor_loop,
    daemon=True).start()

ev3_d4.main_switch_loop()
