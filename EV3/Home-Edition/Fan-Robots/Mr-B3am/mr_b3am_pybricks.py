#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.tools import wait


class MrB3am(EV3Brick):
    def __init__(
            self,
            gear_motor_port: Port = Port.A,
            color_sensor_port: Port = Port.S3):
        self.gear_motor = Motor(port=gear_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.color_sensor = ColorSensor(port=color_sensor_port)

    def hello_text(self):
        self.screen.clear()
        self.screen.draw_text(
            x=2, y=0,
            text='Mr. B3am!',
            text_color=Color.BLACK,
            background_color=None)

    def insert_b3am(self):
        self.hello_text()

        self.screen.draw_text(
            x=0, y=18,
            text='Insert B3am!',
            text_color=Color.BLACK,
            background_color=None)

    def measure_b3am(self):
        self.hello_text()

        self.screen.draw_text(
            x=0, y=18,
            text='Measuring B3am!',
            text_color=Color.BLACK,
            background_color=None)

    def detect_color(self):
        self.hello_text()

        self.screen.draw_text(
            x=0, y=18,
            text='Detecting Color!',
            text_color=Color.BLACK,
            background_color=None)

    def eject_b3am(self):
        self.hello_text()

        self.screen.draw_text(
            x=0, y=18,
            text='Ejecting B3am!',
            text_color=Color.BLACK,
            background_color=None)

    def process_b3am(self):
        self.insert_b3am()

        self.measure_b3am()

        self.detect_color()

        self.eject_b3am()

    def print_result(self):
        ...

    def debug(self):
        ...

    def main(self):
        while True:
            self.process_b3am()

            self.print_result()

            self.screen.draw_text(
                x=0, y=36,
                text='Press Enter...',
                text_color=Color.BLACK,
                background_color=None)

            while Button.CENTER not in self.buttons.pressed():
                pass


if __name__ == '__main__':
    MR_B3AM = MrB3am()

    MR_B3AM.main()
