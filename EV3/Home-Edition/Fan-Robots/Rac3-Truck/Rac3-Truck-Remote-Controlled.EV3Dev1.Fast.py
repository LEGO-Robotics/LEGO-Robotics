#!/usr/bin/env python3

"""
When you run this program, you can control your truck with the IR Beacon!

Run this program if you want to remote-control your Rac3 Truck
with the IR Beacon.
"""

from rac3_truck_ev3dev1 import Rac3Truck

from time import sleep


RAC3_TRUCK = Rac3Truck(fast=True)

RAC3_TRUCK.reset()

sleep(1)

RAC3_TRUCK.keep_driving_by_ir_beacon()
