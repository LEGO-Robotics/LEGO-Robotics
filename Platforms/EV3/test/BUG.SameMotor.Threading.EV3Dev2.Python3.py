#!/usr/bin/env python3


from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor

from threading import Thread


TOUCH_SENSOR = TouchSensor(address=INPUT_1)
IR_SENSOR = InfraredSensor(address=INPUT_4)
MOTOR = MediumMotor(address=OUTPUT_A)


def touch_to_turn_motor_clockwise():
    while True:
        if TOUCH_SENSOR.is_pressed:
            MOTOR.on_for_seconds(
                speed=100,
                seconds=1,
                brake=True,
                block=True)


def press_any_ir_remote_button_to_turn_motor_counterclockwise():
    while True:
        if IR_SENSOR.buttons_pressed(channel=1):
            MOTOR.on_for_seconds(
                speed=-100,
                seconds=1,
                brake=True,
                block=True)


Thread(target=touch_to_turn_motor_clockwise,
       daemon=True).start()

press_any_ir_remote_button_to_turn_motor_counterclockwise()

# *** BUG as of 2020 ***
# *** as soon as both Touch Sensor and an IR button are pressed ***
# Traceback (most recent call last):
#   File "/home/robot/test/BUG.SameMotor.Threading.EV3Dev2.Python3.py", line 39, in <module>
#     press_any_ir_remote_button_to_turn_motor_counterclockwise()
#   File "/home/robot/test/BUG.SameMotor.Threading.EV3Dev2.Python3.py", line 33, in press_any_ir_remote_button_to_turn_motor_counterclockwise
#     block=True)
#   File "/usr/lib/python3/dist-packages/ev3dev2/motor.py", line 1048, in on_for_seconds
#     self.wait_until_not_moving()
#   File "/usr/lib/python3/dist-packages/ev3dev2/motor.py", line 928, in wait_until_not_moving
#     return self.wait(lambda state: self.STATE_RUNNING not in state or self.STATE_STALLED in state, timeout)
#   File "/usr/lib/python3/dist-packages/ev3dev2/motor.py", line 908, in wait
#     self._poll.poll(poll_tm)
# RuntimeError: concurrent poll() invocation
