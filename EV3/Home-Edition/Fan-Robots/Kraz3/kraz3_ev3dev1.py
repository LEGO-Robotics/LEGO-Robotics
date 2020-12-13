#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4,
    Sound, Screen
)

from time import sleep

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor,
    TouchSensor as FastTouchSensor,
    ColorSensor as FastColorSensor
)
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank


class Kraz3(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_C, right_motor_port: str = OUTPUT_B,
            wiggle_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel,
            polarity=Motor.POLARITY_INVERSED,
            fast=fast)

        if fast:
            self.wiggle_motor = FastMediumMotor(address=wiggle_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

            self.color_sensor = FastColorSensor(address=color_sensor_port)

        else:
            self.wiggle_motor = MediumMotor(address=wiggle_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

            self.color_sensor = ColorSensor(address=color_sensor_port)

        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=ir_beacon_channel)

        self.speaker = Sound()
        self.screen = Screen()

    def kungfu_maneouver_if_touched_or_remote_controlled(self):
        """
        Kung-Fu Maneouver voa Touch Sensor and Remote Control of head and arms
        """
        if self.touch_sensor.is_pressed:
            self.speaker.play(wav_file='/home/robot/sound/Kung fu.wav')

            self.wiggle_motor.run_to_rel_pos(
                speed_sp=500,   # degrees per second
                position_sp=360,   # degrees
                stop_action=Motor.STOP_ACTION_HOLD)

        elif self.beacon.beacon:
            self.wiggle_motor.run_forever(speed_sp=111)

        else:
            self.wiggle_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

    def kungfu_maneouver_whenever_touched_or_remote_controlled(self):
        while True:
            self.kungfu_maneouver_if_touched_or_remote_controlled()

    def follow_beacon(self):
        """
        Simple "Follow Me" method
        (built by NeXTSTORM and first used in EV3-D4 project)
        """
        ...

    def keep_following_beacon(self):
        while True:
            self.follow_beacon()

    def main(self):
        while True:
            self.drive_once_by_ir_beacon()


if __name__ == '__main__':
    KRAZ3 = Kraz3()

    KRAZ3.main()
