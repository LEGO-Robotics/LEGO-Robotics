#!/usr/bin/env pybricks-micropython


from wack3m_pybricks import Wack3m

from pybricks.media.ev3dev import ImageFile
from pybricks.parameters import Stop

from random import uniform
from time import sleep


WACK3M = Wack3m()

WACK3M.screen.load_image(ImageFile.EV3_ICON)

WACK3M.start_up()

while True:
    sleep(uniform(0.1, 3))

    WACK3M.left_motor.run_angle(
        speed=1000,
        rotation_angle=90,   # 60 too weak
        then=Stop.COAST,
        wait=True)

    WACK3M.left_motor.run_time(
        speed=-1000,   # orig: -400
        time=500,
        then=Stop.HOLD,
        wait=True)

    WACK3M.middle_motor.run_angle(
        speed=1000,
        rotation_angle=210,   # orig: 170
        then=Stop.COAST,
        wait=True)

    WACK3M.middle_motor.run_time(
        speed=-1000,   # orig: -400
        time=500,   # orig: 400
        then=Stop.COAST,
        wait=True)

    WACK3M.right_motor.run_angle(
        speed=1000,
        rotation_angle=90,   # 60 too weak
        then=Stop.COAST,
        wait=True)

    WACK3M.right_motor.run_time(
        speed=-1000,   # orig: -400
        time=500,
        then=Stop.HOLD,
        wait=True)

    sleep(1)
