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
        """
        This first sequence of blocks waits for a B3am to be inserted. 
        A B3am is detected when the ambient light level is
        above or equal to the value 3.
        When a B3am is inserted the motor stops and the EV3 says "Thank you".
        """
        self.hello_text()

        self.screen.draw_text(
            x=0, y=18,
            text='Insert B3am!',
            text_color=Color.BLACK,
            background_color=None)

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
        self.hello_text()

        self.screen.draw_text(
            x=0, y=18,
            text='Measuring B3am!',
            text_color=Color.BLACK,
            background_color=None)

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
        self.hello_text()

        self.screen.draw_text(
            x=0, y=18,
            text='Detecting Color!',
            text_color=Color.BLACK,
            background_color=None)

    def eject_b3am(self):
        """
        After the color is found, the EV3 calculates the number of degrees
        required to move the wheels,
        such that the B3am is ejected from the machine.
        """
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
