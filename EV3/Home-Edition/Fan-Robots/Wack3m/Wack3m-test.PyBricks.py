#!/usr/bin/env pybricks-micropython


from wack3m_pybricks import Wack3m

from pybricks.media.ev3dev import ImageFile
from pybricks.parameters import Stop

from random import uniform
from time import sleep


WACK3M = Wack3m()

WACK3M.screen.load_image(ImageFile.EV3_ICON)

WACK3M.left_motor.run_time(
    speed=-300,
    time=1000,
    then=Stop.HOLD,
    wait=True)

WACK3M.left_motor.reset_angle(angle=0)

while True:
    sleep(uniform(0.1, 3))

    WACK3M.left_motor.run_angle(
        speed=1000,
        rotation_angle=60,
        then=Stop.COAST,
        wait=True)

    WACK3M.left_motor.run_time(
        speed=-400,
        time=1000 * 0.5,
        then=Stop.HOLD,
        wait=True)

    sleep(1)
