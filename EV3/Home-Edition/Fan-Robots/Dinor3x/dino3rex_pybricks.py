#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.robotics import DriveBase


from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class Dinor3x(EV3Brick):
    def __init__(
            self,
            left_motor_port: str = Port.B, right_motor_port: str = Port.C,
            jaw_motor_port: str = Port.A,
            touch_sensor_port: str = Port.S1,
            ir_sensor_port: str = Port.S4, ir_beacon_channel: int = 1):
        self.left_motor = Motor(port=left_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.right_motor = Motor(port=left_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.jaw_motor = Motor(port=jaw_motor_port)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)


    def calibrate_legs(self):
        self.left_motor.run(speed=100)
        self.left_motor.run(speed=100)   

        while self.touch_sensor.pressed:
            pass

        self.tank_driver.off(brake=True)

        self.left_motor.on(speed=40)

        while not self.touch_sensor.is_pressed:
            pass

        self.left_motor.off(brake=True)

        self.left_motor.on_for_rotations(
            rotations=-0.2,
            speed=50,
            brake=True,
            block=True)

        self.right_motor.on(speed=40)

        while not self.touch_sensor.is_pressed:
            pass

        self.right_motor.off(brake=True)

        self.right_motor.on_for_rotations(
            rotations=-0.2,
            speed=50,
            brake=True,
            block=True)

        self.left_motor.reset()
        self.right_motor.reset()
