#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, OUTPUT_B
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4


LARGE_MOTOR = LargeMotor(OUTPUT_B)

IR_SENSOR = InfraredSensor(INPUT_4)


while True:
    if IR_SENSOR.proximity <= 20:
        LARGE_MOTOR.on(
            speed=100,
            brake=False,
            block=False)

    else:
        LARGE_MOTOR.on(
            speed=50,
            block=False,
            brake=False) 
