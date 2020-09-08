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


    def calibrate_legs(self):
        self.left_motor.run(speed=100)
        self.right_motor.run(speed=100)   

        while self.touch_sensor.pressed:
            pass

        self.left_motor.stop()
        self.right_motor.stop()

        self.left_motor.run(speed=400)

        while not self.touch_sensor.is_pressed:
            pass

        self.left_motor.stop()

        self.left_motor.run_angle(
            rotation_angle=0.2 * 360,
            speed=-500,
            then=Stop.HOLD,
            wait=True)

        self.right_motor.run(speed=400)

        while not self.touch_sensor.is_pressed:
            pass

        self.left_motor.stop()

        self.left_motor.run_angle(
            rotation_angle=0.2 * 360,
            speed=-500,
            then=Stop.HOLD,
            wait=True)

        self.left_motor.reset()
        self.right_motor.reset()
