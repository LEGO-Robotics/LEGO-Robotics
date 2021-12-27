#!/usr/bin/env pybricks-micropython


__all__ = ('IRBeaconRemoteControlledTank',)


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Button, Direction, Port

from .ir_beacon_util_pybricks import ir_beacon_measurements_reliable


class IRBeaconRemoteControlledTank:
    def __init__(
            self,
            wheel_diameter: float, axle_track: float,   # both in milimeters
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            polarity: str = 'normal',
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1,
            debug: bool = False):
        self.debug = debug
        if debug:
            self.ev3_brick = EV3Brick()

        motor_positive_direction = \
            Direction.CLOCKWISE \
            if polarity == 'normal' \
            else Direction.COUNTERCLOCKWISE

        self.left_motor = Motor(port=left_motor_port,
                                positive_direction=motor_positive_direction)

        self.right_motor = Motor(port=right_motor_port,
                                 positive_direction=motor_positive_direction)

        self.drive_base = DriveBase(left_motor=self.left_motor,
                                    right_motor=self.right_motor,
                                    wheel_diameter=wheel_diameter,
                                    axle_track=axle_track)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.tank_drive_ir_beacon_channel = ir_beacon_channel

    def drive_once_by_ir_beacon(
            self,
            speed: float = 1000,    # mm/s
            turn_rate: float = 90   # rotational speed deg/s
            ):
        ir_beacon_button_pressed = \
            set(self.ir_sensor.buttons(
                    channel=self.tank_drive_ir_beacon_channel))

        # forward
        if ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
            self.drive_base.drive(
                speed=speed,
                turn_rate=0)

        # backward
        elif ir_beacon_button_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.drive_base.drive(
                speed=-speed,
                turn_rate=0)

        # turn left on the spot
        elif ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_DOWN}:
            self.drive_base.drive(
                speed=0,
                turn_rate=-turn_rate)

        # turn right on the spot
        elif ir_beacon_button_pressed == {Button.RIGHT_UP, Button.LEFT_DOWN}:
            self.drive_base.drive(
                speed=0,
                turn_rate=turn_rate)

        # turn left forward
        elif ir_beacon_button_pressed == {Button.LEFT_UP}:
            self.drive_base.drive(
                speed=speed,
                turn_rate=-turn_rate)

        # turn right forward
        elif ir_beacon_button_pressed == {Button.RIGHT_UP}:
            self.drive_base.drive(
                speed=speed,
                turn_rate=turn_rate)

        # turn left backward
        elif ir_beacon_button_pressed == {Button.LEFT_DOWN}:
            self.drive_base.drive(
                speed=-speed,
                turn_rate=turn_rate)

        # turn right backward
        elif ir_beacon_button_pressed == {Button.RIGHT_DOWN}:
            self.drive_base.drive(
                speed=-speed,
                turn_rate=-turn_rate)

        # otherwise stop
        else:
            self.drive_base.stop()

    # this method must be used in a parallel process/thread
    # in order not to block other operations
    def keep_driving_by_ir_beacon(
            self,
            speed: float = 1000,    # mm/s
            turn_rate: float = 90   # rotational speed deg/s
            ):
        while True:
            self.drive_once_by_ir_beacon(
                speed=speed,
                turn_rate=turn_rate)

    def follow_ir_beacon_once(self, target_distance: float = 10):
        distance, angle = \
            self.ir_sensor.beacon(channel=self.tank_drive_ir_beacon_channel)
        _ir_beacon_measurements_reliable = \
            ir_beacon_measurements_reliable(
                heading_angle=angle,
                distance=distance)

        if self.debug:
            self.ev3_brick.screen.clear()
            self.ev3_brick.screen.print(
                'HA={}, D={}'.format(angle, distance)
                if _ir_beacon_measurements_reliable
                else 'x HA={}, D={}'.format(angle, distance))

        if _ir_beacon_measurements_reliable:
            self.drive_base.turn(angle=angle)

            if distance > target_distance:
                self.drive_base.straight(distance=100)

            else:
                self.drive_base.straight(distance=-100)

    # this method must be used in a parallel process/thread
    # in order not to block other operations
    def keep_following_ir_beacon(self, target_distance: float = 10):
        while True:
            self.follow_ir_beacon_once(target_distance=target_distance)


if __name__ == '__main__':
    IR_BEACON_REMOTE_CONTROLLED_TANK = \
        IRBeaconRemoteControlledTank(
            wheel_diameter=33,
            axle_track=99,
            left_motor_port=Port.B,   # OR: Port.C
            right_motor_port=Port.C,    # OR: Port.B
            polarity='normal',   # OR: 'inversed'
            debug=True)

    # IR_BEACON_REMOTE_CONTROLLED_TANK.keep_driving_by_ir_beacon(speed=1000)
    # OR:
    IR_BEACON_REMOTE_CONTROLLED_TANK.keep_following_ir_beacon()
