#!/usr/bin/env micropython


__all__ = 'Track3r',


from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.display import Display
from ev3dev2.sound import Sound


import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


class Track3r(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.medium_motor = MediumMotor(address=medium_motor_port)

        self.screen = Display(desc='Display')
        self.speaker = Sound()


if __name__ == '__main__':
    TRACK3R = Track3r()

    TRACK3R.keep_driving_by_ir_beacon(speed=100)
