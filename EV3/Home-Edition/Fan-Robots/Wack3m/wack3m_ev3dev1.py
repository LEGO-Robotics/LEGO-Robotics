#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, InfraredSensor, INPUT_1, INPUT_4,
    Leds, Screen, Sound
)

from random import randint
from time import sleep


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

        self.leds = Leds()
        self.screen = Screen()
        self.speaker = Sound()

    def start_up(self):
        self.leds.set_color(
            group=Leds.LEFT,
            color=Leds.RED,
            pct=1)
        self.leds.set_color(
            group=Leds.RIGHT,
            color=Leds.RED,
            pct=1)

        self.screen.draw.text(
            xy=(5, 2),
            text='WACK3M',
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

        self.left_motor.run_timed(
            speed_sp=-300,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.left_motor.wait_while(Motor.STATE_RUNNING)

        self.left_motor.reset()

        self.middle_motor.run_timed(
            speed_sp=-50,
            time_sp=2000,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.middle_motor.wait_while(Motor.STATE_RUNNING)

        self.middle_motor.reset()

        self.right_motor.run_timed(
            speed_sp=-300,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.right_motor.wait_while(Motor.STATE_RUNNING)

        self.right_motor.reset()

    def main(self):
        self.start_up()

        while True:

            self.leds.set_color(
                group=Leds.LEFT,
                color=Leds.ORANGE,
                pct=1)
            self.leds.set_color(
                group=Leds.RIGHT,
                color=Leds.ORANGE,
                pct=1)


if __name__ == '__main__':
    WACK3M = Wack3m()

    WACK3M.main()
