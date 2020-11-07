#!/usr/bin/env python3


from time import sleep

from ev3_game_ev3dev2 import EV3Game


EV3_GAME = EV3Game(fast=True)

EV3_GAME.calibrate_grip()

sleep(1)

EV3_GAME.grip_motor.on_for_degrees(
    speed=10,
    degrees=220,
    brake=True,
    block=True)

sleep(1)

EV3_GAME.calibrate_grip()
