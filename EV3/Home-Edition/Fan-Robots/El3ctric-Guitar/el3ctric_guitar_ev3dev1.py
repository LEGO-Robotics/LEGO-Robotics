#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_D,
    TouchSensor, InfraredSensor, INPUT_1, INPUT_4,
    Leds, Screen, Sound
)

from PIL import Image
from time import sleep

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor,
    TouchSensor as FastTouchSensor
)


class El3ctricGuitar:
    NOTES = [1318, 1174, 987, 880, 783, 659, 587, 493, 440, 392, 329, 293]
    N_NOTES = len(NOTES)

    def __init__(
            self,
            lever_motor_port: str = OUTPUT_D,
            touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4,
            fast=False):
        if fast:
            self.lever_motor = FastMediumMotor(address=lever_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

        else:
            self.lever_motor = MediumMotor(address=lever_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)

        self.leds = Leds()
        self.screen = Screen()
        self.speaker = Sound()

    def start(self):
        self.screen.image.paste(
            im=Image.open('/home/robot/image/LEGO.bmp'))
        self.screen.update()

        self.leds.set_color(
            group=Leds.LEFT,
            color=Leds.ORANGE,
            pct=1)
        self.leds.set_color(
            group=Leds.RIGHT,
            color=Leds.ORANGE,
            pct=1)

        self.lever_motor.run_timed(
            speed_sp=50,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_COAST)
        self.lever_motor.wait_while(Motor.STATE_RUNNING)

        self.lever_motor.run_to_rel_pos(
            speed_sp=50,
            position_sp=-30,
            stop_action=Motor.STOP_ACTION_BRAKE)
        self.lever_motor.wait_while(Motor.STATE_RUNNING)

        sleep(0.1)

        self.lever_motor.reset()

    def read_lever(self):
        self.lever = self.lever_motor.position

        if abs(self.lever) <= 4:
            self.lever = 0

    def keep_reading_lever(self):
        while True:
            self.read_lever()

    def play_music(self, debug=False):
        if not self.touch_sensor.is_pressed:
            raw = sum(self.ir_sensor.proximity for _ in range(4)) / 4

            # raw distance typically ranges 0-50 (but sometimes greater)
            fret = min(round(raw / 5, ndigits=None), self.N_NOTES - 1)

            if debug:
                self.screen.clear()

                self.screen.draw.text(
                    xy=(17, 0),
                    text='b={}'.format(self.lever),
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
                    xy=(17, 11),
                    text='f={}'.format(fret),
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
                    xy=(17, 22),
                    text='raw={:.0f}'.format(raw),
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

            self.speaker.tone(
                self.NOTES[fret] - 11 * self.lever,
                100)

    def keep_playing_music(self):
        while True:
            self.play_music()

    def main(self):
        self.start()

        while True:
            self.read_lever()

            self.play_music()


if __name__ == '__main__':
    EL3CTRIC_GUITAR = El3ctricGuitar()

    EL3CTRIC_GUITAR.main()
