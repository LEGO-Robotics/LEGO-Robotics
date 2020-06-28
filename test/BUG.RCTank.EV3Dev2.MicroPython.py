#!/usr/bin/env micropython


# *** BUG as of 2020: happens in MICROPYTHON only (fine in Python3) ***
# ERROR:ev3dev2.control.rc_tank:'InfraredSensor' object has no attribute '_state'
# Traceback (most recent call last):
#   File "ev3dev2/control/rc_tank.py", line 40, in main
#   File "ev3dev2/sensor/lego.py", line 959, in process
# AttributeError: 'InfraredSensor' object has no attribute '_state'


from ev3dev2.motor import OUTPUT_B, OUTPUT_C
from ev3dev2.control.rc_tank import RemoteControlledTank


RC_TANK = RemoteControlledTank(left_motor_port=OUTPUT_B, right_motor_port=OUTPUT_C,
                               polarity='normal', speed=1000, channel=1)

RC_TANK.main()
