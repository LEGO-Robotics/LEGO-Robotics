#!/usr/bin/env micropython


from time import sleep

from rac3_truck_ev3dev2 import Rac3Truck


RAC3_TRUCK = Rac3Truck(fast=True)

RAC3_TRUCK.reset()

RAC3_TRUCK.steer_driver.on_for_rotations(
    steering=0,
    speed=80,
    rotations=5,
    brake=True,
    block=True)

sleep(1)

RAC3_TRUCK.steer_right()

RAC3_TRUCK.tank_driver.on_for_seconds(
    left_speed=100,
    right_speed=60,
    seconds=1,
    brake=True,
    block=True)

sleep(1)

RAC3_TRUCK.steer_center()

RAC3_TRUCK.steer_driver.on_for_rotations(
    steering=0,
    speed=80,
    rotations=5,
    brake=True,
    block=True)
