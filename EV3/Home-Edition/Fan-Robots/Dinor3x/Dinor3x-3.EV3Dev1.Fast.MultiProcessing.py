#!/usr/bin/env python3


from ev3dev.ev3 import Motor

from multiprocessing import Process
from random import choice, randint

from dinor3x_ev3dev1 import Dinor3x


DINOR3X = Dinor3x(fast=True)


DINOR3X.calibrate_legs()

DINOR3X.open_mouth()

while True:
    # FIXME: .leg_to_pos(...) hangs
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
        DINOR3X.left_motor.run_to_rel_pos(
            position_sp=n_turn_rotations * 360,   # degrees
            speed_sp=600,   # degrees per second
            stop_action=Motor.STOP_ACTION_BRAKE)
        DINOR3X.right_motor.run_to_rel_pos(
            position_sp=-n_turn_rotations * 360,   # degrees
            speed_sp=600,   # degrees per second
            stop_action=Motor.STOP_ACTION_BRAKE)
        DINOR3X.left_motor.wait_while(Motor.STATE_RUNNING)
        DINOR3X.right_motor.wait_while(Motor.STATE_RUNNING)

    else:
        DINOR3X.left_motor.run_to_rel_pos(
            position_sp=-n_turn_rotations * 360,   # degrees
            speed_sp=600,   # degrees per second
            stop_action=Motor.STOP_ACTION_BRAKE)
        DINOR3X.right_motor.run_to_rel_pos(
            position_sp=n_turn_rotations * 360,   # degrees
            speed_sp=600,   # degrees per second
            stop_action=Motor.STOP_ACTION_BRAKE)
        DINOR3X.left_motor.wait_while(Motor.STATE_RUNNING)
        DINOR3X.right_motor.wait_while(Motor.STATE_RUNNING)
