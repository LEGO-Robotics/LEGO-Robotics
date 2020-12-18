#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.tools import wait

from random import randint

# import sys
# sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class EV3D4(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 20
    AXLE_TRACK = 110

    def __init__(
            self,
            left_motor_port: Port = Port.C, right_motor_port: Port = Port.B,
            head_motor_port: Port = Port.A,
            polarity: str = 'inversed',
            touch_sensor_port: Port = Port.S1,
            color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity=polarity,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.head_motor = Motor(port=head_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_beacon_channel = ir_beacon_channel

        self.state = 0

    def main_switch_loop(self, driving_speed: float = 750):
        """
        This is the Main Switch Loop that allows you to control EV3-D4 using
        the Remote and at the same time it helps EV3-D4 to utilise its B+C
        motors when these are not used when driving EV3-D4 with Remote Control.

        The logic is simple:
        If buttons of Remote Control are pressed then EV3-D4 goes (B+C motors)
        wherever you command it, else it moves according to the behavioural
        state that is changed upon interacting with its Touch Sensor, else stop
        B+C motors.
        """
        while True:
            if Button.BEACON in \
                    self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                self.drive_base.stop()

                if self.state == 0:
                    self.drive_base.stop()

                elif self.state == 1:
                    self.drive_base.turn(
                        speed=driving_speed,
                        angle=-90)

                    self.drive_base.turn(
                        speed=driving_speed,
                        angle=90)

                elif self.state == 2:
                    self.drive_base.straight(distance=-50)

                    self.drive_base.straight(distance=50)

                elif self.state == 3:
                    self.drive_base.straight(distance=50)

                    self.drive_base.straight(distance=-50)

                self.state = 0

            else:
                self.drive_once_by_ir_beacon()

    def color_sensor_loop(self):
        """
        This is the Color Sensor Loop that supports 4 different behaviors that
        are triggered RANDOMLY!!!
        """
        ...

    def touch_sensor_loop(self):
        """
        This is the Touch Sensor Loop that supports 6 different behaviors that
        are triggered RANDOMLY!!!
        """
        ...

    def main(self, driving_speed: float = 750):
        self.main_switch_loop(driving_speed=driving_speed)


if __name__ == '__main__':
    ev3_d4 = EV3D4()

    ev3_d4.main()
