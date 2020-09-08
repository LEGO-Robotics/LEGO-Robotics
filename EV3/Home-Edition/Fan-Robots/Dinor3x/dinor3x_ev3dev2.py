#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.sound import Sound

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


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
        self.ir_beacon_channel = ir_beacon_channel

        self.speaker = Sound()

    def calibrate_legs(self):
        self.tank_driver.on(
            left_speed=10,
            right_speed=20)

        while self.touch_sensor.is_pressed:
            pass

        self.tank_driver.off(brake=True)

        self.left_motor.on(speed=40)

        while not self.touch_sensor.is_pressed:
            pass

        self.left_motor.off(brake=True)

        self.left_motor.on_for_rotations(
            rotations=-0.2,
            speed=50,
            brake=True,
            block=True)

        self.right_motor.on(speed=40)

        while not self.touch_sensor.is_pressed:
            pass

        self.right_motor.off(brake=True)

        self.right_motor.on_for_rotations(
            rotations=-0.2,
            speed=50,
            brake=True,
            block=True)

        self.left_motor.reset()
        self.right_motor.reset()
