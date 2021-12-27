#!/usr/bin/env micropython


from ev3dev2.motor import MediumMotor, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.console import Console
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

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
            lever_motor_port: str = OUTPUT_D, touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4, ir_sensor_channel: int = 1,
            fast: bool = False):
        if fast:
            self.lever_motor = FastMediumMotor(address=lever_motor_port)
            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

        else:
            self.lever_motor = MediumMotor(address=lever_motor_port)
            self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_sensor_channel = ir_sensor_channel

        self.console = Console()
        self.leds = Leds()
        self.speaker = Sound()

    def start(self):
        self.leds.animate_flash(
            color='ORANGE',   # Leds.ORANGE
            groups=('LEFT', 'RIGHT'),   # (Leds.LEFT, Leds.RIGHT)
            sleeptime=0.5,
            duration=3,
            block=True)

        self.lever_motor.on_for_seconds(
            speed=5,
            seconds=1,
            brake=False,
            block=True)

        self.lever_motor.on_for_degrees(
            speed=-5,
            degrees=30,
            brake=True,
            block=True)

        sleep(0.1)

        self.lever_motor.reset()

    def read_lever(self):
        self.lever = self.lever_motor.position

        if abs(self.lever) <= 4:
            self.lever = 0

    def keep_reading_lever(self):
        while True:
            self.read_lever()

    def play_music(self):
        if self.touch_sensor.is_released:
            raw = sum(self.ir_sensor.proximity for _ in range(4)) / 4

            # raw distance typically ranges 0-50 (but sometimes greater)
            fret = min(round(raw / 5), self.N_NOTES - 1)

            self.console.text_at(
                text='b={}'.format(self.lever),
                column=1,
                row=1,
                reset_console=True,
                inverse=False,
                alignment='L')

            self.console.text_at(
                text='f={}'.format(fret),
                column=1,
                row=2,
                reset_console=False,
                inverse=False,
                alignment='L')

            self.console.text_at(
                text='raw={:.0f}'.format(raw),
                column=1,
                row=3,
                reset_console=False,
                inverse=False,
                alignment='L')

            self.speaker.tone(
                self.NOTES[fret] - 11 * self.lever,
                100,
                play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

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
