#!/usr/bin/env micropython


import json

from ev3dev2.motor import Motor, LargeMotor, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sound import Sound

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


HAPPY_BIRTHDAY_SONG = json.load(open('Happy-Birthday-Song.EV3Dev.json'))


class BirthdayBot(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_C, right_motor_port: str = OUTPUT_B,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            display: bool = False,
            fast: bool = False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            motor_class=LargeMotor, polarity=Motor.POLARITY_INVERSED,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel,
            fast=fast)

        if display:
            from ev3dev2.display import Display

            self.screen = Display()

        self.speaker = Sound()

    def say_happy_birthday(self):
        self.speaker.speak(
            text='Happy Birthday to Mommy!',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    def sing_happy_birthday(self):
        self.speaker.play_song(
            song=HAPPY_BIRTHDAY_SONG,
            tempo=120,
            delay=0)

    def main(self):
        # self.say_happy_birthday()

        # self.sing_happy_birthday()
        self.keep_driving_by_ir_beacon()


if __name__ == '__main__':
    BIRTHDAY_BOT = BirthdayBot()

    BIRTHDAY_BOT.main()
