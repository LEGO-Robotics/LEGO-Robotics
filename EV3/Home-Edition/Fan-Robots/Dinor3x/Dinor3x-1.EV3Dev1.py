#!/usr/bin/env python3


from ev3dev.ev3 import Motor

from dino3rex_ev3dev1 import Dinor3x


DINOR3X = Dinor3x()


DINOR3X.left_motor.run_forever(speed_sp=100)
DINOR3X.right_motor.run_forever(speed_sp=200)

while DINOR3X.touch_sensor.is_pressed:
    pass

DINOR3X.left_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)
DINOR3X.right_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)

DINOR3X.left_motor.run_forever(speed_sp=400)

while not DINOR3X.touch_sensor.is_pressed:
    pass

DINOR3X.left_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)

DINOR3X.left_motor.run_to_rel_pos(
    position_sp=-0.2 * 360,
    speed_sp=500,
    stop_action=Motor.STOP_ACTION_BRAKE)
DINOR3X.left_motor.wait_while(Motor.STATE_RUNNING)

DINOR3X.right_motor.run_forever(speed_sp=400)

while not DINOR3X.touch_sensor.is_pressed:
    pass

DINOR3X.right_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)

DINOR3X.right_motor.run_to_rel_pos(
    position_sp=-0.2 * 360,
    speed_sp=500,
    stop_action=Motor.STOP_ACTION_BRAKE)
DINOR3X.right_motor.wait_while(Motor.STATE_RUNNING)

DINOR3X.left_motor.reset()
DINOR3X.right_motor.reset()

DINOR3X.left_motor.run_forever(speed_sp=-400)
DINOR3X.right_motor.run_forever(speed_sp=-400)

while True:
    pass
