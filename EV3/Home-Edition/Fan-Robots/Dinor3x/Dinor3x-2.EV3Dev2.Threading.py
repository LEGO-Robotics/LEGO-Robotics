#!/usr/bin/env micropython


from threading import Thread
from time import sleep

from dinor3x_ev3dev2 import Dinor3x


DINOR3X = Dinor3x()


DINOR3X.calibrate_legs()

DINOR3X.jaw_motor.on(
    speed=20,
    block=False,
    brake=False)

sleep(1)

DINOR3X.jaw_motor.off(brake=True)

while True:
    # recalibrate legs so that the legs don't get too tired
    DINOR3X.calibrate_legs()

    DINOR3X.steer_driver.on(
        steering=0,
        speed=-40)

    while DINOR3X.ir_sensor.proximity >= 25:
        pass

    DINOR3X.steer_driver.off(brake=True)

    Thread(target=DINOR3X.roar).start()

    DINOR3X.steer_driver.on_for_rotations(
        speed=75,
        steering=0,
        rotations=3,
        brake=True,
        block=True)
