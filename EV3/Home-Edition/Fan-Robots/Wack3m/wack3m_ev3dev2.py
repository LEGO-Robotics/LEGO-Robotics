#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.console import Console
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

from random import randint
from time import sleep, time


class Wack3m:
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            middle_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, ir_sensor_port: str = INPUT_4):
        self.left_motor = LargeMotor(address=left_motor_port)
        self.right_motor = LargeMotor(address=right_motor_port)
        self.middle_motor = MediumMotor(address=middle_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)

        self.console = Console()
        self.leds = Leds()
        self.speaker = Sound()

    def start_up(self):
        self.leds.animate_flash(
            color='RED',
            groups=('LEFT', 'RIGHT'),
            sleeptime=0.5,
            duration=3,
            block=True)

        self.console.text_at(
            column=5, row=2,
            text='WACK3M',
            reset_console=True,
            inverse=False,
            alignment='L')

        self.left_motor.on_for_seconds(
            speed=-30,
            seconds=1,
            brake=True,
            block=True)

        self.left_motor.reset()

        self.middle_motor.on_for_seconds(
            speed=-5,
            seconds=2,
            brake=True,
            block=True)

        self.middle_motor.reset()

        self.right_motor.on_for_seconds(
            speed=-30,
            seconds=1,
            brake=True,
            block=True)

        self.right_motor.reset()

    def main(self):
        self.start_up()

        while True:
            self.leds.animate_flash(
                color='ORANGE',
                groups=('LEFT', 'RIGHT'),
                sleeptime=0.5,
                duration=3,
                block=True)


if __name__ == '__main__':
    WACK3M = Wack3m()

    WACK3M.main()
