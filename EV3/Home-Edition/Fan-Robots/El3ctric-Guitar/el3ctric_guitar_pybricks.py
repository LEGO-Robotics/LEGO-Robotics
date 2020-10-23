#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.tools import wait


class El3ctricGuitar(EV3Brick):
    NOTES = [1318, 1174, 987, 880, 783, 659, 587, 493, 440, 392, 329, 293]
    N_NOTES = len(NOTES)

    def __init__(
            self, lever_motor_port: Port = Port.D,
            touch_sensor_port: Port = Port.S1, ir_sensor_port: Port = Port.S4):
        self.lever_motor = Motor(port=lever_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)

    def start(self):
        self.screen.load_image(ImageFile.EV3)

        self.light.on(color=Color.ORANGE)

        self.lever_motor.run_time(
            speed=50,
            time=1000,
            then=Stop.COAST,
            wait=True)

        self.lever_motor.run_angle(
            speed=50,
            rotation_angle=-30,
            then=Stop.BRAKE,
            wait=True)

        wait(100)

        self.lever_motor.reset_angle(angle=0)

    def read_lever(self):
        self.lever = self.lever_motor.angle()

        if abs(self.lever) <= 4:
            self.lever = 0

    def keep_reading_lever(self):
        while True:
            self.read_lever()

    def play_music(self):
        if not self.touch_sensor.pressed():
            raw = sum(self.ir_sensor.distance() for _ in range(4)) / 4

            # raw distance typically ranges 0-50 (but sometimes greater)
            fret = min(round(raw / 5, ndigits=None), self.N_NOTES - 1)

            self.screen.clear()

            self.screen.draw_text(
                x=17, y=0,
                text='b={}'.format(self.lever),
                text_color=Color.BLACK,
                background_color=None)

            self.screen.draw_text(
                x=17, y=11,
                text='f={}'.format(fret),
                text_color=Color.BLACK,
                background_color=None)

            self.screen.draw_text(
                x=17, y=22,
                text='raw={:.0f}'.format(raw),
                text_color=Color.BLACK,
                background_color=None)

            self.speaker.beep(
                frequency=self.NOTES[fret] - 11 * self.lever,
                duration=100)

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
