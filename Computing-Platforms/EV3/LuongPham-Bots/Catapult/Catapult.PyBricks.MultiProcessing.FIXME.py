#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop

from multiprocessing import Process

import os
import sys
sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class Catapult(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 23
    AXLE_TRACK = 65

    def __init__(
            self,
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            catapult_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1, color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)
        
        self.catapult_motor = Motor(port=catapult_motor_port,
                                    positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)
        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    
    def scan_colors(self):
        while True:
            if self.color_sensor.color() == Color.YELLOW:
                pass

            elif self.color_sensor.color() == Color.WHITE:
                self.speaker.play_file(file=SoundFile.GOOD)


    def make_noise_when_touched(self):
        while True:
            if self.touch_sensor.pressed():
                self.speaker.play_file(file=SoundFile.OUCH)


    def throw_by_ir_beacon(self):
        while True:
            if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                self.catapult_motor.run_angle(
                    speed=3500,
                    rotation_angle=-150,
                    then=Stop.HOLD,
                    wait=True)

                self.catapult_motor.run_angle(
                    speed=3500,
                    rotation_angle=150,
                    then=Stop.HOLD,
                    wait=True)

                while Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                    pass


    def main(self):
        self.speaker.play_file(file=SoundFile.YES)
             
        Process(target=self.make_noise_when_touched).start()

        Process(target=self.throw_by_ir_beacon).start()

        Process(target=self.scan_colors).start()
        
        self.keep_driving_by_ir_beacon(speed=1000)

        # FIXME: OSError: [Errno 5] EIO: 
        # Unexpected hardware input/output error with a motor or sensor:
        # --> Try unplugging the sensor or motor and plug it back in again.
        # --> To see which sensor or motor is causing the problem,
        #     check the line in your script that matches
        #     the line number given in the 'Traceback' above.
        # --> Try rebooting the hub/brick if the problem persists.


if __name__ == '__main__':
    CATAPULT = Catapult()

    CATAPULT.main()
