#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4,
    Screen, Sound
)

from multiprocessing import Process
from PIL import Image

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank


class Sweep3r(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            right_motor_port: str = OUTPUT_C, left_motor_port: str = OUTPUT_B,
            medium_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.medium_motor = MediumMotor(address=medium_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.screen = Screen()
        self.speaker = Sound()

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.remote_control = RemoteControl(sensor=self.ir_sensor,
                                            channel=ir_beacon_channel)

    
    def drill(self):
        while True:
            if self.remote_control.beacon:
                self.medium_motor.run_timed(
                    speed_sp=1000,   # deg/s
                    time_sp=0.3 * 1000,   # ms 
                    stop_action=Motor.STOP_ACTION_HOLD)
                self.medium_motor.wait_while(Motor.STATE_RUNNING)


    def move_when_touched(self):
        while True:    
            if self.touch_sensor.is_pressed:
                self.right_motor.run_timed(
                    time_sp=1000,
                    speed_sp=1000,
                    stop_action=Motor.STOP_ACTION_BRAKE)

                self.right_motor.wait_while(Motor.STATE_RUNNING)


    def move_when_see_smothing(self):
        while True:
            if self.color_sensor.reflected_light_intensity > 30:
                self.left_motor.run_timed(
                    time_sp=1000,
                    speed_sp=1000,
                    stop_action=Motor.STOP_ACTION_BRAKE)

                self.left_motor.wait_while(Motor.STATE_RUNNING)
       
                     
    def main(self,
             speed: float = 1000   # degrees per second
            ):
        self.screen.image.paste(im=Image.open('/home/robot/image/Pinch middle.bmp'))
        self.screen.update()
    
        Process(target=self.move_when_touched,
                daemon=True).start() 

        Process(target=self.move_when_see_smothing,
                daemon=True).start()

        Process(target=self.drill,
                daemon=True).start()

        self.keep_driving_by_ir_beacon(speed=speed)

        # FIXME: multiple Processes control Large Motors conflictingly


if __name__ == '__main__':
    SWEEP3R = Sweep3r()

    SWEEP3R.main()
