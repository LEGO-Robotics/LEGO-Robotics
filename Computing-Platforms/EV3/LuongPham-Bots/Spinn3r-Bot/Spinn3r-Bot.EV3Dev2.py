#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from threading import Thread


# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor
)
from util.drive_util_ev3dev2 import IRBeaconRemoteControlledTank


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

            self.ir_sensor = InfraredSensor(address=ir_sensor_port)

        self.ir_beacon_channel = ir_beacon_channel

    def spin_spinner(self, rotations: float = 1):
        self.blast_motor.on_for_rotations(
            speed=75,
            rotations=rotations,
            brake=True,
            block=True)

    def main(self):
        while True:
            self.blast(rotations=3)

            self.drive_once_by_ir_beacon(speed=1000)


if __name__ == '__main__':
    SPINN3R_BOT = Spinn3rBot()

    SPINN3R_BOT.main()
