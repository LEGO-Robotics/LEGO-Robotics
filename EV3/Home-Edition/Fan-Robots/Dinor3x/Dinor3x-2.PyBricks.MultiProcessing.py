#!/usr/bin/env pybricks-micropython


from pybricks.parameters import Stop

from multiprocessing import Process
from time import sleep

from dinor3x_pybricks import Dinor3x


DINOR3X = Dinor3x()


DINOR3X.calibrate_legs()

DINOR3X.jaw_motor.run(speed=200)
sleep(1)
DINOR3X.jaw_motor.stop()

while True:
    # recalibrate legs so that the legs don't get too tired
    DINOR3X.calibrate_legs()

    DINOR3X.left_motor.run(speed=-400)
    DINOR3X.right_motor.run(speed=-400)

    while DINOR3X.ir_sensor.distance() >= 25:
        pass

    DINOR3X.left_motor.stop()
    DINOR3X.right_motor.stop()

    Process(target=DINOR3X.roar).start()

    DINOR3X.run_away()
