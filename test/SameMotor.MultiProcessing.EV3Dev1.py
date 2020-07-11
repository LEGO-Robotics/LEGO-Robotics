#!/usr/bin/env python3


# BUG: https://github.com/ev3dev/ev3dev/issues/1422


from ev3dev.ev3 import TouchSensor, INPUT_1, InfraredSensor, INPUT_4, RemoteControl, MediumMotor, OUTPUT_A

from multiprocessing import Process


TOUCH_SENSOR = TouchSensor(address=INPUT_1)
REMOTE_CONTROL = RemoteControl(sensor=InfraredSensor(address=INPUT_4),
                               channel=1)
MOTOR = MediumMotor(address=OUTPUT_A)


def touch_to_turn_motor():
    while True:
        if TOUCH_SENSOR.is_pressed:
            MOTOR.run_timed(
                speed_sp=1000,   # deg/s
                time_sp=1000,   # ms
                stop_action=MediumMotor.STOP_ACTION_HOLD)


def press_ir_button_to_turn_motor():
    while True:
        if REMOTE_CONTROL.buttons_pressed:
            MOTOR.run_timed(
                speed_sp=-1000,   # deg/s
                time_sp=1000,   # ms
                stop_action=MediumMotor.STOP_ACTION_HOLD)


Process(target=touch_to_turn_motor,
        daemon=True).start()

press_ir_button_to_turn_motor()
