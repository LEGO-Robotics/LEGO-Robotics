#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.robotics import DriveBase

from threading import Thread

import os
import sys
sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class Gripp3r(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 26
    AXLE_TRACK = 115

    def __init__(
            self,
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            grip_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)
            
        self.drive_base.settings(
            straight_speed=750,   # milimeters per second
            straight_acceleration=750,
            turn_rate=90,   # degrees per second
            turn_acceleration=90)
                
        self.grip_motor = Motor(port=grip_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel


    def grip_or_release_by_ir_beacon(self, speed: float = 500):
        while True:
            if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                if self.touch_sensor.pressed():
                    self.speaker.play_file(file=SoundFile.AIR_RELEASE)

                    self.grip_motor.run_time(
                        speed=speed,
                        time=1000,
                        then=Stop.BRAKE,
                        wait=True)

                else:
                    self.speaker.play_file(file=SoundFile.AIRBRAKE)

                    self.grip_motor.run(speed=-speed)

                    while not self.touch_sensor.pressed():
                        pass

                    self.grip_motor.stop()

                while Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                    pass


    def main(self, speed: float = 1000):
        self.grip_motor.run_time(
            speed=-500,
            time=1000,
            then=Stop.BRAKE,
            wait=True)

        Thread(target=self.grip_or_release_by_ir_beacon).start()
            
        self.keep_driving_by_ir_beacon(speed=speed)    


if __name__ == '__main__':
    GRIPP3R = Gripp3r()

    GRIPP3R.main()
