#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, InfraredSensor, RemoteControl,
    INPUT_1, INPUT_3, INPUT_4,
    Button, Sound
)

from time import sleep

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    MediumMotor as FastMediumMotor,
    TouchSensor as FastTouchSensor,
    ColorSensor as FastColorSensor
)
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank

from dinor3x_util import cyclic_position_offset


class Dinor3x(IRBeaconRemoteControlledTank):
    FAST_WALK_SPEED = 800
    NORMAL_WALK_SPEED = 400
    SLOW_WALK_SPEED = 200

    # https://sites.google.com/site/ev3python/learn_ev3_python/using-motors
    MEDIUM_MOTOR_POWER_FACTOR = 1.4

    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            jaw_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast: bool = False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel,
            fast=fast)

        if fast:
            self.jaw_motor = FastMediumMotor(address=jaw_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

            self.color_sensor = FastColorSensor(address=color_sensor_port)

        else:
            self.jaw_motor = MediumMotor(address=jaw_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

            self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=ir_beacon_channel)

        self.button = Button()
        self.speaker = Sound()

        self.roaring = False
        self.walk_speed = self.NORMAL_WALK_SPEED

    def roar_by_ir_beacon(self):
        """
        Dinor3x roars when the Beacon button is pressed
        """
        if self.beacon.beacon:
            self.roaring = True
            self.open_mouth()
            self.roar()

        elif self.roaring:
            self.roaring = False
            self.close_mouth()

    def keep_roaring_by_ir_beacon(self):
        while True:
            self.roar_by_ir_beacon()

    def change_speed_by_color(self):
        """
        Dinor3x changes its speed when detecting some colors
        - Red: walk fast
        - Green: walk normally
        - White: walk slowly
        """
        if self.color_sensor.color == ColorSensor.COLOR_RED:
            self.speaker.speak(text='RUN!')
            self.walk_speed = self.FAST_WALK_SPEED
            self.walk(speed=self.walk_speed)

        elif self.color_sensor.color == ColorSensor.COLOR_GREEN:
            self.speaker.speak(text='Normal')
            self.walk_speed = self.NORMAL_WALK_SPEED
            self.walk(speed=self.walk_speed)

        elif self.color_sensor.color == ColorSensor.COLOR_WHITE:
            self.speaker.speak(text='slow.......')
            self.walk_speed = self.SLOW_WALK_SPEED
            self.walk(speed=self.walk_speed)

    def keep_changing_speed_by_color(self):
        while True:
            self.change_speed_by_color()

    def walk_by_ir_beacon(self):
        """
        Dinor3x walks or turns according to instructions from the IR Beacon
        - 2 top/up buttons together: walk forward
        - 2 bottom/down buttons together: walk backward
        - Top Left / Red Up: turn left on the spot
        - Top Right / Blue Up: turn right on the spot
        - Bottom Left / Red Down: stop
        - Bottom Right / Blue Down: calibrate to make the legs straight
        """
        # forward
        if self.tank_drive_remote_control.red_up and \
                self.tank_drive_remote_control.blue_up:
            self.walk(speed=self.walk_speed)

        # backward
        elif self.tank_drive_remote_control.red_down and \
                self.tank_drive_remote_control.blue_down:
            self.walk(speed=-self.walk_speed)

        # turn left on the spot
        elif self.tank_drive_remote_control.red_up:
            self.turn(speed=self.walk_speed)

        # turn right on the spot
        elif self.tank_drive_remote_control.blue_up:
            self.turn(speed=-self.walk_speed)

        # stop
        elif self.tank_drive_remote_control.red_down:
            self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
            self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        # calibrate legs
        elif self.tank_drive_remote_control.blue_down:
            self.calibrate_legs()

    def keep_walking_by_ir_beacon(self):
        while True:
            self.walk_by_ir_beacon()

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

    def position_legs(
            self,
            speed: float = 1000,
            left_position: float = 0,
            right_position: float = 0):
        self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
        self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        self.left_motor.run_to_rel_pos(
            speed_sp=speed,
            position_sp=left_position - self.left_motor.position % 360,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.left_motor.wait_while(Motor.STATE_RUNNING)

        self.right_motor.run_to_rel_pos(
            speed_sp=speed,
            position_sp=right_position - self.right_motor.position % 360,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.right_motor.wait_while(Motor.STATE_RUNNING)

    def leg_adjust(
            self,
            cyclic_degrees: float = 360,
            speed: float = 1000,
            leg_offset_percent: float = 0,
            mirrored_adjust: bool = False,
            brake: bool = True,
            debug: bool = False):
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

            if debug:
                self.screen.clear()
                self.screen.draw.text(
                    xy=(2, 5),
                    text='{}, {}'.format(speed, diff),
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

    def adjust_legs(self, speed: float = 1000, brake: bool = True):
        self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
        self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        diff = (self.left_motor.position % 360) \
            - (self.right_motor.position % 360)

        if diff > 180:
            diff -= 360
        elif diff < -180:
            diff += 360

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

    def walk(self, speed: float = 1000):
        # to make legs ready to walk properly
        self.calibrate_legs()

        # self.adjust_legs(
        #     speed=speed,
        #     brake=False)
        # self.leg_adjust(
        #     cyclic_degrees=360,
        #     speed=speed,
        #     leg_offset_percent=0,
        #     mirrored_adjust=False,
        #     brake=False)

        self.left_motor.run_forever(speed_sp=-speed)
        self.right_motor.run_forever(speed_sp=-speed)

    def walk_n_steps(self, speed: float = 1000, n_steps: int = 1):
        ...

    def turn(self, speed: float = 1000):
        # to make legs ready to walk properly
        self.calibrate_legs()

        # self.adjust_legs(
        #     speed=speed,
        #     brake=False)
        # self.leg_adjust(
        #     cyclic_degrees=360,
        #     speed=speed,
        #     leg_offset_percent=0,
        #     mirrored_adjust=False,
        #     brake=False)

        if speed >= 0:
            self.left_motor.run_to_rel_pos(
                position_sp=180,
                speed_sp=speed,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.left_motor.wait_while(Motor.STATE_RUNNING)

        else:
            self.right_motor.run_to_rel_pos(
                position_sp=180,
                speed_sp=-speed,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.right_motor.wait_while(Motor.STATE_RUNNING)

        self.left_motor.run_forever(speed_sp=speed)
        self.right_motor.run_forever(speed_sp=-speed)

    def turn_n_steps(self, speed: float = 1000, n_steps: int = 1):
        ...

    def close_mouth(self):
        self.jaw_motor.run_timed(
            speed_sp=-self.MEDIUM_MOTOR_POWER_FACTOR * 200,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_COAST)

    def open_mouth(self):
        self.jaw_motor.run_timed(
            speed_sp=self.MEDIUM_MOTOR_POWER_FACTOR * 200,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_COAST)

    def _open_mouth(self):
        self.jaw_motor.run_forever(
            speed_sp=self.MEDIUM_MOTOR_POWER_FACTOR * 200)
        sleep(1)
        self.jaw_motor.stop(stop_action=Motor.STOP_ACTION_COAST)

    def walk_until_blocked(self):
        self.left_motor.run_forever(speed_sp=-400)
        self.right_motor.run_forever(speed_sp=-400)

        while self.ir_sensor.proximity >= 25:
            pass

        self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
        self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

    def back_away(self):
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

    def roar(self):
        self.speaker.play(wav_file='/home/robot/sound/T-rex roar.wav')

        # *** SKIPPING BELOW BLOCK, WHICH SEEMS TO HANG
        # self.jaw_motor.run_to_rel_pos(
        #     position_sp=-60,
        #     speed_sp=self.MEDIUM_MOTOR_POWER_FACTOR * 400,
        #     stop_action=Motor.STOP_ACTION_HOLD)
        # self.jaw_motor.wait_while(Motor.STATE_RUNNING)

        self.jaw_motor.run_timed(
            speed_sp=-self.MEDIUM_MOTOR_POWER_FACTOR * 200,
            time_sp=0.5 * 1000,
            stop_action=Motor.STOP_ACTION_COAST)
        self.jaw_motor.wait_while(Motor.STATE_RUNNING)

        # SKIPPING BELOW BLOCK, WHICH SEEMS TO HANG
        # jaw loop
        # for _ in range(12):
        #     self.jaw_motor.run_timed(
        #         speed_sp=-self.MEDIUM_MOTOR_POWER_FACTOR * 400,
        #         time_sp=0.05 * 1000,
        #         stop_action=Motor.STOP_ACTION_HOLD)
        #     self.jaw_motor.wait_while(Motor.STATE_RUNNING)
        #     self.jaw_motor.run_timed(
        #         speed_sp=self.MEDIUM_MOTOR_POWER_FACTOR * 400,
        #         time_sp=0.05 * 1000,
        #         stop_action=Motor.STOP_ACTION_HOLD)
        #     self.jaw_motor.wait_while(Motor.STATE_RUNNING)

        self.jaw_motor.run_timed(
            speed_sp=self.MEDIUM_MOTOR_POWER_FACTOR * 200,
            time_sp=0.5 * 1000,
            stop_action=Motor.STOP_ACTION_COAST)
        self.jaw_motor.wait_while(Motor.STATE_RUNNING)

    # MAIN
    # ----

    def main(self):
        self.close_mouth()

        while True:
            self.roar_by_ir_beacon()
            self.change_speed_by_color()
            self.walk_by_ir_beacon()


if __name__ == '__main__':
    DINOR3X = Dinor3x()

    DINOR3X.main()
