#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port
from pybricks.tools import wait

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class RoboDoz3r(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 24   # milimeters
    AXLE_TRACK = 100      # milimeters

    def __init__(
            self,
            left_motor_port: Port = Port.C, right_motor_port: Port = Port.B,
            shovel_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4,
            tank_drive_ir_beacon_channel: int = 1,
            shovel_control_ir_beacon_channel: int = 4):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity='inversed',
            ir_sensor_port=ir_sensor_port,
            ir_beacon_channel=tank_drive_ir_beacon_channel)

        self.shovel_motor = Motor(port=shovel_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.shovel_control_ir_beacon_channel = \
            shovel_control_ir_beacon_channel

    def raise_or_lower_shovel_once_by_ir_beacon(self):
        ir_beacon_button_pressed = \
            set(self.ir_sensor.buttons(
                    channel=self.shovel_control_ir_beacon_channel))

        # raise the shovel
        if ir_beacon_button_pressed.intersection(
                {Button.LEFT_UP, Button.RIGHT_UP}):

            self.shovel_motor.run(speed=100)

        # lower the shovel
        elif ir_beacon_button_pressed.intersection(
                {Button.LEFT_DOWN, Button.RIGHT_DOWN}):

            self.shovel_motor.run(speed=-100)

        else:
            self.shovel_motor.hold()

    def main(self,
             driving_speed: float = 1000   # mm/s
             ):

        while True:
            self.drive_once_by_ir_beacon(speed=driving_speed)

            self.raise_or_lower_shovel_once_by_ir_beacon()


if __name__ == '__main__':
    ROBODOZ3R = RoboDoz3r()

    ROBODOZ3R.main()
