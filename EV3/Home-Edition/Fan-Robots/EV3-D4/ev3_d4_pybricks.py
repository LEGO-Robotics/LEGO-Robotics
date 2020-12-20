#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.tools import wait

from pybricks.experimental import run_parallel

from random import choice, randint

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
            touch_sensor_port: Port = Port.S1,
            color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity='inversed',
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.head_motor = Motor(port=head_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_beacon_channel = ir_beacon_channel

        self.state = 0

    def shake_head(self, left_first: bool = True, n_times: int = 1):
        speed_sign = 1 if left_first else -1

        for _ in range(n_times):
            self.head_motor.run_angle(
                speed=speed_sign * 500,
                rotation_angle=100,
                then=Stop.HOLD,
                wait=True)

            self.head_motor.run_angle(
                speed=-speed_sign * 500,
                rotation_angle=200,
                then=Stop.HOLD,
                wait=True)

            self.head_motor.run_angle(
                speed=speed_sign * 500,
                rotation_angle=100,
                then=Stop.HOLD,
                wait=True)

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
            if not (self.ir_sensor.buttons(channel=1) or
                    self.ir_sensor.buttons(channel=2) or
                    self.ir_sensor.buttons(channel=3) or
                    self.ir_sensor.buttons(channel=4)):
                self.drive_base.stop()

                if self.state == 1:
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

            elif Button.BEACON in \
                    self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                self.shake_head(left_first=choice((False, True)))

            else:
                self.drive_once_by_ir_beacon(speed=driving_speed)

    def color_sensor_loop(self):
        """
        This is the Color Sensor Loop that supports 4 different behaviors that
        are triggered RANDOMLY!!!
        """
        while True:
            if self.color_sensor.color == Color.RED:
                random_number = randint(1, 4)

                if random_number == 1:
                    for _ in range(2):
                        self.light.on(color=Color.ORANGE)

                        wait(100)

                        self.light.on(color=Color.GREEN)

                        wait(100)

                        self.light.on(color=Color.RED)

                        wait(100)

                elif random_number == 2:
                    self.speaker.play_file(file=SoundFile.CONFIRM)

                    self.speaker.play_file(file=SoundFile.SMACK)

                    self.shake_head(left_first=True)

                    self.light.on(color=Color.RED)

                elif random_number == 3:
                    self.speaker.play_file(file=SoundFile.OVERPOWER)

                    self.shake_head(
                        left_first=False,
                        n_times=3)

                elif random_number == 4:
                    self.shake_head(
                        left_first=True,
                        n_times=2)

                    self.speaker.play_file(file=SoundFile.READY)

    def touch_sensor_loop(self):
        """
        This is the Touch Sensor Loop that supports 6 different behaviors that
        are triggered RANDOMLY!!!
        """
        ...

    def main(self):
        run_parallel(
            self.main_switch_loop,
            self.color_sensor_loop)


if __name__ == '__main__':
    ev3_d4 = EV3D4()

    ev3_d4.main()
