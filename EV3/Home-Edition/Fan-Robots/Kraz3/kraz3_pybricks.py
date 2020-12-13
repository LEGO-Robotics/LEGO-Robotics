#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor, ColorSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.tools import wait

# import sys
# sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class Kraz3(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 24
    AXLE_TRACK = 100

    def __init__(
            self,
            left_motor_port: Port = Port.C, right_motor_port: Port = Port.B,
            wiggle_motor_port: Port = Port.A,
            polarity: str = 'inversed',
            touch_sensor_port: Port = Port.S1,
            color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity=polarity,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.wiggle_motor = Motor(port=wiggle_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    def kungfu_maneouver_if_touched_or_remote_controlled(self):
        """
        Kung-Fu Maneouver voa Touch Sensor and Remote Control of head and arms
        """
        if self.touch_sensor.pressed():
            self.speaker.play_file(file=SoundFile.KUNG_FU)

            self.wiggle_motor.run_angle(
                speed=500,
                rotation_angle=360,
                then=Stop.HOLD,
                wait=True)

        elif Button.BEACON in \
                self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.wiggle_motor.run(speed=111)

        else:
            self.wiggle_motor.stop()

    def kungfu_maneouver_whenever_touched_or_remote_controlled(self):
        while True:
            self.kungfu_maneouver_if_touched_or_remote_controlled()

    def follow_beacon(self):
        """
        Simple "Follow Me" method
        (built by NeXTSTORM and first used in EV3-D4 project)
        """
        distance, angle = self.ir_sensor.beacon(channel=self.ir_beacon_channel)

        if not ((distance is None) or (angle is None)):
            self.drive_base.turn(angle=angle)

            if distance > 50:
                self.drive_base.drive(
                    speed=100,   # drive slowly
                    turn_rate=0)

            elif distance < 20:
                self.drive_base.drive(
                    speed=-100,   # drive slowly
                    turn_rate=0)

    def keep_following_beacon(self):
        while True:
            self.follow_beacon()

    def main(self):
        while True:
            self.drive_once_by_ir_beacon()


if __name__ == '__main__':
    KRAZ3 = Kraz3()

    KRAZ3.main()
