#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.sound import Sound

from multiprocessing import Process

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


class CuriosityRov3r(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)
            
        self.medium_motor = MediumMotor(address=medium_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.noise = Sound()

    
    def spin_fan(self, speed: float = 100):
        while True:
            if self.color_sensor.reflected_light_intensity > 20:
                self.medium_motor.on(
                    speed=speed,
                    brake=False,
                    block=False)

            else:
                self.medium_motor.off(brake=True)
                

    def say_when_touched(self):
        while True:
            if self.touch_sensor.is_pressed:
                self.noise.play_file(
                    wav_file='/home/robot/sound/No.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                self.medium_motor.on_for_seconds(
                    speed=-50,
                    seconds=3,
                    brake=True,
                    block=True)


    def main(self, speed: float = 100):
        Process(target=self.say_when_touched).start()

        Process(target=self.spin_fan).start()
        
        self.keep_driving_by_ir_beacon(speed=speed)


if __name__ == '__main__':
    CURIOSITY_ROV3R = CuriosityRov3r()

    CURIOSITY_ROV3R.main()
