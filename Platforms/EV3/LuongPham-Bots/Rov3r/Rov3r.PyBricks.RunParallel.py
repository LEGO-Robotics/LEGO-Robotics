#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop

from pybricks.experimental import run_parallel

import os
import sys
sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class Rov3r(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 23
    AXLE_TRACK = 65

    def __init__(
            self,
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            gear_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1, color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)
        
        self.gear_motor = Motor(port=gear_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)
        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel


    def spin_gears(self, speed: float = 1000):
        while True:
            if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                self.gear_motor.run(speed=1000)

            else:
                self.gear_motor.stop()


    def change_screen_when_touched(self):
        while True:
            if self.touch_sensor.pressed():
                self.screen.load_image(ImageFile.ANGRY)
                
            else:
                self.screen.load_image(ImageFile.FORWARD)


    def make_noise_when_seeing_black(self):
        while True:
            if self.color_sensor.color == Color.BLACK:
                self.speaker.play_file(file=SoundFile.OUCH)


    def main(self):
        self.speaker.play_file(file=SoundFile.YES)

        run_parallel(
            self.make_noise_when_seeing_black,
            self.spin_gears,
            self.change_screen_when_touched,
            self.keep_driving_by_ir_beacon)
            

if __name__ == '__main__':
    ROV3R = Rov3r()

    ROV3R.main()
