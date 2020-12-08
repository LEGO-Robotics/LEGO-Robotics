#!/usr/bin/env pybricks-micropython


from pybricks.parameters import Stop

from time import sleep

from rac3_truck_pybricks import Rac3Truck


RAC3_TRUCK = Rac3Truck()

RAC3_TRUCK.reset()

RAC3_TRUCK.left_motor.run_angle(
    speed=800,
    rotation_angle=5 * 360,
    then=Stop.HOLD,
    wait=False)
RAC3_TRUCK.right_motor.run_angle(
    speed=800,
    rotation_angle=5 * 360,
    then=Stop.HOLD,
    wait=True)

sleep(1)

RAC3_TRUCK.steer_right()

RAC3_TRUCK.left_motor.run_time(
    speed=1000,
    time=1000,
    then=Stop.HOLD,
    wait=False)
RAC3_TRUCK.right_motor.run_time(
    speed=600,
    time=1000,
    then=Stop.HOLD,
    wait=True)

sleep(1)

RAC3_TRUCK.steer_center()

RAC3_TRUCK.left_motor.run_angle(
    speed=800,
    rotation_angle=5 * 360,
    then=Stop.HOLD,
    wait=False)
RAC3_TRUCK.right_motor.run_angle(
    speed=800,
    rotation_angle=5 * 360,
    then=Stop.HOLD,
    wait=True)
