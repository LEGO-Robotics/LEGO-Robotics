#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port
from pybricks.tools import wait

from time import time

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class RoboDoz3r(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 24   # milimeters
    AXLE_TRACK = 100      # milimeters

    def __init__(
            self,
            left_motor_port: Port = Port.C, right_motor_port: Port = Port.B,
            shovel_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4,
            tank_drive_ir_beacon_channel: int = 1,
            shovel_control_ir_beacon_channel: int = 4):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity='inversed',
            ir_sensor_port=ir_sensor_port,
            ir_beacon_channel=tank_drive_ir_beacon_channel)

        self.shovel_motor = Motor(port=shovel_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.shovel_control_ir_beacon_channel = \
            shovel_control_ir_beacon_channel

    def drive_by_ir_beacon_until_touched(
            self,
            speed: float = 1000   # mm/s
            ):
        while not self.touch_sensor.pressed():
            self.drive_once_by_ir_beacon(speed=speed)

    def raise_or_lower_shovel_once_by_ir_beacon(self):
        """
        If the channel 4 is selected on the IR remote
        then you can control raising and lowering the shovel on the RoboDoz3r.

        Use the IR sensor in Remote mode.
        Each button press on the IR beacon is converted into a numeric value
        which is checked using the switch block.
        """
        ir_beacon_button_pressed = \
            set(self.ir_sensor.buttons(
                    channel=self.shovel_control_ir_beacon_channel))

        # raise the shovel
        if ir_beacon_button_pressed.intersection(
                {Button.LEFT_UP, Button.RIGHT_UP}):
            self.shovel_motor.run(speed=100)

        # lower the shovel
        elif ir_beacon_button_pressed.intersection(
                {Button.LEFT_DOWN, Button.RIGHT_DOWN}):
            self.shovel_motor.run(speed=-100)

        else:
            self.shovel_motor.hold()

    def raise_or_lower_shovel_by_ir_beacon_until_touched(self):
        while not self.touch_sensor.pressed():
            self.raise_or_lower_shovel_once_by_ir_beacon()

    def main(self,
             driving_speed: float = 1000   # mm/s
             ):
        """
        This is the main control program for the RoboDoz3r.
        It uses two methods to get commands from the IR remote
        and to raise or lower the shovel.
        """
        self.screen.print('ROBODOZ3R')

        self.speaker.play_file(SoundFile.MOTOR_START)

        # Let the engine sound idle for 2 seconds
        motor_idle_start_time = time()
        while time() - motor_idle_start_time <= 2:
            self.speaker.play_file(SoundFile.MOTOR_IDLE)

        while True:
            # Manual mode where the movement of the RoboDoz3r is controlled
            # by the IR remote
            while not self.touch_sensor.pressed():
                self.raise_or_lower_shovel_once_by_ir_beacon()

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

            self.speaker.play_file(SoundFile.AIRBRAKE)

            # In autonomous mode the RoboDoz3r uses the IR sensor
            # in proximity mode to detect nearby obstacles in its path
            while not self.touch_sensor.pressed():
                if self.ir_sensor.distance() < 50:
                    self.drive_base.stop()

                    wait(1000)

                    self.drive_base.straight(distance=-100)

                    self.drive_base.turn(angle=90)

                else:
                    self.drive_base.drive(
                        speed=500,
                        turn_rate=0)

            self.speaker.play_file(SoundFile.AIRBRAKE)


if __name__ == '__main__':
    ROBODOZ3R = RoboDoz3r()

    ROBODOZ3R.main()
