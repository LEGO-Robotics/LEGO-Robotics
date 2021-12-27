#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Button, Direction, Port, Stop

from threading import Thread

# import sys
# sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class Spinn3rBot(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 40
    AXLE_TRACK = 110

    def __init__(
            self,
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            blast_motor_port: Port = Port.A,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity='normal',
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.blast_motor = Motor(port=blast_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.ir_beacon_channel = ir_beacon_channel

    def blast(self, rotations: float = 1):
        if Button.BEACON in \
                    self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.blast_motor.run_angle(
                speed=750,
                rotation_angle=rotations * 360,
                then=Stop.HOLD,
                wait=True)

            self.blast_motor.stop()

            while Button.BEACON in \
                    self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                pass

    def main(self):
        while True:
            self.blast(rotations=3)

            self.drive_once_by_ir_beacon(speed=1000)


if __name__ == '__main__':
    SPINN3R_BOT = Spinn3rBot()

    SPINN3R_BOT.main()
