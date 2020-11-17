#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Direction, Port, Stop, Color

from time import sleep, time
from random import randint


class Wack3m(EV3Brick):
    def __init__(
            self,
            left_motor_port: str = Port.B, right_motor_port: str = Port.C,
            middle_motor_port: str = Port.A,
            touch_sensor_port: str = Port.S1, ir_sensor_port: str = Port.S4):
        self.left_motor = Motor(port=left_motor_port,
                                positive_direction=Direction.CLOCKWISE)
        self.right_motor = Motor(port=right_motor_port,
                                 positive_direction=Direction.CLOCKWISE)
        self.middle_motor = Motor(port=middle_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)

    def start_up(self):
        self.light.on(color=Color.RED)

        self.screen.clear()
        self.screen.draw_text(
            x=5, y=2,
            text='WACK3M',
            text_color=Color.BLACK,
            background_color=None)

        self.left_motor.run_time(
            speed=-300,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        self.left_motor.reset_angle(angle=0)

        self.middle_motor.run_time(
            speed=-50,
            time=2000,
            then=Stop.HOLD,
            wait=True)

        self.middle_motor.reset_angle(angle=0)

        self.right_motor.run_time(
            speed=-300,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        self.right_motor.reset_angle(angle=0)

    def main(self):
        self.start_up()

        while True:
            self.light.on(color=Color.ORANGE)


if __name__ == '__main__':
    WACK3M = Wack3m()

    WACK3M.main()
