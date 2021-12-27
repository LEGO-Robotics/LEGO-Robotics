#!/usr/bin/env pybricks-micropython


import json

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.media.ev3dev import ImageFile
from pybricks.parameters import Button, Direction, Port

# import sys
# sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


HAPPY_BIRTHDAY_SONG = json.load(open('Happy-Birthday-Song.PyBricks.json'))


class BirthdayGiftPresent3r(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 44   # milimeters
    AXLE_TRACK = 88       # milimeters

    def __init__(
            self,
            left_motor_port: Port = Port.C, right_motor_port: Port = Port.B,
            medium_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4,
            driving_ir_beacon_channel: int = 1,
            non_driving_ir_beacon_channel: int = 4):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity='inversed',
            ir_sensor_port=ir_sensor_port,
            ir_beacon_channel=driving_ir_beacon_channel)

        self.arm_control_motor = \
            Motor(port=medium_motor_port,
                  positive_direction=Direction.COUNTERCLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.non_driving_ir_beacon_channel = non_driving_ir_beacon_channel

        # self.non_driving_ir_beacon_channels = set(range(1, 5))
        # self.non_driving_ir_beacon_channels.remove(driving_ir_beacon_channel)

    def start_up(self):
        self.screen.load_image(ImageFile.NEUTRAL)

        self.speaker.set_speech_options(
            language='en',
            voice='m3',
            speed=None,
            pitch=None)

        self.speaker.set_volume(
            volume=100,
            which='_all_')

    def lower_or_raise_arm_by_ir_beacon(self):
        non_driving_ir_beacon_button_pressed = \
            self.ir_sensor.buttons(channel=self.non_driving_ir_beacon_channel)
        #   *** Using sum(...) like below leads to                       ***
        #   *** TypeError: unsupported type for __hash__: 'bound_method' ***
        #   sum(self.ir_sensor.buttons(channel=channel)
        #       for channel in self.non_driving_ir_beacon_channels)

        if {Button.LEFT_DOWN, Button.RIGHT_DOWN}.intersection(
                non_driving_ir_beacon_button_pressed):
            self.arm_control_motor.run(speed=-100)

        elif {Button.LEFT_UP, Button.RIGHT_UP}.intersection(
                non_driving_ir_beacon_button_pressed):
            self.arm_control_motor.run(speed=100)

        else:
            self.arm_control_motor.hold()

    def keep_controlling_arm_by_ir_beacon(self):
        while True:
            self.lower_or_raise_arm_by_ir_beacon()

    def say_happy_birthday_if_touch_sensor_pressed(self):
        if self.touch_sensor.pressed():
            self.speaker.say(text='Happy Birthday, My Love!')

    def say_happy_birthday_whenever_touch_sensor_pressed(self):
        while True:
            self.say_happy_birthday_if_touch_sensor_pressed()

    def sing_happy_birthday_if_ir_beacon_button_pressed(self):
        if Button.BEACON in (self.ir_sensor.buttons(channel=1) +
                             self.ir_sensor.buttons(channel=2) +
                             self.ir_sensor.buttons(channel=3) +
                             self.ir_sensor.buttons(channel=4)):
            self.speaker.play_notes(
                notes=HAPPY_BIRTHDAY_SONG,
                tempo=120)

    def sing_happy_birthday_whenever_ir_beacon_button_pressed(self):
        while True:
            self.sing_happy_birthday_if_ir_beacon_button_pressed()


if __name__ == '__main__':
    GIFT_PRESENT3R = BirthdayGiftPresent3r()

    GIFT_PRESENT3R.start_up()

    while True:
        GIFT_PRESENT3R.drive_once_by_ir_beacon()

        GIFT_PRESENT3R.lower_or_raise_arm_by_ir_beacon()

        GIFT_PRESENT3R.say_happy_birthday_if_touch_sensor_pressed()

        GIFT_PRESENT3R.sing_happy_birthday_if_ir_beacon_button_pressed()
