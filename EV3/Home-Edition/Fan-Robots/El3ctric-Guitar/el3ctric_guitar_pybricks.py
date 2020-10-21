#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Direction, Port, Stop

from time import sleep


class El3ctricGuitar(EV3Brick):
    NOTES = [1318, 1174, 987, 880, 783, 659, 587, 493, 440, 392, 329, 293]

    def __init__(
            self,
            lever_motor_port: Port = Port.D,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4):
        self.lever_motor = Motor(port=lever_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)

        self.lever = 0

        self.lever_motor.run_time(
            speed=50,
            time=1000,
            then=Stop.COAST,
            wait=True)

        self.lever_motor.run_angle(
            speed=50,
            rotation_angle=-30,
            then=Stop.HOLD,
            wait=True)

        sleep(0.1)

        self.lever_motor.reset_angle(angle=0)
