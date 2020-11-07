#!/usr/bin/env pybricks-micropython


from pybricks.parameters import Stop

from time import sleep

from ev3_game_pybricks import EV3Game


EV3_GAME = EV3Game()

EV3_GAME.calibrate_grip()

sleep(1)

EV3_GAME.grip_motor.run_angle(
    speed=100,
    rotation_angle=220,
    then=Stop.HOLD,
    wait=True)

sleep(1)

EV3_GAME.calibrate_grip()
