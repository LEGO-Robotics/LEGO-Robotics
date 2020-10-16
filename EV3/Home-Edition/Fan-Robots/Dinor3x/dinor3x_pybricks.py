#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop

from time import sleep

from dinor3x_util import cyclic_position_offset


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

    def position_legs(
            self,
            speed: float = 1000,
            left_position: float = 0,
            right_position: float = 0):
        self.left_motor.hold()
        self.right_motor.hold()

        self.left_motor.run_angle(
            speed=speed,
            rotation_angle=left_position - self.left_motor.angle() % 360,
            then=Stop.HOLD,
            wait=True)

        self.right_motor.run_angle(
            speed=speed,
            rotation_angle=right_position - self.right_motor.angle() % 360,
            then=Stop.HOLD,
            wait=True)

    def adjust_legs(self, speed: float = 1000, brake: bool = True):
        self.left_motor.hold()
        self.right_motor.hold()

        diff = (self.left_motor.angle() % 360) \
            - (self.right_motor.angle() % 360)

        if diff > 180:
            diff -= 360
        elif diff < -180:
            diff += 360

        if speed >= 0:
            if diff >= 0:
                self.left_motor.run_angle(
                    speed=-speed,
                    rotation_angle=diff,
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

            else:
                self.right_motor.run_angle(
                    speed=-speed,
                    rotation_angle=abs(diff),
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

        else:
            if diff >= 0:
                self.right_motor.run_angle(
                    speed=-speed,
                    rotation_angle=diff,
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

            else:
                self.left_motor.run_angle(
                    speed=-speed,
                    rotation_angle=abs(diff),
                    then=Stop.HOLD if brake else Stop.COAST,
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

    def close_mouth(self):
        self.jaw_motor.run(speed=200)
        sleep(1)
        self.jaw_motor.stop()

    def walk_until_blocked(self):
        self.left_motor.run(speed=-400)
        self.right_motor.run(speed=-400)

        while self.ir_sensor.distance() >= 25:
            pass

        self.left_motor.stop()
        self.right_motor.stop()

    def run_away(self):
        self.left_motor.run_angle(
            speed=750,
            rotation_angle=3 * 360,
            then=Stop.HOLD,
            wait=False)
        self.right_motor.run_angle(
            speed=750,
            rotation_angle=3 * 360,
            then=Stop.HOLD,
            wait=True)

    def jump(self):
        """
        Dinor3x Mission 02 Challenge: make it jump
        """
        ...

    # TRANSLATED FROM EV3-G MY BLOCKS
    # -------------------------------

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

        self.left_motor.reset_angle(angle=0)
        self.right_motor.reset_angle(angle=0)

    def leg_to_pos(
            self,
            speed: float = 1000,
            left_position: float = 0,
            right_position: float = 0):
        self.left_motor.hold()
        self.right_motor.hold()

        self.left_motor.run_angle(
            speed=speed,
            rotation_angle=left_position -
                           cyclic_position_offset(
                                rotation_sensor=self.left_motor.angle(),
                                cyclic_degrees=360),
            then=Stop.HOLD,
            wait=True)

        self.right_motor.run_angle(
            speed=speed,
            rotation_angle=right_position -
                           cyclic_position_offset(
                                rotation_sensor=self.right_motor.angle(),
                                cyclic_degrees=360),
            then=Stop.HOLD,
            wait=True)

    def leg_adjust(
            self,
            cyclic_degrees: float = 360,
            speed: float = 1000,
            leg_offset_percent: float = 0,
            mirrored_adjust: bool = False,
            brake: bool = True):
        self.left_motor.hold()
        self.right_motor.hold()

        diff = cyclic_position_offset(
                rotation_sensor=self.left_motor.angle(),
                cyclic_degrees=cyclic_degrees) \
            - cyclic_position_offset(
                rotation_sensor=self.right_motor.angle(),
                cyclic_degrees=cyclic_degrees)

        if diff > (cyclic_degrees / 2):
            diff -= cyclic_degrees

        if diff < -180:
            diff += cyclic_degrees

        if speed >= 0:
            if diff >= 0:
                self.left_motor.run_angle(
                    speed=-speed,
                    rotation_angle=diff,
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

            else:
                self.right_motor.run_angle(
                    speed=-speed,
                    rotation_angle=abs(diff),
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

        else:
            if diff >= 0:
                self.right_motor.run_angle(
                    speed=-speed,
                    rotation_angle=diff,
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

            else:
                self.left_motor.run_angle(
                    speed=-speed,
                    rotation_angle=abs(diff),
                    then=Stop.HOLD if brake else Stop.COAST,
                    wait=True)

            # TODO: print to screen

    def walk(self, speed: float = 1000):
        # to make legs ready to walk properly
        self.calibrate_legs()

        # self.adjust_legs(
        #     speed=speed,
        #     brake=False)
        # self.leg_adjust(
        #     cyclic_degrees=360,
        #     speed=speed,
        #     leg_offset_percent=0,
        #     mirrored_adjust=False,
        #     brake=False)

        self.left_motor.run(speed=-speed)
        self.right_motor.run(speed=-speed)

    def walk_n_steps(self, speed: float = 1000, n_steps: int = 1):
        ...

    def turn(self, speed: float = 1000):
        # to make legs ready to walk properly
        self.calibrate_legs()

        # self.adjust_legs(
        #     speed=speed,
        #     brake=False)
        # self.leg_adjust(
        #     cyclic_degrees=360,
        #     speed=speed,
        #     leg_offset_percent=0,
        #     mirrored_adjust=False,
        #     brake=False)

        if speed >= 0:
            self.left_motor.run_angle(
                rotation_angle=180,
                speed=speed,
                then=Stop.HOLD,
                wait=True)

        else:
            self.right_motor.run_angle(
                rotation_angle=180,
                speed=-speed,
                then=Stop.HOLD,
                wait=True)

        self.left_motor.run(speed=speed)
        self.right_motor.run(speed=-speed)

    def turn_n_steps(self, speed: float = 1000, n_steps: int = 1):
        ...
