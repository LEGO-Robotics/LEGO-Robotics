#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4, 
    Sound
)

from PIL import Image

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank


class Catapult(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            catapult_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)
        
        self.catapult_motor = MediumMotor(address=catapult_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=1)

        self.speaker = Sound()


    def scan_colors(self):
        if self.color_sensor.color == ColorSensor.COLOR_YELLOW:
            pass
        
        elif self.color_sensor.color == ColorSensor.COLOR_WHITE:
            self.speaker.play(wav_file='/home/robot/sound/Good.wav').wait()


    def make_noise_when_touched(self):
        if self.touch_sensor.is_pressed:
           self.speaker.play(wav_file='/home/robot/sound/Ouch.wav').wait()


    def throw_by_ir_beacon(self):
        if self.beacon.beacon:
            self.catapult_motor.run_to_rel_pos(
                speed_sp=1000,
                position_sp=-150,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.catapult_motor.wait_while(Motor.STATE_RUNNING)

            self.catapult_motor.run_to_rel_pos(
                speed_sp=1000,
                position_sp=150,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.catapult_motor.wait_while(Motor.STATE_RUNNING)

            while self.beacon.beacon:
                pass


    def main(self):
        self.speaker.play(wav_file='/home/robot/sound/Yes.wav').wait()

        while True:
            self.drive_once_by_ir_beacon(speed=1000)
            
            self.make_noise_when_touched()

            self.throw_by_ir_beacon()

            self.scan_colors()


if __name__ == '__main__':
    CATAPULT = Catapult()

    CATAPULT.main()
