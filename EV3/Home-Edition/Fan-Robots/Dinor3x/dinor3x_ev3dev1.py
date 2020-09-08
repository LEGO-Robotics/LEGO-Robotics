#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4,
    Sound
)

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank


class Dinor3x(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            jaw_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.jaw_motor = MediumMotor(address=jaw_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=ir_beacon_channel)

        self.speaker = Sound()

    def calibrate_legs(self):
        self.left_motor.run_forever(speed_sp=100)
        self.right_motor.run_forever(speed_sp=200)

        while self.touch_sensor.is_pressed:
            pass

        self.left_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)
        self.right_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)

        self.left_motor.run_forever(speed_sp=400)

        while not self.touch_sensor.is_pressed:
            pass

        self.left_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)

        self.left_motor.run_to_rel_pos(
            position_sp=-0.2 * 360,
            speed_sp=500,
            stop_action=Motor.STOP_ACTION_BRAKE)
        self.left_motor.wait_while(Motor.STATE_RUNNING)

        self.right_motor.run_forever(speed_sp=400)

        while not self.touch_sensor.is_pressed:
            pass

        self.right_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)

        self.right_motor.run_to_rel_pos(
            position_sp=-0.2 * 360,
            speed_sp=500,
            stop_action=Motor.STOP_ACTION_BRAKE)
        self.right_motor.wait_while(Motor.STATE_RUNNING)

        self.left_motor.reset()
        self.right_motor.reset()
