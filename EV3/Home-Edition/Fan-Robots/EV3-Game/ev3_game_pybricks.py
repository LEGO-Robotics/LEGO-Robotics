#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop

from random import randint
from time import sleep, time


class EV3Game(EV3Brick):
    N_LEVELS = 9
    N_SHUFFLE_SECONDS = 15
    OFFSET_HOLDCUP = 60

    def __init__(
            self,
            b_motor_port: Port = Port.B, c_motor_port: Port = Port.C,
            grip_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        self.b_motor = Motor(port=b_motor_port,
                             positive_direction=Direction.CLOCKWISE)
        self.c_motor = Motor(port=c_motor_port,
                             positive_direction=Direction.CLOCKWISE)

        self.grip_motor = Motor(port=grip_motor_port,
                                positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    def calibrate_grip(self):
        # self.grip_motor.run(speed=-100)

        # sleep(0.5)

        self.grip_motor.run_until_stalled(
            speed=-100,
            then=Stop.HOLD,
            duty_limit=None)

        self.grip_motor.run_angle(
            speed=100,
            rotation_angle=30,
            then=Stop.HOLD,
            wait=True)

    def display_level(self):
        self.screen.clear()

        self.screen.draw_text(
            x=0, y=0,
            text='Level {}'.format(self.level),
            text_color=Color.BLACK,
            background_color=None)

        sleep(1)

    def display_cup_number(self):
        ...

    def start_up(self):
        self.light.on(color=Color.RED)

        self.calibrate_grip()

        self.screen.clear()

        self.level = 1

        self.display_level()

        self.choice = 2

        self.display_cup_number()

        self.current_b = self.current_c = 1

    def select_level(self):
        while not self.touch_sensor.pressed():
            ir_buttons_pressed = \
                set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

            if ir_buttons_pressed.intersection(
                    {Button.LEFT_UP, Button.RIGHT_UP}) and \
                    (self.level < self.N_LEVELS):
                self.level += 1

                self.display_level()

            elif ir_buttons_pressed.intersection(
                    {Button.LEFT_DOWN, Button.RIGHT_DOWN}) and \
                    (self.level > 1):
                self.level -= 1

                self.display_level()

        self.speaker.play_file(file=SoundFile.GO)

    def move_1_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = self.OFFSET_HOLDCUP + 180

        elif self.current_b == 2:
            self.rotate_b = 2 * self.OFFSET_HOLDCUP + 180

        elif self.current_b == 3:
            self.rotate_b = 180

    def move_1_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = 0

        elif self.current_c == 2:
            self.rotate_c = -self.OFFSET_HOLDCUP

        elif self.current_c == 3:
            self.rotate_c = self.OFFSET_HOLDCUP

    def move_1(self):
        self.move_1_rotate_b()
        self.move_1_rotate_c()

        self.current_b = 3
        self.current_c = 1

    def move_2_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = -self.OFFSET_HOLDCUP - 180

        elif self.current_b == 2:
            self.rotate_b = -180

        elif self.current_b == 3:
            self.rotate_b = -2 * self.OFFSET_HOLDCUP - 180

    def move_2_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = 0

        elif self.current_c == 2:
            self.rotate_c = -self.OFFSET_HOLDCUP

        elif self.current_c == 3:
            self.rotate_c = self.OFFSET_HOLDCUP

    def move_2(self):
        self.move_2_rotate_b()
        self.move_2_rotate_c()

        self.current_b = 2
        self.current_c = 1

    def move_3_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = 0

        elif self.current_b == 2:
            self.rotate_b = self.OFFSET_HOLDCUP

        elif self.current_b == 3:
            self.rotate_b = -self.OFFSET_HOLDCUP

    def move_3_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = self.OFFSET_HOLDCUP + 180

        elif self.current_c == 2:
            self.rotate_c = 180

        elif self.current_c == 3:
            self.rotate_c = 2 * self.OFFSET_HOLDCUP + 180

    def move_3(self):
        self.move_3_rotate_b()
        self.move_3_rotate_c()

        self.current_b = 1
        self.current_c = 2

    def move_4_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = 0

        elif self.current_b == 2:
            self.rotate_b = self.OFFSET_HOLDCUP

        elif self.current_b == 3:
            self.rotate_b = -self.OFFSET_HOLDCUP

    def move_4_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = -self.OFFSET_HOLDCUP - 180

        elif self.current_c == 2:
            self.rotate_c = -2 * self.OFFSET_HOLDCUP - 180

        elif self.current_c == 3:
            self.rotate_c = -180

    def move_4(self):
        self.move_4_rotate_b()
        self.move_4_rotate_c()

        self.current_b = 1
        self.current_c = 3

    def execute_move(self):
        speed = 100 * self.level

        if self.rotate_b * self.rotate_c > 0:
            self.b_motor.run_angle(
                speed=speed,
                rotation_angle=self.rotate_b,
                then=Stop.HOLD,
                wait=False)
            self.c_motor.run_angle(
                speed=speed,
                rotation_angle=self.rotate_c,
                then=Stop.HOLD,
                wait=True)

        elif self.current_b == 1:
            self.b_motor.run_angle(
                speed=speed,
                rotation_angle=self.rotate_b,
                then=Stop.HOLD,
                wait=True)

            self.c_motor.run_angle(
                speed=speed,
                rotation_angle=self.rotate_c,
                then=Stop.HOLD,
                wait=True)

        else:
            self.c_motor.run_angle(
                speed=speed,
                rotation_angle=self.rotate_c,
                then=Stop.HOLD,
                wait=True)

            self.b_motor.run_angle(
                speed=speed,
                rotation_angle=self.rotate_b,
                then=Stop.HOLD,
                wait=True)

    def update_ball_cup(self):
        if self.move in {1, 2}:
            if self.cup_with_ball == 1:
                self.cup_with_ball = 2

            elif self.cup_with_ball == 2:
                self.cup_with_ball = 1

        else:
            if self.cup_with_ball == 2:
                self.cup_with_ball = 3

            elif self.cup_with_ball == 3:
                self.cup_with_ball = 2

    def shuffle(self):
        shuffle_start_time = time()

        while time() - shuffle_start_time < self.N_SHUFFLE_SECONDS:
            self.move = randint(1, 4)

            if self.move == 1:
                self.move_1()

            elif self.move == 2:
                self.move_2()

            elif self.move == 3:
                self.move_3()

            elif self.move == 4:
                self.move_4()

            self.execute_move()
            self.update_ball_cup()

    def reset_motor_positions(self):
        """
        Resetting motors' positions like it is done when the moves finish
        """
        # Resetting Motor A to Position 1,
        # which, for Motor A corresponds to Move 3
        self.move_3_rotate_b()

        # Reseting Motor D to Position 1,
        # which, for Motor D corresponds to Move 1
        self.move_1_rotate_c()

        self.current_b = self.current_c = 1

        # Executing the reset for both motors
        self.execute_move()

    def select_choice(self):
        self.choice = None

        while not self.choice:
            ir_buttons_pressed = \
                set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

            if ir_buttons_pressed == {Button.LEFT_UP}:
                self.choice = 1

            elif ir_buttons_pressed == {Button.BEACON}:
                self.choice = 2

                # wait for BEACON button to turn off
                while set(self.ir_sensor.buttons(
                            channel=self.ir_beacon_channel)) \
                        == {Button.BEACON}:
                    pass

            elif ir_buttons_pressed == {Button.RIGHT_UP}:
                self.choice = 3

    def cup_to_center(self):
        # Saving a copy of the current Level
        self.level_copy = self.level

        # Using Level 1 to rotate the chosen cup to the center
        self.level = 1

        if self.choice == 1:
            self.move = 1
            self.move_1()

            self.execute_move()
            self.update_ball_cup()

        elif self.choice == 3:
            self.move = 3
            self.move_3()

            self.execute_move()
            self.update_ball_cup()

        self.reset_motor_positions()

        # Restoring previous value of Level
        self.level = self.level_copy

    def lift_cup(self):
        self.grip_motor.run_angle(
            speed=100,
            rotation_angle=220,
            then=Stop.HOLD,
            wait=True)

    def main(self):
        self.start_up()

        while True:
            self.cup_with_ball = 2

            self.select_level()

            self.light.on(color=Color.GREEN)

            self.shuffle()

            self.reset_motor_positions()

            self.light.off()

            correct_choice = False

            while not correct_choice:
                self.select_choice()

                self.cup_to_center()

                # The choice will be now in the middle, Position 2

                self.lift_cup()

                correct_choice = (self.cup_with_ball == 2)

                if correct_choice:
                    self.light.on(color=Color.GREEN)

                    self.speaker.play_file(file=SoundFile.CHEERING)

                else:
                    self.light.on(color=Color.RED)

                    self.speaker.play_file(file=SoundFile.BOO)

                sleep(2)

                self.calibrate_grip()


if __name__ == '__main__':
    EV3_GAME = EV3Game()

    EV3_GAME.main()
