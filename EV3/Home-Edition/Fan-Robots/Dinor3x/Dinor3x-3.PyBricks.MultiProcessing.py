#!/usr/bin/env pybricks-micropython


from pybricks.parameters import Stop

from multiprocessing import Process
from random import choice, randint

from dinor3x_pybricks import Dinor3x


DINOR3X = Dinor3x()


DINOR3X.calibrate_legs()

DINOR3X.open_mouth()

# main loop
while True:
    DINOR3X.leg_to_pos(
        speed=1000,
        left_position=0,
        right_position=0)

    DINOR3X.walk_until_blocked()

    Process(target=DINOR3X.roar).start()

    DINOR3X.back_away()

    DINOR3X.leg_to_pos(
        speed=1000,
        left_position=180,
        right_position=0)

    n_turn_rotations = randint(3, 10)

    if choice([True, False]):
        DINOR3X.left_motor.run_angle(
            rotation_angle=n_turn_rotations * 360,
            speed=600,
            then=Stop.HOLD,
            wait=False)
        DINOR3X.right_motor.run_angle(
            rotation_angle=n_turn_rotations * 360,
            speed=-600,
            then=Stop.HOLD,
            wait=True)

    else:
        DINOR3X.left_motor.run_angle(
            rotation_angle=n_turn_rotations * 360,
            speed=-600,
            then=Stop.HOLD,
            wait=False)
        DINOR3X.right_motor.run_angle(
            rotation_angle=n_turn_rotations * 360,
            speed=600,
            then=Stop.HOLD,
            wait=True)
