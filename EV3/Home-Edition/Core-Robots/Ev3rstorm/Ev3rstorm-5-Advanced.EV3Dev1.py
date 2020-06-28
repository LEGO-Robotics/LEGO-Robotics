#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4, 
    Leds, Screen, Sound
)

from PIL import Image

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank


class Ev3rstorm(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B,
            right_foot_motor_port: str = OUTPUT_C,
            shooting_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4,
            ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_foot_motor_port,
            right_motor_port=right_foot_motor_port,
            ir_sensor_port=ir_sensor_port,
            ir_beacon_channel=ir_beacon_channel)

        self.shooting_motor = MediumMotor(address=shooting_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.screen = Screen()
        self.speaker = Sound()


    def shoot_when_touched(self):
        if self.touch_sensor.is_pressed:
            if self.color_sensor.ambient_light_intensity < 5:   # 15 not dark enough
                self.speaker.play(wav_file='/home/robot/sound/Up.wav').wait()

                self.shooting_motor.run_to_rel_pos(
                    speed_sp=1000,   # degrees per second
                    position_sp=-3 * 360,   # degrees
                    stop_action=Motor.STOP_ACTION_HOLD)

            else:
                self.speaker.play(wav_file='/home/robot/sound/Down.wav').wait()

                self.shooting_motor.run_to_rel_pos(
                    speed_sp=1000,   # degrees per second
                    position_sp=3 * 360,   # degrees
                    stop_action=Motor.STOP_ACTION_HOLD)

            while self.touch_sensor.is_pressed:
                pass


    def main(self):
        self.screen.image.paste(im=Image.open('/home/robot/image/Target.bmp'))
        self.screen.update()
    
        while True:
            self.drive_by_ir_beacon()
            
            self.shoot_when_touched()


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()
