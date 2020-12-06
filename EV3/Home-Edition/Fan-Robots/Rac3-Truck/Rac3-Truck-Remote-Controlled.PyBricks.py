#!/usr/bin/env pybricks-micropython

"""
When you run this program, you can control your truck with the IR Beacon!
"""

from rac3_truck_pybricks import Rac3Truck

from time import sleep


RAC3_TRUCK = Rac3Truck()

RAC3_TRUCK.reset()

sleep(1)

RAC3_TRUCK.keep_driving_by_ir_beacon()
