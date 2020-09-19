#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop

from time import sleep

from util import cyclic_position_offset


class Dinor3x(EV3Brick):
    """
    Challenges:
    - Can you make DINOR3X remote controlled with the IR-Beacon?
    - Can you attach a colorsensor to DINOR3X, and make it behave differently
        depending on which color is in front of the sensor
        (red = walk fast, white = walk slow, etc.)?
    """

    def __init__(
            self,
            left_motor_port: Port = Port.B, right_motor_port: Port = Port.C,
            jaw_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        self.left_motor = Motor(port=left_motor_port,
                                positive_direction=Direction.CLOCKWISE)
        self.right_motor = Motor(port=right_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.jaw_motor = Motor(port=jaw_motor_port,
                               positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    def calibrate_legs(self):
        self.left_motor.run(speed=100)
        self.right_motor.run(speed=200)

        while self.touch_sensor.pressed():
            pass

        self.left_motor.hold()
        self.right_motor.hold()

        self.left_motor.run(speed=400)

        while not self.touch_sensor.pressed():
            pass

        self.left_motor.hold()

        self.left_motor.run_angle(
            rotation_angle=-0.2 * 360,
            speed=500,
            then=Stop.HOLD,
            wait=True)

        self.right_motor.run(speed=400)

        while not self.touch_sensor.pressed():
            pass

        self.right_motor.hold()

        self.right_motor.run_angle(
            rotation_angle=-0.2 * 360,
            speed=500,
            then=Stop.HOLD,
            wait=True)

    def roar(self):
        self.speaker.play_file(file=SoundFile.T_REX_ROAR)

        self.jaw_motor.run_angle(
            speed=400,
            rotation_angle=-60,
            then=Stop.HOLD,
            wait=True)

        # FIXME: jaw doesn't close
        for i in range(12):
            self.jaw_motor.run_time(
                speed=-400,
                time=0.05 * 1000,
                then=Stop.HOLD,
                wait=True)

            self.jaw_motor.run_time(
                speed=400,
                time=0.05 * 1000,
                then=Stop.HOLD,
                wait=True)

        self.jaw_motor.run(speed=200)

        sleep(0.5)

    def run_away(self):
        self.left_motor.run_angle(
            speed=750,
            rotation_angle=3 * 360,
            then=Stop.BRAKE,
            wait=False)
        self.right_motor.run_angle(
            speed=750,
            rotation_angle=3 * 360,
            then=Stop.BRAKE,
            wait=True)

    def jump(self):
        """
        Dinor3x Mission 02 Challenge: make it jump
        """
        ...

    # MY BLOCKS
    def leg_adjust(
            self,
            cyclic_degrees: float,
            speed: float = 400,
            leg_offset_percent: float = 0,
            mirrored_adjust: bool = False,
            brake: bool = True):
        ...

    def leg_to_pos(
            self,
            speed: float = 400,
            b_position: float = 0,
            c_position: float = 0):
        ...

    def turn(self, speed: float = 400, n_steps: int = 1):
        ...
    
    def walk(self, speed: float = 400):
        ...

    def walk_steps(self, speed: float = 400, n_steps: int = 1):
        ...
