#!/usr/bin/env micropython


from ev3dev2.motor import (
    LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
)
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.console import Console
from ev3dev2.display import Display
from ev3dev2.sound import Sound


class EV3Game:
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            grip_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.tank_driver = MoveTank(left_motor_port=left_motor_port,
                                    right_motor_port=right_motor_port,
                                    motor_class=LargeMotor)

        self.grip_motor = MediumMotor(address=grip_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.console = Console()
        self.dis = Display()
        self.speaker = Sound()
