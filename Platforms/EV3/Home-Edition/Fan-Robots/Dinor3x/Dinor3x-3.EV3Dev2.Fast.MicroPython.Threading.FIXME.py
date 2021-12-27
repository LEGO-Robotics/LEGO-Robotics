#!/usr/bin/env micropython


from random import randint
from threading import Thread

from dinor3x_ev3dev2 import Dinor3x


DINOR3X = Dinor3x(fast=True)


DINOR3X.calibrate_legs()

DINOR3X.open_mouth()

# main loop
while True:
    DINOR3X.leg_to_pos(
        speed=100,
        left_position=0,
        right_position=0)

    DINOR3X.walk_until_blocked()

    Thread(target=DINOR3X.roar).start()

    DINOR3X.back_away()

    DINOR3X.leg_to_pos(
        speed=100,
        left_position=180,
        right_position=0)

    n_turn_rotations = randint(3, 10)

    if randint(0, 1):
        DINOR3X.tank_driver.on_for_rotations(
           left_speed=60,
           right_speed=-60,
           rotations=n_turn_rotations,
           brake=True,
           block=True)

    else:
        DINOR3X.tank_driver.on_for_rotations(
           left_speed=-60,
           right_speed=60,
           rotations=n_turn_rotations,
           brake=True,
           block=True)
