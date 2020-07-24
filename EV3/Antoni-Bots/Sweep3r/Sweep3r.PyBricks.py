#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile
from pybricks.parameters import Button, Port, Stop

import os
import sys
sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class Sweep3r(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 40
    AXLE_TRACK = 110


    def __init__(
            self,
            left_foot_motor_port: Port = Port.B, right_foot_motor_port: Port = Port.C,
            medium_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1, color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):            
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_foot_motor_port, right_motor_port=right_foot_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.medium_motor = Motor(port=medium_motor_port)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)
        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel


    def drill(self, speed: float = 1000):
        if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.medium_motor.run_angle(
                speed=speed,
                rotation_angle=2 * 360,
                then=Stop.HOLD,
                wait=True)


    def move_when_touched(self):    
        if self.touch_sensor.pressed():
            self.drive_base.turn(angle=100)


    def move_when_see_smothing(self):
        if self.color_sensor.reflection() > 30:
             self.drive_base.turn(angle=-100)

        
    def main(self, speed: float = 1000):
        self.screen.load_image(ImageFile.PINCHED_MIDDLE)
    
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

            self.move_when_touched()

            self.move_when_see_smothing()

            self.drill(speed=speed)


if __name__ == '__main__':
    SWEEP3R = Sweep3r()

    SWEEP3R.main()
