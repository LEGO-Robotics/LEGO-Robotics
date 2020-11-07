#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_4,
    Sound, Screen
)

from time import sleep


class EV3Game:
    def __init__(
            self,
            b_motor_port: str = OUTPUT_B, c_motor_port: str = OUTPUT_C,
            grip_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.b_motor = LargeMotor(address=b_motor_port)
        self.c_motor = LargeMotor(address=c_motor_port)

        self.grip_motor = MediumMotor(address=grip_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel
        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=ir_beacon_channel)

        self.screen = Screen()
        self.speaker = Sound()

        self.offset_holdcup = 60
        self.current_b = self.current_c = 1

    def calibrate_grip(self):
        self.grip_motor.run_forever(speed_sp=-100)

        sleep(0.5)

        self.grip_motor.wait_until_not_moving()

        self.grip_motor.run_to_rel_pos(
            speed_sp=100,
            position_sp=30,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.grip_motor.wait_while(Motor.STATE_RUNNING)

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
            self.rotate_b = self.offset_holdcup + 180

        elif self.current_b == 2:
            self.rotate_b = -180

        elif self.current_b == 3:
            self.rotate_b = 2 * self.offset_holdcup + 180

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
            self.rotate_c = self.offset_holdcup + 180

        elif self.current_c == 2:
            self.rotate_c = 2 * self.offset_holdcup + 180

        elif self.current_c == 3:
            self.rotate_c = -180
