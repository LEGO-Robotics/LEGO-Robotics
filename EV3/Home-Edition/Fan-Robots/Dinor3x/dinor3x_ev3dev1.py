#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_4,
    Button, Sound
)

from time import sleep

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor,
    TouchSensor as FastTouchSensor
)
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank

from dinor3x_util import cyclic_position_offset


class Dinor3x(IRBeaconRemoteControlledTank):
    """
    Challenges:
    - Can you make DINOR3X remote controlled with the IR-Beacon?
    - Can you attach a colorsensor to DINOR3X, and make it behave differently
        depending on which color is in front of the sensor
        (red = walk fast, white = walk slow, etc.)?
    """

    # https://sites.google.com/site/ev3python/learn_ev3_python/using-motors
    MEDIUM_MOTOR_POWER_FACTOR = 1.4

    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            jaw_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel,
            fast=fast)

        if fast:
            self.jaw_motor = MediumMotor(address=jaw_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

        else:
            self.jaw_motor = FastMediumMotor(address=jaw_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=ir_beacon_channel)

        self.button = Button()
        self.speaker = Sound()

    def close_mouth(self):
        self.jaw_motor.run_forever(
            speed_sp=self.MEDIUM_MOTOR_POWER_FACTOR * 200)
        sleep(1)
        self.jaw_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

    def roar(self):
        self.speaker.play(wav_file='/home/robot/sound/T-rex roar.wav')

        self.jaw_motor.run_to_rel_pos(
            position_sp=-60,
            speed_sp=self.MEDIUM_MOTOR_POWER_FACTOR * 400,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.jaw_motor.wait_while(Motor.STATE_RUNNING)

        # FIXME: jaw keeps opening wider and wider and doesn't close
        for i in range(12):
            self.jaw_motor.run_timed(
                speed_sp=-self.MEDIUM_MOTOR_POWER_FACTOR * 400,
                time_sp=0.05 * 1000,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.jaw_motor.wait_while(Motor.STATE_RUNNING)

            self.jaw_motor.run_timed(
                speed_sp=self.MEDIUM_MOTOR_POWER_FACTOR * 400,
                time_sp=0.05 * 1000,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.jaw_motor.wait_while(Motor.STATE_RUNNING)

        self.jaw_motor.run_forever(
            speed_sp=self.MEDIUM_MOTOR_POWER_FACTOR * 200)

        sleep(0.5)

    def walk_until_blocked(self):
        self.left_motor.run_forever(speed_sp=-400)
        self.right_motor.run_forever(speed_sp=-400)

        while self.ir_sensor.proximity >= 25:
            pass

        self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
        self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

    def run_away(self):
        self.left_motor.run_to_rel_pos(
            speed_sp=750,
            position_sp=3 * 360,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.right_motor.run_to_rel_pos(
            speed_sp=750,
            position_sp=3 * 360,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.left_motor.wait_while(Motor.STATE_RUNNING)
        self.right_motor.wait_while(Motor.STATE_RUNNING)

    def jump(self):
        """
        Dinor3x Mission 02 Challenge: make it jump
        """
        ...

    # TRANSLATED FROM EV3-G MY BLOCKS
    # -------------------------------

    def calibrate_legs(self):
        self.left_motor.run_forever(speed_sp=100)
        self.right_motor.run_forever(speed_sp=200)

        while self.touch_sensor.is_pressed:
            pass

        self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
        self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        self.left_motor.run_forever(speed_sp=400)

        while not self.touch_sensor.is_pressed:
            pass

        self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        self.left_motor.run_to_rel_pos(
            position_sp=-0.2 * 360,
            speed_sp=500,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.left_motor.wait_while(Motor.STATE_RUNNING)

        self.right_motor.run_forever(speed_sp=400)

        while not self.touch_sensor.is_pressed:
            pass

        self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        self.right_motor.run_to_rel_pos(
            position_sp=-0.2 * 360,
            speed_sp=500,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.right_motor.wait_while(Motor.STATE_RUNNING)

        self.left_motor.reset()
        self.right_motor.reset()

    def leg_to_pos(
            self,
            speed: float = 1000,
            left_position: float = 0,
            right_position: float = 0):
        self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
        self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        self.left_motor.run_to_rel_pos(
            speed_sp=speed,
            position_sp=left_position -
                        cyclic_position_offset(
                            rotation_sensor=self.left_motor.position,
                            cyclic_degrees=360),
            stop_action=Motor.STOP_ACTION_HOLD)
        self.left_motor.wait_while(Motor.STATE_RUNNING)

        self.right_motor.run_to_rel_pos(
            speed_sp=speed,
            position_sp=right_position -
                        cyclic_position_offset(
                            rotation_sensor=self.right_motor.position,
                            cyclic_degrees=360),
            stop_action=Motor.STOP_ACTION_HOLD)
        self.right_motor.wait_while(Motor.STATE_RUNNING)

    def leg_adjust(
            self,
            cyclic_degrees: float,
            speed: float = 1000,
            leg_offset_percent: float = 0,
            mirrored_adjust: bool = False,
            brake: bool = True):
        self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
        self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        diff = cyclic_position_offset(
                rotation_sensor=self.left_motor.position,
                cyclic_degrees=cyclic_degrees) \
            - cyclic_position_offset(
                rotation_sensor=self.right_motor.position,
                cyclic_degrees=cyclic_degrees)

        if diff > (cyclic_degrees / 2):
            diff -= cyclic_degrees

        if diff < -180:
            diff += cyclic_degrees

        if speed >= 0:
            if diff >= 0:
                self.left_motor.run_to_rel_pos(
                    position_sp=-diff,
                    speed_sp=speed,
                    # EV3Dev2 equivalent:
                    # speed=-speed,
                    # degrees=diff,
                    stop_action=Motor.STOP_ACTION_HOLD
                                if brake
                                else Motor.STOP_ACTION_COAST)
                self.left_motor.wait_while(Motor.STATE_RUNNING)

            else:
                self.right_motor.run_to_rel_pos(
                    position_sp=diff,
                    speed_sp=speed,
                    # EV3Dev2 equivalent:
                    # speed=-speed,
                    # degrees=abs(diff),
                    stop_action=Motor.STOP_ACTION_HOLD
                                if brake
                                else Motor.STOP_ACTION_COAST)
                self.right_motor.wait_while(Motor.STATE_RUNNING)

        else:
            if diff >= 0:
                self.right_motor.run_to_rel_pos(
                    position_sp=diff,
                    speed_sp=-speed,
                    stop_action=Motor.STOP_ACTION_HOLD
                                if brake
                                else Motor.STOP_ACTION_COAST)
                self.right_motor.wait_while(Motor.STATE_RUNNING)

            else:
                self.left_motor.run_to_rel_pos(
                    position_sp=abs(diff),
                    speed_sp=-speed,
                    stop_action=Motor.STOP_ACTION_HOLD
                                if brake
                                else Motor.STOP_ACTION_COAST)
                self.left_motor.wait_while(Motor.STATE_RUNNING)

            # TODO: print to screen

    def turn(self, speed: float = 1000, n_steps: int = 1):
        ...

    def walk(self, speed: float = 1000):
        ...

    def walk_steps(self, speed: float = 1000, n_steps: int = 1):
        ...
