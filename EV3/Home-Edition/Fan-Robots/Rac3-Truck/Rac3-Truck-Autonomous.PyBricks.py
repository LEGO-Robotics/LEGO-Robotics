#!/usr/bin/env pybricks-micropython

"""
When you run this program, the Racing Truck will drive around by itself!

Run this program if you want the Rac3 Truck to drive around autonomously
(by itself)
"""

from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Stop

from rac3_truck_pybricks import Rac3Truck


RAC3_TRUCK = Rac3Truck()

RAC3_TRUCK.reset()

while True:
    RAC3_TRUCK.drive_base.drive(
        speed=80,
        turn_rate=0)

    while RAC3_TRUCK.ir_sensor.distance() >= 30:
        pass

    RAC3_TRUCK.drive_base.stop()

    RAC3_TRUCK.steer_left()

    RAC3_TRUCK.speaker.play_file(file=SoundFile.OBJECT)

    RAC3_TRUCK.speaker.play_file(file=SoundFile.DETECTED)

    RAC3_TRUCK.left_motor.run_time(
        speed=-600,
        time=2000,
        then=Stop.COAST,
        wait=False)
    RAC3_TRUCK.right_motor.run_time(
        speed=-1000,
        time=2000,
        then=Stop.COAST,
        wait=True)

    RAC3_TRUCK.steer_right()

    RAC3_TRUCK.left_motor.run_time(
        speed=1000,
        time=2000,
        then=Stop.COAST,
        wait=False)
    RAC3_TRUCK.right_motor.run_time(
        speed=600,
        time=2000,
        then=Stop.COAST,
        wait=True)

    RAC3_TRUCK.steer_center()
