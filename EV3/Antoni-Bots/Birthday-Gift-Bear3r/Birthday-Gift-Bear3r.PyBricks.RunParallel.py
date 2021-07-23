#!/usr/bin/env pybricks-micropython


import json

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile
from pybricks.parameters import Button, Direction, Port

from pybricks.experimental import run_parallel

# import sys
# sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


HAPPY_BIRTHDAY_SONG = json.load(open('Happy-Birthday-Song.PyBricks.json'))


class BirthdayGiftBear3r(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 44   # milimeters
    AXLE_TRACK = 88       # milimeters

    def __init__(
            self,
            left_motor_port: Port = Port.C, right_motor_port: Port = Port.B,
            medium_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4,
            driving_ir_beacon_channel: int = 1,
            non_driving_ir_beacon_channel: int = 2):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity='inversed',
            ir_sensor_port=ir_sensor_port,
            ir_beacon_channel=driving_ir_beacon_channel)

        self.arm_control_motor = Motor(port=medium_motor_port,
                                       positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.non_driving_ir_beacon_channel = non_driving_ir_beacon_channel

    def start_up(self):
        self.screen.load_image(ImageFile.NEUTRAL)

    def sing_happy_birthday_whenever_ir_beacon_pressed(self):
        while True:
            ir_beacon_button_pressed = \
                set(self.ir_sensor.buttons(
                        channel=self.non_driving_ir_beacon_channel))

            if ir_beacon_button_pressed == {Button.BEACON}:
                self.speaker.play_notes(
                    notes=HAPPY_BIRTHDAY_SONG,
                    tempo=120)

    def main(self):
        self.start_up()

        run_parallel(
            self.keep_driving_by_ir_beacon,
            self.sing_happy_birthday_whenever_ir_beacon_pressed)


if __name__ == '__main__':
    BIRTHDAY_GIFT_BEAR3R = BirthdayGiftBear3r()

    BIRTHDAY_GIFT_BEAR3R.main()
