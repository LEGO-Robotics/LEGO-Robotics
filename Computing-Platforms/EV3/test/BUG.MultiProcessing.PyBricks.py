#!/usr/bin/env pybricks-micropython


from pybricks.ev3devices import TouchSensor, Motor
from pybricks.parameters import Port, Stop

from multiprocessing import Process


TOUCH_SENSOR = TouchSensor(port=Port.S1)
MOTOR = Motor(port=Port.A)


def motor_on_when_touched():
    while True:
        if TOUCH_SENSOR.pressed():
            MOTOR.run_time(
                speed=1000,   # deg/s
                time=1000,   # ms
                then=Stop.COAST,
                wait=True)


Process(target=motor_on_when_touched).start()
# *** BUG as of 2020 ***
# *** as soon as the Touch Sensor is pressed ***
# OSError: [Errno 5] EIO:
# Unexpected hardware input/output error with a motor or sensor:
# --> Try unplugging the sensor or motor and plug it back in again.
# --> To see which sensor or motor is causing the problem,
#     check the line in your script that matches
#     the line number given in the 'Traceback' above.
# --> Try rebooting the hub/brick if the problem persists.


while True:
    pass
