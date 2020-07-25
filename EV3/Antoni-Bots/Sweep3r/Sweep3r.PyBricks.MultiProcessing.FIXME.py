#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile
from pybricks.parameters import Button, Port, Stop

from multiprocessing import Process

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


    def drill(self):
        while True:
            if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                self.medium_motor.run_angle(
                    speed=1000,
                    rotation_angle=2 * 360,
                    then=Stop.HOLD,
                    wait=True)


    def move_when_touched(self):
        while True:    
            if self.touch_sensor.pressed():
                self.drive_base.turn(angle=100)


    def move_when_see_smothing(self):
        while True:
            if self.color_sensor.reflection() > 30:
                self.drive_base.turn(angle=-100)

        
    def main(self, speed: float = 1000):
        self.screen.load_image(ImageFile.PINCHED_MIDDLE)

        Process(target=self.move_when_touched).start()

        Process(target=self.move_when_see_smothing).start()

        Process(target=self.drill).start()

        self.keep_driving_by_ir_beacon(speed=speed)

        # FIXME: OSError: [Errno 5] EIO: 
        # Unexpected hardware input/output error with a motor or sensor:
        # --> Try unplugging the sensor or motor and plug it back in again.
        # --> To see which sensor or motor is causing the problem,
        #     check the line in your script that matches
        #     the line number given in the 'Traceback' above.
        # --> Try rebooting the hub/brick if the problem persists.


if __name__ == '__main__':
    SWEEP3R = Sweep3r()

    SWEEP3R.main()
