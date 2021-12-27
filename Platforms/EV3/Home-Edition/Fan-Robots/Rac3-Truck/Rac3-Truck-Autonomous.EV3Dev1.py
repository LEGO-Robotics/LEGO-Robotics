#!/usr/bin/env python3

"""
When you run this program, the Racing Truck will drive around by itself!

Run this program if you want the Rac3 Truck to drive around autonomously
(by itself)
"""

from ev3dev.ev3 import Motor

from rac3_truck_ev3dev1 import Rac3Truck


RAC3_TRUCK = Rac3Truck()

RAC3_TRUCK.reset()

while True:
    RAC3_TRUCK.left_motor.run_forever(speed_sp=800)
    RAC3_TRUCK.right_motor.run_forever(speed_sp=800)

    while RAC3_TRUCK.ir_sensor.proximity >= 30:
        pass

    RAC3_TRUCK.left_motor.stop(stop_action=Motor.STOP_ACTION_COAST)
    RAC3_TRUCK.right_motor.stop(stop_action=Motor.STOP_ACTION_COAST)

    RAC3_TRUCK.steer_left()

    RAC3_TRUCK.speaker.play(wav_file='/home/robot/sound/Object.wav').wait()
    RAC3_TRUCK.speaker.play(wav_file='/home/robot/sound/Detected.wav').wait()

    RAC3_TRUCK.left_motor.run_timed(
        speed_sp=-600,
        time_sp=2000,
        stop_action=Motor.STOP_ACTION_COAST)
    RAC3_TRUCK.right_motor.run_timed(
        speed_sp=-1000,
        time_sp=2000,
        stop_action=Motor.STOP_ACTION_COAST)
    RAC3_TRUCK.left_motor.wait_while(Motor.STATE_RUNNING)
    RAC3_TRUCK.right_motor.wait_while(Motor.STATE_RUNNING)

    RAC3_TRUCK.steer_right()

    RAC3_TRUCK.left_motor.run_timed(
        speed_sp=1000,
        time_sp=2000,
        stop_action=Motor.STOP_ACTION_COAST)
    RAC3_TRUCK.right_motor.run_timed(
        speed_sp=600,
        time_sp=2000,
        stop_action=Motor.STOP_ACTION_COAST)
    RAC3_TRUCK.left_motor.wait_while(Motor.STATE_RUNNING)
    RAC3_TRUCK.right_motor.wait_while(Motor.STATE_RUNNING)

    RAC3_TRUCK.steer_center()
