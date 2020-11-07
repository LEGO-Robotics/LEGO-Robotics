#!/usr/bin/env python3


from ev3dev.ev3 import Motor

from time import sleep

from ev3_game_ev3dev1 import EV3Game


EV3_GAME = EV3Game()

EV3_GAME.calibrate_grip()

sleep(1)

EV3_GAME.grip_motor.run_to_rel_pos(
    speed_sp=100,
    position_sp=220,
    stop_action=Motor.STOP_ACTION_HOLD)
EV3_GAME.grip_motor.wait_while(Motor.STATE_RUNNING)

sleep(1)

EV3_GAME.calibrate_grip()
