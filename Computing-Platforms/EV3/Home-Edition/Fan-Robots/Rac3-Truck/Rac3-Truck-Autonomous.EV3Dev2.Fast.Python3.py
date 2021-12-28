#!/usr/bin/env python3

"""
When you run this program, the Racing Truck will drive around by itself!

Run this program if you want the Rac3 Truck to drive around autonomously
(by itself)
"""

from ev3dev2.sound import Sound

from rac3_truck_ev3dev2 import Rac3Truck


RAC3_TRUCK = Rac3Truck(fast=True)


RAC3_TRUCK.reset()

while True:
    RAC3_TRUCK.tank_driver.on(
        left_speed=80,
        right_speed=80)

    while RAC3_TRUCK.ir_sensor.proximity >= 30:
        pass

    RAC3_TRUCK.tank_driver.off(brake=False)

    RAC3_TRUCK.steer_left()

    RAC3_TRUCK.speaker.play_file(
        wav_file='/home/robot/sound/Object.wav',
        volume=100,
        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
    RAC3_TRUCK.speaker.play_file(
        wav_file='/home/robot/sound/Detected.wav',
        volume=100,
        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    RAC3_TRUCK.tank_driver.on_for_seconds(
        left_speed=-60,
        right_speed=-100,
        seconds=2,
        brake=False,
        block=True)

    RAC3_TRUCK.steer_right()

    RAC3_TRUCK.tank_driver.on_for_seconds(
        left_speed=100,
        right_speed=60,
        seconds=2,
        brake=False,
        block=True)

    RAC3_TRUCK.steer_center()
