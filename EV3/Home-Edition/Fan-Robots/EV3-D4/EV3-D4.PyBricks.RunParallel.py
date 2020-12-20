#!/usr/bin/env pybricks-micropython


from pybricks.experimental import run_parallel

from ev3_d4_pybricks import EV3D4


ev3_d4 = EV3D4()

run_parallel(
    ev3_d4.main_switch_loop,
    ev3_d4.color_sensor_loop,
    ev3_d4.touch_sensor_loop)
