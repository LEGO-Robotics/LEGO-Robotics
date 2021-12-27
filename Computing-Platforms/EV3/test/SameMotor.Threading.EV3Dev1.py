#!/usr/bin/env python3


from ev3dev.ev3 import TouchSensor, INPUT_1, InfraredSensor, INPUT_4, RemoteControl, MediumMotor, OUTPUT_A

from threading import Thread


TOUCH_SENSOR = TouchSensor(address=INPUT_1)
REMOTE_CONTROL = RemoteControl(sensor=InfraredSensor(address=INPUT_4),
                               channel=1)
MOTOR = MediumMotor(address=OUTPUT_A)


def touch_to_turn_motor_clockwise():
    while True:
        if TOUCH_SENSOR.is_pressed:
            MOTOR.run_timed(
                speed_sp=1000,   # deg/s
                time_sp=1000,   # ms
                stop_action=MediumMotor.STOP_ACTION_HOLD)


def press_any_ir_remote_button_to_turn_motor_counterclockwise():
    while True:
        if REMOTE_CONTROL.buttons_pressed:
            MOTOR.run_timed(
                speed_sp=-1000,   # deg/s
                time_sp=1000,   # ms
                stop_action=MediumMotor.STOP_ACTION_HOLD)


Thread(target=touch_to_turn_motor_clockwise,
       daemon=True).start()

press_any_ir_remote_button_to_turn_motor_counterclockwise()

# observation: both threads run successfully WITHOUT mutual blocking
# i.e. 1 thread CAN interrupt/reverse the other thread's Motor movement mid-stream
