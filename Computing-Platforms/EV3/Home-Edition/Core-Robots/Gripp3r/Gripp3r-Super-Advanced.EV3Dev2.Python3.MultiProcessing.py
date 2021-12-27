#!/usr/bin/env python3


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4 
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.sound import Sound

from multiprocessing import Process

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


class Gripp3r(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            grip_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            motor_class=LargeMotor,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.grip_motor = MediumMotor(address=grip_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.speaker = Sound()


    def grip_or_release_by_ir_beacon(self, speed: float = 50):
        while True:
            if self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                if self.touch_sensor.is_pressed:
                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Air release.wav',
                        volume=100,
                        play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

                    self.grip_motor.on_for_seconds(
                        speed=speed,
                        seconds=1,
                        brake=True,
                        block=True)

                else:
                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Airbrake.wav',
                        volume=100,
                        play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

                    self.grip_motor.on(
                        speed=-speed,
                        brake=False,
                        block=False)

                    self.touch_sensor.wait_for_pressed()

                    self.grip_motor.off(brake=True)

                while self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                    pass


    def main(self, speed: float = 100):
        self.grip_motor.on_for_seconds(
            speed=-50,
            seconds=1,
            brake=True,
            block=True)
    
        Process(target=self.grip_or_release_by_ir_beacon,
                daemon=True).start()

        self.keep_driving_by_ir_beacon(speed=speed)
    

if __name__ == '__main__':
    GRIPP3R = Gripp3r()

    GRIPP3R.main()
