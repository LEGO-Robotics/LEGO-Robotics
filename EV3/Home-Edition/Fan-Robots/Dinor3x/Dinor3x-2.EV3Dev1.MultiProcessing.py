#!/usr/bin/env python3


from ev3dev.ev3 import Motor

from multiprocessing import Process
from time import sleep

from dinor3x_ev3dev1 import Dinor3x


DINOR3X = Dinor3x()


DINOR3X.calibrate_legs()

DINOR3X.close_mouth()

while True:
    # recalibrate legs so that the legs don't get too tired
    DINOR3X.calibrate_legs()

    DINOR3X.left_motor.run_forever(speed_sp=-400)
    DINOR3X.right_motor.run_forever(speed_sp=-400)

    while DINOR3X.ir_sensor.proximity >= 25:
        pass

    DINOR3X.left_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)
    DINOR3X.right_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)

    Process(target=DINOR3X.roar).start()

    DINOR3X.left_motor.run_to_rel_pos(
        speed_sp=750,
        position_sp=3 * 360,
        stop_action=Motor.STOP_ACTION_BRAKE)
    DINOR3X.right_motor.run_to_rel_pos(
        speed_sp=750,
        position_sp=3 * 360,
        stop_action=Motor.STOP_ACTION_BRAKE)
    DINOR3X.left_motor.wait_while(Motor.STATE_RUNNING)
    DINOR3X.right_motor.wait_while(Motor.STATE_RUNNING)
