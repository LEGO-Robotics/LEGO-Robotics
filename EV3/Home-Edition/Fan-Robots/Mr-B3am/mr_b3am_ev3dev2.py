#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.console import Console
from ev3dev2.sound import Sound

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
        self.console = Console()
        self.speaker = Sound()

    def header_text(self):
        self.console.text_at(
            column=1, row=1,
            text='Mr. B3am!',
            reset_console=True,
            inverse=False,
            alignment='L')

    def insert_b3am(self):
        """
        This first sequence of blocks waits for a B3am to be inserted.
        A B3am is detected when the ambient light level is
        above or equal to the value 3.
        When a B3am is inserted the motor stops and the EV3 says "Thank you".
        """
        self.header_text()

        self.console.text_at(
            column=1, row=2,
            text='Insert B3am!',
            reset_console=False,
            inverse=False,
            alignment='L')

        # self.color_sensor.calibrate_white()   # this leads to wrong detection

        self.gear_motor.on(
            speed=-15,
            brake=False,
            block=False)

        while self.color_sensor.reflected_light_intensity < 3:
            pass

        self.gear_motor.off(brake=True)

        self.speaker.play_file(
            wav_file='/home/robot/sound/Thank you.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

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

        self.console.text_at(
            column=1, row=2,
            text='Measuring B3am!',
            reset_console=False,
            inverse=False,
            alignment='L')

        self.gear_motor.reset()

        self.gear_motor.on(
            speed=-15,
            brake=False,
            block=False)

        while self.color_sensor.reflected_light_intensity > 1:
            pass

        self.gear_motor.off(brake=True)

        self.current_b3am_length = abs(self.gear_motor.position)

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

        self.console.text_at(
            column=1, row=2,
            text='Detecting Color!',
            reset_console=False,
            inverse=False,
            alignment='L')

        self.gear_motor.on_for_degrees(
            speed=15,
            degrees=self.current_b3am_length / 2,
            block=True,
            brake=True)

        self.current_b3am_color = self.color_sensor.color

        self.speaker.play_file(
            wav_file='/home/robot/sound/Detected.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    def eject_b3am(self):
        """
        After the color is found, the EV3 calculates the number of degrees
        required to move the wheels,
        such that the B3am is ejected from the machine.
        """
        self.header_text()

        self.console.text_at(
            column=1, row=2,
            text='Ejecting B3am!',
            reset_console=False,
            inverse=False,
            alignment='L')

        self.gear_motor.on_for_degrees(
            speed=15,
            degrees=self.current_b3am_length / 2 + 700,
            block=True,
            brake=True)

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

            self.console.text_at(
                column=1, row=3,
                text='Press Enter...',
                reset_console=False,
                inverse=False,
                alignment='L')

            while not self.button.enter:
                pass


if __name__ == '__main__':
    MR_B3AM = MrB3am()

    MR_B3AM.main()
