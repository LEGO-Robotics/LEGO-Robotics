#!/usr/bin/env python3


from wack3m_ev3dev2 import Wack3m

from random import uniform
from time import sleep


WACK3M = Wack3m(use_screen=True)

WACK3M.screen.image_filename(
    filename='/home/robot/image/EV3 icon.bmp',
    clear_screen=True)
WACK3M.screen.update()

WACK3M.left_motor.on_for_seconds(
    speed=-30,
    seconds=1,
    brake=True,
    block=True)

WACK3M.left_motor.reset()

while True:
    sleep(uniform(0.1, 3))

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
