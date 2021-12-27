#!/usr/bin/env micropython


from wack3m_ev3dev2 import Wack3m

from random import randint
from time import sleep


WACK3M = Wack3m()

WACK3M.start_up()

while True:
    sleep(0.1 + (3 - 0.1) * randint(1, 10) / 10)

    WACK3M.left_motor.on_for_degrees(
        speed=100,
        degrees=60,
        brake=False,
        block=True)

    WACK3M.left_motor.on_for_seconds(
        speed=-100,   # orig: -40
        seconds=0.5,
        brake=True,
        block=True)

    WACK3M.middle_motor.on_for_degrees(
        speed=100,
        degrees=170,
        brake=False,
        block=True)

    WACK3M.middle_motor.on_for_seconds(
        speed=-100,   # orig: -40
        seconds=0.5,   # orig: 0.4
        brake=False,
        block=True)

    WACK3M.right_motor.on_for_degrees(
        speed=100,
        degrees=60,
        brake=False,
        block=True)

    WACK3M.right_motor.on_for_seconds(
        speed=-100,   # orig: -40
        seconds=0.5,
        brake=True,
        block=True)

    sleep(1)
