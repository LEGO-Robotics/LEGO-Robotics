#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A,
    ColorSensor, INPUT_3,
    Button, Screen, Sound
)

from time import sleep

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor,
    ColorSensor as FastColorSensor
)


class MrB3am:
    def __init__(
            self,
            gear_motor_port: str = OUTPUT_A, color_sensor_port: str = INPUT_3,
            fast=False):
        if fast:
            self.gear_motor = FastMediumMotor(address=gear_motor_port)
            self.color_sensor = FastColorSensor(address=color_sensor_port)
        else:
            self.gear_motor = MediumMotor(address=gear_motor_port)
            self.color_sensor = ColorSensor(address=color_sensor_port)

        self.button = Button()
        self.screen = Screen()
        self.speaker = Sound()

    def header_text(self):
        self.screen.clear()

        self.screen.draw.text(
            xy=(2, 0),
            text='Mr. B3am!',
            fill=None,
            font=None,
            anchor=None,
            spacing=4,
            align='left',
            direction=None,
            features=None,
            language=None,
            stroke_width=0,
            stroke_fill=None)

    def insert_b3am(self):
        """
        This first sequence of blocks waits for a B3am to be inserted. 
        A B3am is detected when the ambient light level is
        above or equal to the value 3.
        When a B3am is inserted the motor stops and the EV3 says "Thank you".
        """
        self.header_text()

        self.screen.draw.text(
            xy=(0, 6),
            text='Insert B3am!',
            fill=None,
            font=None,
            anchor=None,
            spacing=4,
            align='left',
            direction=None,
            features=None,
            language=None,
            stroke_width=0,
            stroke_fill=None)

        self.screen.update()

    def measure_b3am(self):
        """
        The next sequence of blocks measures the length of the B3am,
        by first reseting the motor counter and then moves the B3am
        until the other end is found. 
        This is detected when the ambient light level is below the value 1.
        Note that the length measured is the number of degrees
        that the wheels has turned.
        This value will later be converted to the actual B3am length.
        """
        self.header_text()

        self.screen.draw.text(
            xy=(0, 6),
            text='Measuring B3am!',
            fill=None,
            font=None,
            anchor=None,
            spacing=4,
            align='left',
            direction=None,
            features=None,
            language=None,
            stroke_width=0,
            stroke_fill=None)

        self.screen.update()

    def detect_color(self):
        """
        After having found the length of the B3am, the length is saved
        in a variable, named "Length".
        Afterwards the B3am is moved half way thorugh the machine
        so its color can be measured.
        When the color is found it is saved in a variable,
        named "Color" and the EV3 says "Detected".
        Note the saved value is the color ID and this will later be converted
        to the actual color name.
        """
        self.header_text()

        self.screen.draw.text(
            xy=(0, 6),
            text='Detecting Color!',
            fill=None,
            font=None,
            anchor=None,
            spacing=4,
            align='left',
            direction=None,
            features=None,
            language=None,
            stroke_width=0,
            stroke_fill=None)

        self.screen.update()

    def eject_b3am(self):
        """
        After the color is found, the EV3 calculates the number of degrees
        required to move the wheels,
        such that the B3am is ejected from the machine.
        """
        self.header_text()

        self.screen.draw.text(
            xy=(0, 6),
            text='Ejecting B3am!',
            fill=None,
            font=None,
            anchor=None,
            spacing=4,
            align='left',
            direction=None,
            features=None,
            language=None,
            stroke_width=0,
            stroke_fill=None)

        self.screen.update()

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

            self.screen.draw.text(
                xy=(0, 11),
                text='Press Enter...',
                fill=None,
                font=None,
                anchor=None,
                spacing=4,
                align='left',
                direction=None,
                features=None,
                language=None,
                stroke_width=0,
                stroke_fill=None)

            self.screen.update()

            while not self.button.enter:
                pass


if __name__ == '__main__':
    MR_B3AM = MrB3am()

    MR_B3AM.main()
