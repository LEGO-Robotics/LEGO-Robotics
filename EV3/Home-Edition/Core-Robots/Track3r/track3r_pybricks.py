#!/usr/bin/env pybricks-micropython


__all__ = 'Track3r',


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

import os
import sys
sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class Track3r(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 26
    AXLE_TRACK = 140

    def __init__(
            self,
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            medium_motor_port: Port = Port.A,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.medium_motor = Motor(port=medium_motor_port)


if __name__ == '__main__':
    TRACK3R = Track3r()

    TRACK3R.keep_driving_by_ir_beacon(speed=1000)
