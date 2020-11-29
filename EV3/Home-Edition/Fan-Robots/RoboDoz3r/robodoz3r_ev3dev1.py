#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, RemoteControl, INPUT_1, INPUT_4,
    Screen, Sound
)

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor,
    TouchSensor as FastTouchSensor
)

from time import sleep


class RoboDoz3r(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_C, right_motor_port: str = OUTPUT_B,
            shovel_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4,
            tank_drive_ir_beacon_channel: int = 1,
            shovel_control_ir_beacon_channel: int = 4,
            fast=False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity=Motor.POLARITY_INVERSED,
            ir_sensor_port=ir_sensor_port,
            ir_beacon_channel=tank_drive_ir_beacon_channel,
            fast=fast)

        if fast:
            self.shovel_motor = FastMediumMotor(address=shovel_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

        else:
            self.shovel_motor = MediumMotor(address=shovel_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.shovel_control_remote_control = \
            RemoteControl(
                sensor=self.ir_sensor,
                channel=shovel_control_ir_beacon_channel)

        self.screen = Screen()
        self.speaker = Sound()

    def main(self,
             driving_speed: float = 1000   # deg/s
             ):

        while True:
            # Determine which motor to drive
            # from the value sent by the IR remote.
            # Use a large switch block to convert each code from the remote
            # into a motor movement.
            # Use the IR sensor in Remote mode to accept commands
            # from the IR beacon.
            # Each key press combination on the IR beacon corresponds to
            # a numeric value from 0 to 9.
            # Each value is handled in a case in the switch statement.
            self.drive_once_by_ir_beacon(speed=driving_speed)


if __name__ == '__main__':
    ROBODOZ3R = RoboDoz3r()

    ROBODOZ3R.main()
