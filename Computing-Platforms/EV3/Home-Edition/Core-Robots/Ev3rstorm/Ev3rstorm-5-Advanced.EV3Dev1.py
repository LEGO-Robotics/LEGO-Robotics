#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, INPUT_1, INPUT_3, INPUT_4,
    Screen, Sound
)

from PIL import Image

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank


class Ev3rstorm(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B, right_foot_motor_port: str = OUTPUT_C,
            bazooka_blast_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_foot_motor_port, right_motor_port=right_foot_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.bazooka_blast_motor = MediumMotor(address=bazooka_blast_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.screen = Screen()
        self.speaker = Sound()


    def blast_bazooka_if_touched(self):
        if self.touch_sensor.is_pressed:
            if self.color_sensor.ambient_light_intensity < 5:   # 15 not dark enough
                self.speaker.play(wav_file='/home/robot/sound/Up.wav').wait()

                self.bazooka_blast_motor.run_to_rel_pos(
                    speed_sp=1000,   # degrees per second
                    position_sp=-3 * 360,   # degrees
                    stop_action=Motor.STOP_ACTION_HOLD)

            else:
                self.speaker.play(wav_file='/home/robot/sound/Down.wav').wait()

                self.bazooka_blast_motor.run_to_rel_pos(
                    speed_sp=1000,   # degrees per second
                    position_sp=3 * 360,   # degrees
                    stop_action=Motor.STOP_ACTION_HOLD)

            while self.touch_sensor.is_pressed:
                pass


    def main(self,
             driving_speed: float = 1000   # degrees per second
            ):
        self.screen.image.paste(im=Image.open('/home/robot/image/Target.bmp'))
        self.screen.update()
    
        while True:
            self.drive_once_by_ir_beacon(speed=driving_speed)
            
            self.blast_bazooka_if_touched()


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()
