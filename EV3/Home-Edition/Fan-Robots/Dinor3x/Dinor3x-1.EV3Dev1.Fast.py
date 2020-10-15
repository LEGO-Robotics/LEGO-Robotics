#!/usr/bin/env python3


from ev3dev.ev3 import Motor

from dinor3x_ev3dev1 import Dinor3x


DINOR3X = Dinor3x(fast=True)


while not DINOR3X.button.any():
    # recalibrate legs every 5 seconds so that the legs don't get too tired
    DINOR3X.calibrate_legs()

    DINOR3X.left_motor.run_timed(
        speed_sp=-400,
        time_sp=5000,
        stop_action=Motor.STOP_ACTION_BRAKE)
    DINOR3X.right_motor.run_timed(
        speed_sp=-400,
        time_sp=5000,
        stop_action=Motor.STOP_ACTION_BRAKE)
    DINOR3X.left_motor.wait_while(Motor.STATE_RUNNING)
    DINOR3X.right_motor.wait_while(Motor.STATE_RUNNING)
