#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.robotics import DriveBase
from pybricks.parameters import Button, Direction, Port, Stop

from threading import Thread

import sys
sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class CuriosityRov3r(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 35   # milimeters
    AXLE_TRACK = 130      # milimeters


    def __init__(
            self,
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            medium_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1, color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)
            
        self.medium_motor = Motor(port=medium_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)
        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    
    def spin_fan(self, speed: float = 1000):
        while True:
            if self.color_sensor.reflection() > 20:
                self.medium_motor.run(speed=speed)

            else:
                self.medium_motor.stop()

            
    def say_when_touched(self):
        while True:
            if self.touch_sensor.pressed():
                self.screen.load_image(ImageFile.ANGRY)

                self.speaker.play_file(file=SoundFile.NO)

                self.medium_motor.run_time(
                    speed=-500,
                    time=3000,
                    then=Stop.HOLD,
                    wait=True)


    def main(self, speed: float = 1000):
        Thread(target=self.say_when_touched).start()

        Thread(target=self.spin_fan).start()

        self.keep_driving_by_ir_beacon(speed=speed)
            

if __name__ == '__main__':
    CURIOSITY_ROV3R = CuriosityRov3r()

    CURIOSITY_ROV3R.main()
