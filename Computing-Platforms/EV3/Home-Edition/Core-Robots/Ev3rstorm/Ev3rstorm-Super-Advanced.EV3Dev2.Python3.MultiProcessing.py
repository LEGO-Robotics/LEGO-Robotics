#!/usr/bin/env python3
# (Display not yet working in MicroPython as of 2020)


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.display import Display
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

from multiprocessing import Process
from random import randint

import os
import sys
sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


class Ev3rstorm(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B, right_foot_motor_port: str = OUTPUT_C,
            bazooka_blast_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_foot_motor_port, right_motor_port=right_foot_motor_port, motor_class=LargeMotor,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.bazooka_blast_motor = MediumMotor(address=bazooka_blast_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.leds = Leds()
        self.speaker = Sound()
        self.screen = Display()

    
    def dance_whenever_ir_beacon_pressed(self):
        while True:
            while self.ir_sensor.beacon(channel=self.tank_drive_ir_beacon_channel):
                self.tank_driver.on_for_seconds(
                    left_speed=randint(-100, 100),
                    right_speed=randint(-100, 100),
                    seconds=1,
                    brake=False,
                    block=True)


    def keep_detecting_objects_by_ir_sensor(self):
        while True:
            if self.ir_sensor.proximity < 25: 
                self.leds.animate_police_lights(
                    color1=Leds.ORANGE,
                    color2=Leds.RED,
                    group1=Leds.LEFT,
                    group2=Leds.RIGHT,
                    sleeptime=0.5,
                    duration=5,
                    block=False)
                
                self.speaker.play_file(
                    wav_file='/home/robot/sound/Object.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                self.speaker.play_file(                                  
                    wav_file='/home/robot/sound/Detected.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                self.speaker.play_file(
                    wav_file='/home/robot/sound/Error alarm.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            else:
                self.leds.all_off()


    def blast_bazooka_whenever_touched(self):
        while True:
            if self.touch_sensor.is_pressed:
                if self.color_sensor.ambient_light_intensity < 5:   # 15 not dark enough
                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Up.wav',
                        volume=100,
                        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                    self.bazooka_blast_motor.on_for_rotations(
                        speed=100,
                        rotations=-3,
                        brake=True,
                        block=True)

                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Laughing 1.wav',
                        volume=100,
                        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                else:
                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Down.wav',
                        volume=100,
                        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                    self.bazooka_blast_motor.on_for_rotations(
                        speed=100,
                        rotations=3,
                        brake=True,
                        block=True)

                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Laughing 2.wav',
                        volume=100,
                        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                self.touch_sensor.wait_for_released()

    
    def main(self, driving_speed: float = 100):
        self.screen.image_filename(
            filename='/home/robot/image/Target.bmp',
            clear_screen=True)
        self.screen.update()

        Process(target=self.dance_whenever_ir_beacon_pressed,
                daemon=True).start()

        # DON'T use IR Sensor in 2 different modes in the same program / loop
        # - https://github.com/pybricks/support/issues/62
        # - https://github.com/ev3dev/ev3dev/issues/1401
        # Process(target=self.keep_detecting_objects_by_ir_sensor,
        #         daemon=True).start()

        Process(target=self.blast_bazooka_whenever_touched,
                daemon=True).start()

        self.keep_driving_by_ir_beacon(speed=driving_speed)


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()
