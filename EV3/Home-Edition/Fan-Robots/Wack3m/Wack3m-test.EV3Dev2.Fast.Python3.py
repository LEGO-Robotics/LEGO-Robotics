#!/usr/bin/env python3


from wack3m_ev3dev2 import Wack3m

from random import randint
from time import sleep


WACK3M = Wack3m(fast=True)

WACK3M.left_motor.on_for_seconds(
    speed=-30,
    seconds=1,
    brake=True,
    block=True)

WACK3M.left_motor.reset()

while True:
    sleep(0.1 + (3 - 0.1) * randint(1, 10) / 10)

    WACK3M.left_motor.on_for_degrees(
        speed=100,
        degrees=60,
        brake=False,
        block=True)

    WACK3M.left_motor.on_for_seconds(
        speed=-40,
        seconds=0.5,
        brake=True,
        block=True)

    sleep(1)
