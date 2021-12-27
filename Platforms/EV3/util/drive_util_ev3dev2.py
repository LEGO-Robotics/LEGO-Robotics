#!/usr/bin/env micropython


__all__ = ('IRBeaconRemoteControlledTank',)


from ev3dev2.motor import \
    Motor, LargeMotor, MoveSteering, MoveTank, \
    OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.console import Console

from .ev3dev_fast.ev3fast import \
    LargeMotor as FastLargeMotor, \
    MoveTank as FastMoveTank, MoveSteering as FastMoveSteering

from .ir_beacon_util_ev3dev2 import ir_beacon_measurements_reliable


class IRBeaconRemoteControlledTank:
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            motor_class=LargeMotor, polarity: str = Motor.POLARITY_NORMAL,
            ir_sensor_port: str = INPUT_4,
            # sites.google.com/site/ev3devpython/learn_ev3_python/using-sensors
            ir_beacon_channel: int = 1,
            fast: bool = False,
            debug: bool = False):
        self.debug = debug
        if debug:
            self.console = Console()

        if fast:
            self.left_motor = FastLargeMotor(address=left_motor_port)
            self.right_motor = FastLargeMotor(address=right_motor_port)

            self.tank_driver = \
                FastMoveTank(
                    left_motor_port=left_motor_port,
                    right_motor_port=right_motor_port,
                    motor_class=motor_class)

            self.steer_driver = \
                FastMoveSteering(
                    left_motor_port=left_motor_port,
                    right_motor_port=right_motor_port,
                    motor_class=motor_class)

        else:
            self.left_motor = LargeMotor(address=left_motor_port)
            self.right_motor = LargeMotor(address=right_motor_port)

            self.tank_driver = \
                MoveTank(
                    left_motor_port=left_motor_port,
                    right_motor_port=right_motor_port,
                    motor_class=motor_class)

            self.steer_driver = \
                MoveSteering(
                    left_motor_port=left_motor_port,
                    right_motor_port=right_motor_port,
                    motor_class=motor_class)

        self.left_motor.polarity = self.right_motor.polarity = \
            self.tank_driver.left_motor.polarity = \
            self.tank_driver.right_motor.polarity = \
            self.steer_driver.left_motor.polarity = \
            self.steer_driver.right_motor.polarity = polarity

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.tank_drive_ir_beacon_channel = ir_beacon_channel

    def drive_once_by_ir_beacon(self, speed: float = 100):
        # forward
        if self.ir_sensor.top_left(
                    channel=self.tank_drive_ir_beacon_channel) and \
                self.ir_sensor.top_right(
                    channel=self.tank_drive_ir_beacon_channel):
            self.tank_driver.on(
                left_speed=speed,
                right_speed=speed)

        # backward
        elif self.ir_sensor.bottom_left(
                    channel=self.tank_drive_ir_beacon_channel) and \
                self.ir_sensor.bottom_right(
                    channel=self.tank_drive_ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=-speed)

        # turn left on the spot
        elif self.ir_sensor.top_left(
                    channel=self.tank_drive_ir_beacon_channel) and \
                self.ir_sensor.bottom_right(
                    channel=self.tank_drive_ir_beacon_channel):
            self.steer_driver.on(
                steering=-100,
                speed=speed)

        # turn right on the spot
        elif self.ir_sensor.top_right(
                    channel=self.tank_drive_ir_beacon_channel) and \
                self.ir_sensor.bottom_left(
                    channel=self.tank_drive_ir_beacon_channel):
            self.steer_driver.on(
                steering=100,
                speed=speed)

        # turn left forward
        elif self.ir_sensor.top_left(
                    channel=self.tank_drive_ir_beacon_channel):
            self.steer_driver.on(
                steering=-50,
                speed=speed)

        # turn right forward
        elif self.ir_sensor.top_right(
                    channel=self.tank_drive_ir_beacon_channel):
            self.steer_driver.on(
                steering=50,
                speed=speed)

        # turn left backward
        elif self.ir_sensor.bottom_left(
                    channel=self.tank_drive_ir_beacon_channel):
            self.tank_driver.on(
                left_speed=0,
                right_speed=-speed)

        # turn right backward
        elif self.ir_sensor.bottom_right(
                    channel=self.tank_drive_ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=0)

        # otherwise stop
        else:
            self.tank_driver.off(brake=False)

    # this method must be used in a parallel process/thread
    # in order not to block other operations
    def keep_driving_by_ir_beacon(self, speed: float = 100):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

    def follow_ir_beacon_once(
            self,
            speed: float = 100,
            target_distance: float = 10):
        heading, distance = self.ir_sensor.heading_and_distance(channel=1)
        _ir_beacon_measurements_reliable = \
            ir_beacon_measurements_reliable(
                heading_angle=heading,
                distance=distance)

        if self.debug:
            self.console.text_at(
                text='HA={}, D={}'.format(heading, distance)
                     if _ir_beacon_measurements_reliable
                     else 'x HA={}, D={}'.format(heading, distance),
                column=1, row=1,
                reset_console=True,
                inverse=False,
                alignment='L')

        if _ir_beacon_measurements_reliable:
            if heading < -3:
                self.steer_driver.on_for_seconds(
                    steering=-100,
                    speed=speed,
                    seconds=1,
                    brake=False,
                    block=True)

            elif heading > 3:
                self.steer_driver.on_for_seconds(
                    steering=100,
                    speed=speed,
                    seconds=1,
                    brake=False,
                    block=True)

            if distance > target_distance:
                self.steer_driver.on_for_seconds(
                    steering=0,
                    speed=speed,
                    seconds=1,
                    brake=False,
                    block=True)

            else:
                self.steer_driver.on_for_seconds(
                    steering=0,
                    speed=-speed,
                    seconds=1,
                    brake=False,
                    block=True)

    # this method must be used in a parallel process/thread
    # in order not to block other operations
    def keep_following_ir_beacon(
            self,
            speed: float = 100,
            target_distance: float = 10):
        while True:
            self.follow_ir_beacon_once(
                speed=speed,
                target_distance=target_distance)


if __name__ == '__main__':
    IR_BEACON_REMOTE_CONTROLLED_TANK = IRBeaconRemoteControlledTank()

    IR_BEACON_REMOTE_CONTROLLED_TANK.keep_driving_by_ir_beacon()
