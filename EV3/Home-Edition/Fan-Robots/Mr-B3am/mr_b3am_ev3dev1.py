#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A,
    ColorSensor, INPUT_3,
    Button, Screen, Sound
)

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
            xy=(0, 0),
            text='MR. B3AM',
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
        This waits for a B3am to be inserted.
        A B3am is detected when the ambient light level is
        above or equal to the value 3.
        When a B3am is inserted the motor stops and the EV3 says "Thank you".
        """
        self.header_text()

        self.screen.draw.text(
            xy=(0, 10),
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

        self.gear_motor.run_forever(speed_sp=-150)

        while self.color_sensor.reflected_light_intensity < 3:
            pass

        self.gear_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        self.speaker.play(wav_file='/home/robot/sound/Thank you.wav').wait()

    def measure_b3am(self):
        """
        This measures the length of the B3am,
        by first resetting the motor counter and then moves the B3am
        until the other end is found.
        This is detected when the ambient light level is below the value 1.
        Note that the length measured is the number of degrees
        that the wheels has turned.
        This value will later be converted to the actual B3am length.
        After having found the length of the B3am, the length is saved
        in a variable, named "current_b3am_length_in_degrees".
        """
        self.header_text()

        self.screen.draw.text(
            xy=(0, 10),
            text='Measuring B3am...',
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

        self.gear_motor.reset()

        self.gear_motor.run_forever(speed_sp=-150)

        while self.color_sensor.reflected_light_intensity > 1:
            pass

        self.gear_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        self.current_b3am_length_in_degrees = abs(self.gear_motor.position)

    def detect_color(self):
        """
        Afterwards the B3am is moved half way thorugh the machine
        so its color can be measured.
        When the color is found it is saved in a variable,
        named "current_b3am_color_code" and the EV3 says "Detected".
        Note the saved value is the color ID and this will later be converted
        to the actual color name.
        """
        self.header_text()

        self.screen.draw.text(
            xy=(0, 10),
            text='Detecting Color...',
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

        self.gear_motor.run_to_rel_pos(
            speed_sp=150,
            position_sp=self.current_b3am_length_in_degrees / 2,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.gear_motor.wait_while(Motor.STATE_RUNNING)

        self.current_b3am_color_code = self.color_sensor.color

        self.speaker.play(wav_file='/home/robot/sound/Detected.wav').wait()

    def eject_b3am(self):
        """
        After the color is found, the EV3 calculates the number of degrees
        required to move the wheels,
        such that the B3am is ejected from the machine.
        """
        self.header_text()

        self.screen.draw.text(
            xy=(0, 10),
            text='Ejecting B3am...',
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

        self.gear_motor.run_to_rel_pos(
            speed_sp=150,
            position_sp=self.current_b3am_length_in_degrees / 2 + 700,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.gear_motor.wait_while(Motor.STATE_RUNNING)

    def process_b3am(self):
        self.insert_b3am()

        self.measure_b3am()

        self.detect_color()

        self.eject_b3am()

    def report_result(self, debug=False):
        """
        Report the result of the measurement.
        The switch has a case for each color
        the Color Sensor is able to detect.
        MR-B3AM converts from the number of rotation degrees to B3am lengths.
        """
        self.header_text()

        if self.current_b3am_color_code == ColorSensor.COLOR_BLACK:
            self.current_b3am_color = 'black'

            if 400 <= self.current_b3am_length_in_degrees <= 600:
                self.current_b3am_length = 5

            elif 601 <= self.current_b3am_length_in_degrees <= 800:
                self.current_b3am_length = 7

            elif 801 <= self.current_b3am_length_in_degrees <= 1000:
                self.current_b3am_length = 9

            elif 1001 <= self.current_b3am_length_in_degrees <= 1300:
                self.current_b3am_length = 11

            elif 1301 <= self.current_b3am_length_in_degrees <= 1500:
                self.current_b3am_length = 13

            elif 1501 <= self.current_b3am_length_in_degrees <= 1700:
                self.current_b3am_length = 15

            else:
                self.current_b3am_length = 'UNKNOWN'

        elif self.current_b3am_color_code == ColorSensor.COLOR_RED:
            self.current_b3am_color = 'red'

            if 400 <= self.current_b3am_length_in_degrees <= 800:
                self.current_b3am_length = 5

            elif 801 <= self.current_b3am_length_in_degrees <= 1050:
                self.current_b3am_length = 7

            elif 1051 <= self.current_b3am_length_in_degrees <= 1300:
                self.current_b3am_length = 9

            elif 1301 <= self.current_b3am_length_in_degrees <= 1500:
                self.current_b3am_length = 11

            elif 1501 <= self.current_b3am_length_in_degrees <= 1700:
                self.current_b3am_length = 13

            elif 1701 <= self.current_b3am_length_in_degrees <= 1900:
                self.current_b3am_length = 15

            else:
                self.current_b3am_length = 'UNKNOWN'

        else:
            self.current_b3am_color = 'UNKNOWN'
            self.current_b3am_length = 'UNKNOWN'

        self.screen.draw.text(
            xy=(0, 20),
            text='Color: {}'.format(self.current_b3am_color.upper()),
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

        self.screen.draw.text(
            xy=(0, 30),
            text='Length: {}'.format(self.current_b3am_length),
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

        # make Mr. B3am print more information about the B3ams
        if debug:
            self.screen.draw.text(
                xy=(0, 50),
                text='Color Code: {}'.format(self.current_b3am_color_code),
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

            self.screen.draw.text(
                xy=(0, 60),
                text='Degrees: {:,}'.format(
                        self.current_b3am_length_in_degrees),
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

        self.speaker.speak(
            text='{} {}'.format(
                self.current_b3am_color,
                self.current_b3am_length)).wait()

    def main(self, debug=False):
        """
        Main Loop
        """
        while True:
            self.process_b3am()

            self.report_result(debug=debug)

            self.screen.draw.text(
                xy=(0, 80),
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

    MR_B3AM.main(debug=True)
