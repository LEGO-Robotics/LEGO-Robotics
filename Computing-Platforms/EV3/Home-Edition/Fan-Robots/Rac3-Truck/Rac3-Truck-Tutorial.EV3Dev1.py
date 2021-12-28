#!/usr/bin/env python3


from ev3dev.ev3 import Motor

from time import sleep

from rac3_truck_ev3dev1 import Rac3Truck


RAC3_TRUCK = Rac3Truck()

RAC3_TRUCK.reset()

RAC3_TRUCK.left_motor.run_to_rel_pos(
    speed_sp=800,
    position_sp=5 * 360,
    stop_action=Motor.STOP_ACTION_HOLD)
RAC3_TRUCK.right_motor.run_to_rel_pos(
    speed_sp=800,
    position_sp=5 * 360,
    stop_action=Motor.STOP_ACTION_HOLD)
RAC3_TRUCK.left_motor.wait_while(Motor.STATE_RUNNING)
RAC3_TRUCK.right_motor.wait_while(Motor.STATE_RUNNING)

sleep(1)

RAC3_TRUCK.steer_right()

RAC3_TRUCK.left_motor.run_timed(
    speed_sp=1000,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_HOLD)
RAC3_TRUCK.right_motor.run_timed(
    speed_sp=600,
    time_sp=1000,
    stop_action=Motor.STOP_ACTION_HOLD)
RAC3_TRUCK.left_motor.wait_while(Motor.STATE_RUNNING)
RAC3_TRUCK.right_motor.wait_while(Motor.STATE_RUNNING)

sleep(1)

RAC3_TRUCK.steer_center()

RAC3_TRUCK.left_motor.run_to_rel_pos(
    speed_sp=800,
    position_sp=5 * 360,
    stop_action=Motor.STOP_ACTION_HOLD)
RAC3_TRUCK.right_motor.run_to_rel_pos(
    speed_sp=800,
    position_sp=5 * 360,
    stop_action=Motor.STOP_ACTION_HOLD)
RAC3_TRUCK.left_motor.wait_while(Motor.STATE_RUNNING)
RAC3_TRUCK.right_motor.wait_while(Motor.STATE_RUNNING)
