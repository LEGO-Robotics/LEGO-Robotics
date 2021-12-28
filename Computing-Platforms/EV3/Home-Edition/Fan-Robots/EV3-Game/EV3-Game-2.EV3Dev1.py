#!/usr/bin/env python3


from ev3dev.ev3 import Motor

from time import sleep

from ev3_game_ev3dev1 import EV3Game


EV3_GAME = EV3Game()

EV3_GAME.calibrate_grip()

sleep(1)

EV3_GAME.lift_cup()

sleep(1)

EV3_GAME.calibrate_grip()
