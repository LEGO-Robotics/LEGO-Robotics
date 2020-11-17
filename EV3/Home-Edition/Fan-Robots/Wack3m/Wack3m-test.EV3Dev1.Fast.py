#!/usr/bin/env python3


from wack3m_ev3dev1 import Wack3m

from ev3dev.ev3 import Motor

from PIL import Image
from random import uniform
from time import sleep


WACK3M = Wack3m(fast=True)

WACK3M.screen.image.paste(im=Image.open('/home/robot/image/EV3.bmp'))
WACK3M.screen.update()

WACK3M.left_motor.run_timed(
    speed_sp=-300,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_HOLD)
WACK3M.left_motor.wait_while(Motor.STATE_RUNNING)

WACK3M.left_motor.reset()

while True:
    sleep(uniform(0.1, 3))

    WACK3M.left_motor.run_to_rel_pos(
        speed_sp=1000,
        position_sp=60,
        stop_action=Motor.STOP_ACTION_COAST)
    WACK3M.left_motor.wait_while(Motor.STATE_RUNNING)

    WACK3M.left_motor.run_timed(
        speed_sp=-400,
        time_sp=1000 * 0.5,
        stop_action=Motor.STOP_ACTION_HOLD)
    WACK3M.right_motor.wait_while(Motor.STATE_RUNNING)

    sleep(1)
