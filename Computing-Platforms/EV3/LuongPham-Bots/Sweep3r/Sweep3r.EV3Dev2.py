#!/usr/bin/env python3


from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.display import Display
from ev3dev2.sound import Sound

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


class Sweep3r(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B, right_foot_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_foot_motor_port, right_motor_port=right_foot_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.medium_motor = MediumMotor(address=medium_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.screen = Display()
        self.speaker = Sound()


    def drill(self, speed: float = 100):
        if self.ir_sensor.beacon(channel=self.ir_beacon_channel):
            self.medium_motor.on_for_rotations(
                speed=speed,
                rotations=2,
                block=True,
                brake=True)


    def move_when_touched(self):    
        if self.touch_sensor.is_pressed:
            self.tank_driver.on_for_seconds(
                left_speed=100,
                right_speed=-100,
                seconds=2,
                brake=True,
                block=True)


    def move_when_see_smothing(self):
        if self.color_sensor.reflected_light_intensity > 30:
            self.tank_driver.on_for_seconds(
                left_speed=-100,
                right_speed=100,
                seconds=2,
                brake=True,
                block=True)

        
    def main(self, speed: float = 100):
        self.screen.image_filename(
            filename='/home/robot/image/Neutral.bmp',
            clear_screen=True)
        self.screen.update()
    
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

            self.move_when_touched()

            self.move_when_see_smothing()

            self.drill(speed=speed)


if __name__ == '__main__':
    SWEEP3R = Sweep3r()

    SWEEP3R.main()
