#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor, ColorSensor
from ev3dev2.sound import Sound

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


class MarsRov3r(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            grip_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.grip_motor = MediumMotor(address=grip_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.speaker = Sound()

        self.is_gripping = False

    def grip_or_release_claw_by_ir_beacon(self):
        if self.ir_sensor.beacon(channel=self.ir_beacon_channel):
            if self.is_gripping:
                self.grip_motor.on_for_seconds(
                    speed=100,
                    seconds=2,
                    brake=True,
                    block=True)

                self.speaker.play_file(
                    wav_file='/home/robot/sound/Air release.wav',
                    volume=100,
                    play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

                self.is_gripping = False

            else:
                self.grip_motor.on_for_seconds(
                    speed=-100,
                    seconds=2,
                    brake=True,
                    block=True)

                self.speaker.play_file(
                    wav_file='/home/robot/sound/Airbrake.wav',
                    volume=100,
                    play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

                self.is_gripping = True

            while self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                pass

    def main(self):
        self.grip_motor.on_for_seconds(
            speed=50,
            seconds=1,
            brake=True,
            block=True)

        while True:
            self.grip_or_release_claw_by_ir_beacon()
            self.drive_once_by_ir_beacon(speed=100)


if __name__ == '__main__':
    MARS_ROV3R = MarsRov3r()

    MARS_ROV3R.main()
