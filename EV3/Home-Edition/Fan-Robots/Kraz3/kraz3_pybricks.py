#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor, ColorSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.tools import wait

# import sys
# sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class Kraz3(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 24
    AXLE_TRACK = 100

    def __init__(
            self,
            left_motor_port: Port = Port.C, right_motor_port: Port = Port.B,
            wiggle_motor_port: Port = Port.A,
            polarity: str = 'inversed',
            touch_sensor_port: Port = Port.S1,
            color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity=polarity,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.wiggle_motor = Motor(port=wiggle_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    def main(self):
        while True:
            self.drive_once_by_ir_beacon()


if __name__ == '__main__':
    KRAZ3 = Kraz3()

    KRAZ3.main()
