#!/usr/bin/env python3


from ev3dev.ev3 import Motor

from dinor3x_ev3dev1 import Dinor3x
from dinor3x_util import cyclic_position_offset


DINOR3X = Dinor3x()


DINOR3X.calibrate_legs()


speed = 1000
left_position = 0
right_position = 0

DINOR3X.left_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)
DINOR3X.right_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)

DINOR3X.left_motor.run_to_rel_pos(
    speed_sp=speed,
    position_sp=left_position -
                cyclic_position_offset(
                    rotation_sensor=DINOR3X.left_motor.position,
                    cyclic_degrees=360),
    stop_action=Motor.STOP_ACTION_BRAKE)
# *** FIXME: the following hangs ***
DINOR3X.left_motor.wait_while(Motor.STATE_RUNNING)
