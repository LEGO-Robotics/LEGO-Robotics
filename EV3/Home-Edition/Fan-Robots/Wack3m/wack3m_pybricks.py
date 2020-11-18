#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Direction, Port, Stop, Color

from time import sleep, time
from random import randint, uniform


class Wack3m(EV3Brick):
    N_WACK_TIMES = 10

    def __init__(
            self,
            left_motor_port: str = Port.B, right_motor_port: str = Port.C,
            middle_motor_port: str = Port.A,
            touch_sensor_port: str = Port.S1, ir_sensor_port: str = Port.S4):
        self.left_motor = Motor(port=left_motor_port,
                                positive_direction=Direction.CLOCKWISE)
        self.right_motor = Motor(port=right_motor_port,
                                 positive_direction=Direction.CLOCKWISE)
        self.middle_motor = Motor(port=middle_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)

    def start_up(self):
        self.light.on(color=Color.RED)

        self.screen.clear()
        self.screen.print('WACK3M')

        self.left_motor.run_time(
            speed=-300,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        self.left_motor.reset_angle(angle=0)

        self.middle_motor.run_time(
            speed=-50,
            time=2000,
            then=Stop.HOLD,
            wait=True)

        self.middle_motor.reset_angle(angle=0)

        self.right_motor.run_time(
            speed=-300,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        self.right_motor.reset_angle(angle=0)

    def main(self):
        self.start_up()

        while True:
            self.speaker.play_file(file=SoundFile.START)

            self.screen.load_image(ImageFile.TARGET)

            self.light.on(color=Color.ORANGE)

            while not self.touch_sensor.pressed():
                pass

            self.speaker.play_file(file=SoundFile.GO)

            self.light.on(color=Color.GREEN)

            total_response_time = 0

            sleep(1)

            for _ in range(self.N_WACK_TIMES):
                self.light.on(color=Color.GREEN)

                self.screen.load_image(ImageFile.EV3_ICON)

                sleep(uniform(0.1, 3))

                which_motor = randint(1, 3)

                if which_motor == 1:
                    self.left_motor.run_angle(
                        speed=1000,
                        rotation_angle=60,
                        then=Stop.COAST,
                        wait=True)

                    self.screen.load_image(ImageFile.MIDDLE_LEFT)

                    self.left_motor.run_time(
                        speed=-400,
                        time=1000 * 0.5,
                        then=Stop.HOLD,
                        wait=True)

                    proximity = self.ir_sensor.distance()
                    start_time = time()
                    while abs(self.ir_sensor.distance() - proximity) <= 2:
                        pass

                elif which_motor == 2:
                    self.middle_motor.run_angle(
                        speed=500,
                        rotation_angle=170,
                        then=Stop.COAST,
                        wait=True)

                    self.screen.load_image(ImageFile.NEUTRAL)

                    self.middle_motor.run_time(
                        speed=-400,
                        time=1000 * 0.4,
                        then=Stop.HOLD,
                        wait=True)

                    proximity = self.ir_sensor.distance()
                    start_time = time()
                    while abs(self.ir_sensor.distance() - proximity) <= 3:
                        pass

                else:
                    self.right_motor.run_angle(
                        speed=1000,
                        rotation_angle=60,
                        then=Stop.COAST,
                        wait=True)

                    self.screen.load_image(ImageFile.MIDDLE_RIGHT)

                    self.right_motor.run_time(
                        speed=-400,
                        time=1000 * 0.5,
                        then=Stop.HOLD,
                        wait=True)

                    proximity = self.ir_sensor.distance()
                    start_time = time()
                    while abs(self.ir_sensor.distance() - proximity) <= 3:
                        pass

                response_time = time() - start_time

                self.screen.load_image(ImageFile.DIZZY)

                self.screen.print(response_time)

                self.light.on(color=Color.RED)

                self.speaker.play_file(file=SoundFile.BOING)

                total_response_time += response_time

            average_response_time = total_response_time / self.N_WACK_TIMES

            self.screen.clear()
            self.screen.print(
                'Avg. Time: {:.1f}s'.format(average_response_time))

            self.speaker.play_file(
                file=SoundFile.FANTASTIC
                     if average_response_time <= 1
                     else SoundFile.GOOD_JOB)

            self.speaker.play_file(file=SoundFile.GAME_OVER)

            self.light.on(color=Color.RED)

            sleep(4)


if __name__ == '__main__':
    WACK3M = Wack3m()

    WACK3M.main()
