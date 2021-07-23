#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    RemoteControl, INPUT_4
)

from threading import Thread


# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor
)
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank


class Spinn3rBot(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            blast_motor_port: str = OUTPUT_A,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast: bool = False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel,
            polarity=Motor.POLARITY_NORMAL,
            fast=fast)

        if fast:
            self.blast_motor = FastMediumMotor(address=blast_motor_port)

        else:
            self.blast_motor = MediumMotor(address=blast_motor_port)

        self.remote_control = RemoteControl(sensor=self.ir_sensor,
                                            channel=ir_beacon_channel)

    def spin_spinner(self, rotations: float = 1):
        ...

    def main(self):
        while True:
            self.blast(rotations=3)

            self.drive_once_by_ir_beacon(speed=1000)


if __name__ == '__main__':
    SPINN3R_BOT = Spinn3rBot()

    SPINN3R_BOT.main()
