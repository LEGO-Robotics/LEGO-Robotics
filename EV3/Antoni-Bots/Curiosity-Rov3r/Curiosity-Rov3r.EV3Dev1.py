#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4,
    Sound, Screen
)

from PIL import Image

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank


class Curiosity_Rov3r(IRBeaconRemoteControlledTank):
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
        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=ir_beacon_channel)

        self.dis = Screen()

        self.noise = Sound()

    
    def spin_fan(self, speed: 1000):
        if self.color_sensor.reflected_light_intensity > 20:
            self.medium_motor.run_forever(speed_sp=speed)

        elif self.color_sensor.reflected_light_intensity < 20:
            self.medium_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

            
    def say_when_touched(self):
        if self.touch_sensor.is_pressed:
            self.dis.image.paste(im=Image.open('/home/robot/image/Angry.bmp'))
            self.dis.update()

            self.noise.play(wav_file='/home/robot/sound/No.wav').wait()

            self.medium_motor.run_timed(
                speed_sp=-500,
                time_sp=3000,
                stop_action=Motor.STOP_ACTION_BRAKE)
            self.medium_motor.wait_while(Motor.STATE_RUNNING)


    def main(self, speed: float = 1000):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

            self.say_when_touched()

            self.spin_fan(speed=speed)
            

if __name__ == '__main__':
    CURIOSITY_ROV3R = Curiosity_Rov3r()

    CURIOSITY_ROV3R.main()


