#!/usr/bin/env python3


# BUG: https://github.com/ev3dev/ev3dev/issues/1422


from ev3dev.ev3 import TouchSensor, INPUT_1, MediumMotor, OUTPUT_A

from multiprocessing import Process


TOUCH_SENSOR = TouchSensor(address=INPUT_1)
MOTOR = MediumMotor(address=OUTPUT_A)


def motor_on_when_touched():
    while True:
        if TOUCH_SENSOR.is_pressed:
            MOTOR.run_timed(
                speed_sp=1000,   # deg/s
                time_sp=1000,   # ms
                stop_action=MediumMotor.STOP_ACTION_COAST)


Process(target=motor_on_when_touched,
        daemon=True).start()


while True:
    pass
