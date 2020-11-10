#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_4,
    Leds, Screen, Sound
)

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    LargeMotor as FastLargeMotor,
    MediumMotor as FastMediumMotor,
    TouchSensor as FastTouchSensor
)

from random import randint
from time import sleep


class EV3Game:
    def __init__(
            self,
            b_motor_port: str = OUTPUT_B, c_motor_port: str = OUTPUT_C,
            grip_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        if fast:
            self.b_motor = LargeMotor(address=b_motor_port)
            self.c_motor = LargeMotor(address=c_motor_port)

            self.grip_motor = MediumMotor(address=grip_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

        else:
            self.b_motor = FastLargeMotor(address=b_motor_port)
            self.c_motor = FastLargeMotor(address=c_motor_port)

            self.grip_motor = FastMediumMotor(address=grip_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel
        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=ir_beacon_channel)

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

        self.calibrate_grip()

        self.screen.clear()

        self.level = 1

        self.display_level()

        self.choice = 2

        self.display_cup_number()

        self.offset_holdcup = 60

        self.current_b = self.current_c = 1

    def calibrate_grip(self):
        self.grip_motor.run_forever(speed_sp=-100)

        # sleep(0.5)

        self.grip_motor.wait_until_not_moving()

        self.grip_motor.run_to_rel_pos(
            speed_sp=100,
            position_sp=30,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.grip_motor.wait_while(Motor.STATE_RUNNING)

    def display_level(self):
        ...

    def display_cup_number(self):
        ...

    def select_level(self):
        ...

    def move_1_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = self.offset_holdcup + 180

        elif self.current_b == 2:
            self.rotate_b = 2 * self.offset_holdcup + 180

        elif self.current_b == 3:
            self.rotate_b = 180

    def move_1_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = 0

        elif self.current_c == 2:
            self.rotate_c = -self.offset_holdcup

        elif self.current_c == 3:
            self.rotate_c = self.offset_holdcup

    def move_2_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = -self.offset_holdcup - 180

        elif self.current_b == 2:
            self.rotate_b = -180

        elif self.current_b == 3:
            self.rotate_b = -2 * self.offset_holdcup - 180

    def move_2_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = 0

        elif self.current_c == 2:
            self.rotate_c = -self.offset_holdcup

        elif self.current_c == 3:
            self.rotate_c = self.offset_holdcup

    def move_3_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = 0

        elif self.current_b == 2:
            self.rotate_b = self.offset_holdcup

        elif self.current_b == 3:
            self.rotate_b = -self.offset_holdcup

    def move_3_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = self.offset_holdcup + 180

        elif self.current_c == 2:
            self.rotate_c = 180

        elif self.current_c == 3:
            self.rotate_c = 2 * self.offset_holdcup + 180

    def move_4_rotate_b(self):
        if self.current_b == 1:
            self.rotate_b = 0

        elif self.current_b == 2:
            self.rotate_b = self.offset_holdcup

        elif self.current_b == 3:
            self.rotate_b = -self.offset_holdcup

    def move_4_rotate_c(self):
        if self.current_c == 1:
            self.rotate_c = -self.offset_holdcup - 180

        elif self.current_c == 2:
            self.rotate_c = -2 * self.offset_holdcup - 180

        elif self.current_c == 3:
            self.rotate_c = -180

    def execute_move(self):
        speed = 100 * self.level

        if self.rotate_b * self.rotate_c > 0:
            self.b_motor.run_to_rel_pos(
                speed_sp=speed,
                position_sp=self.rotate_b,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.c_motor.run_to_rel_pos(
                speed_sp=speed,
                position_sp=self.rotate_c,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.b_motor.wait_while(Motor.STATE_RUNNING)
            self.c_motor.wait_while(Motor.STATE_RUNNING)

        elif self.current_b == 1:
            self.b_motor.run_to_rel_pos(
                speed_sp=speed,
                position_sp=self.rotate_b,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.b_motor.wait_while(Motor.STATE_RUNNING)

            self.c_motor.run_to_rel_pos(
                speed_sp=speed,
                position_sp=self.rotate_c,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.c_motor.wait_while(Motor.STATE_RUNNING)

        else:
            self.c_motor.run_to_rel_pos(
                speed_sp=speed,
                position_sp=self.rotate_c,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.c_motor.wait_while(Motor.STATE_RUNNING)

            self.b_motor.run_to_rel_pos(
                speed_sp=speed,
                position_sp=self.rotate_b,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.b_motor.wait_while(Motor.STATE_RUNNING)

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
        for _ in range(15):
            self.move = randint(1, 4)

            if self.move == 1:
                self.move_1_rotate_b()
                self.move_1_rotate_c()

                self.current_b = 3
                self.current_c = 1

            elif self.move == 2:
                self.move_2_rotate_b()
                self.move_2_rotate_c()

                self.current_b = 2
                self.current_c = 1

            elif self.move == 3:
                self.move_3_rotate_b()
                self.move_3_rotate_c()

                self.current_b = 1
                self.current_c = 2

            elif self.move == 4:
                self.move_4_rotate_b()
                self.move_4_rotate_c()

                self.current_b = 1
                self.current_c = 3

            self.execute_move()
            self.update_ball_cup()

    def select_choice(self):
        self.choice = None

        while not self.choice:
            if self.beacon.red_up:
                self.choice = 1

            elif self.ir_sensor.beacon:
                self.choice = 2

            elif self.beacon.blue_up:
                self.choice = 3

    def reset_motor_positions(self):
        """
        Resetting motors' positions like it is done when the moves finish
        """
        # Resetting Motor A to Position 1,
        # which, for Motor A corresponds to Move 3
        self.move_3_rotate_b()

        # Resetting Motor D to Position 1,
        # which, for Motor D corresponds to Move 1
        self.move_1_rotate_c()

        self.current_b = self.current_c = 1

        # Executing the reset for both motors
        self.execute_move()

    def cup_to_center(self):
        # Saving a copy of the current Level
        self.level_copy = self.level

        # Using Level 1 to rotate the chosen cup to the center
        self.level = 1

        if self.choice == 1:
            self.move = 1

            self.move_1_rotate_b()
            self.move_1_rotate_c()

            self.current_b = 3
            self.current_c = 1

            self.execute_move()
            self.update_ball_cup()

        elif self.choice == 3:
            self.move == 3

            self.move_3_rotate_b()
            self.move_3_rotate_c()

            self.current_b = 1
            self.current_c = 2

            self.execute_move()
            self.update_ball_cup()

        self.reset_motor_positions()

        # Restoring previous value of level
        self.level = self.level_copy

    def main(self):
        self.start_up()

        while True:
            self.cup_with_ball = 2

            self.select_level()

            self.leds.set_color(
                group=Leds.LEFT,
                color=Leds.GREEN,
                pct=1)
            self.leds.set_color(
                group=Leds.RIGHT,
                color=Leds.GREEN,
                pct=1)

            self.shuffle()

            self.reset_motor_positions()

            self.leds.all_off()

            correct_choice = False

            while not correct_choice:
                self.select_choice()

                self.cup_to_center()

                # The choice will be now in the middle, Position 2

                EV3_GAME.grip_motor.run_to_rel_pos(
                    speed_sp=100,
                    position_sp=220,
                    stop_action=Motor.STOP_ACTION_HOLD)
                EV3_GAME.grip_motor.wait_while(Motor.STATE_RUNNING)

                correct_choice = (self.cup_with_ball == 2)

                if correct_choice:
                    self.leds.set_color(
                        group=Leds.LEFT,
                        color=Leds.GREEN,
                        pct=1)
                    self.leds.set_color(
                        group=Leds.RIGHT,
                        color=Leds.GREEN,
                        pct=1)

                    self.speaker.play(
                        wav_file='/home/robot/sound/Cheering.wav')

                else:
                    self.leds.set_color(
                        group=Leds.LEFT,
                        color=Leds.RED,
                        pct=1)
                    self.leds.set_color(
                        group=Leds.RIGHT,
                        color=Leds.RED,
                        pct=1)

                    self.speaker.play(wav_file='/home/robot/sound/Boo.wav')

            sleep(2)

            self.calibrate_grip()


if __name__ == '__main__':
    EV3_GAME = EV3Game()

    EV3_GAME.main()
