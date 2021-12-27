#!/usr/bin/env python3


from ev3dev2.control.GyroBalancer import GyroBalancer, GracefulShutdown
from ev3dev2.sensor.lego import InfraredSensor

import time


IR_SENSOR = InfraredSensor()
IR_SENSOR.mode = IR_SENSOR.MODE_IR_REMOTE


BALANC3R = GyroBalancer()
BALANC3R.balance()


while True:
    button_code = IR_SENSOR.value()

    if button_code == IR_SENSOR.TOP_LEFT_TOP_RIGHT:
        BALANC3R.move_forward()

    elif button_code == IR_SENSOR.TOP_LEFT_BOTTOM_RIGHT:
        BALANC3R.rotate_right()
    
    elif button_code == IR_SENSOR.BOTTOM_LEFT_TOP_RIGHT:
        BALANC3R.rotate_left()
    
    elif button_code == IR_SENSOR.BOTTOM_LEFT_BOTTOM_RIGHT:
        BALANC3R.move_backward()

    else:
        BALANC3R.stop()
