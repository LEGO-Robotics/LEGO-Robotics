#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4,
    Leds, Sound
)

from random import randint
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


class Kraz3(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_C, right_motor_port: str = OUTPUT_B,
            wiggle_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel,
            polarity=Motor.POLARITY_INVERSED,
            fast=fast)

        if fast:
            self.wiggle_motor = FastMediumMotor(address=wiggle_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

            self.color_sensor = FastColorSensor(address=color_sensor_port)

        else:
            self.wiggle_motor = MediumMotor(address=wiggle_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

            self.color_sensor = ColorSensor(address=color_sensor_port)

        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=ir_beacon_channel)

        self.leds = Leds()
        self.speaker = Sound()

    def kungfu_manoeuvre_if_touched_or_remote_controlled(self):
        """
        Kung-Fu manoeuvre via Touch Sensor and Remote Control of head and arms
        """
        if self.touch_sensor.is_pressed:
            self.speaker.play(wav_file='/home/robot/sound/Kung fu.wav')

            self.wiggle_motor.run_to_rel_pos(
                speed_sp=500,   # degrees per second
                position_sp=360,   # degrees
                stop_action=Motor.STOP_ACTION_HOLD)
            self.wiggle_motor.wait_while(Motor.STATE_RUNNING)

        elif self.beacon.beacon:
            self.wiggle_motor.run_forever(speed_sp=111)

        else:
            self.wiggle_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

    def kungfu_manoeuvre_whenever_touched_or_remote_controlled(self):
        while True:
            self.kungfu_manoeuvre_if_touched_or_remote_controlled()

    def react_to_color(self):
        detected_color = self.color_sensor.color

        if detected_color == ColorSensor.COLOR_YELLOW:
            self.speaker.play(wav_file='/home/robot/sound/Yellow.wav')

            self.wiggle_motor.run_to_rel_pos(
                speed_sp=860,
                position_sp=-360,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.wiggle_motor.wait_while(Motor.STATE_RUNNING)

            self.speaker.play(wav_file='/home/robot/sound/Uh-oh.wav').wait()

            sleep(0.5)

            self.speaker.play(wav_file='/home/robot/sound/Sneezing.wav').wait()

            sleep(0.5)

        elif detected_color == ColorSensor.COLOR_RED:
            self.speaker.play(wav_file='/home/robot/sound/Shouting.wav').wait()

            for _ in range(randint(1, 6)):
                self.speaker.play(
                    wav_file='/home/robot/sound/Smack.wav').wait()

            self.leds.set_color(
                group=Leds.LEFT,
                color=Leds.RED,
                pct=1)
            self.leds.set_color(
                group=Leds.RIGHT,
                color=Leds.RED,
                pct=1)

            self.wiggle_motor.run_to_rel_pos(
                speed_sp=170,
                position_sp=360,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.wiggle_motor.wait_while(Motor.STATE_RUNNING)

            self.speaker.play(wav_file='/home/robot/sound/LEGO.wav').wait()
            self.speaker.play(
                wav_file='/home/robot/sound/MINDSTORMS.wav').wait()

            self.leds.all_off()

        elif detected_color == ColorSensor.COLOR_BROWN:
            self.speaker.play(wav_file='/home/robot/sound/Brown.wav').wait()

            sleep(1)

            self.wiggle_motor.run_to_rel_pos(
                speed_sp=200,
                position_sp=-360,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.wiggle_motor.wait_while(Motor.STATE_RUNNING)

            self.speaker.play(wav_file='/home/robot/sound/Crying.wav').wait()

        elif detected_color == ColorSensor.COLOR_GREEN:
            self.speaker.play(wav_file='/home/robot/sound/Green.wav').wait()

            self.wiggle_motor.run_to_rel_pos(
                speed_sp=400,
                position_sp=-360,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.wiggle_motor.wait_while(Motor.STATE_RUNNING)

            self.speaker.play(wav_file='/home/robot/sound/Yes.wav').wait()

            sleep(1)

        elif detected_color == ColorSensor.COLOR_BLUE:
            self.speaker.play(wav_file='/home/robot/sound/Blue.wav').wait()

            self.speaker.play(
                wav_file='/home/robot/sound/Fantastic.wav').wait()

            self.speaker.play(wav_file='/home/robot/sound/Good job.wav')

            self.wiggle_motor.run_to_rel_pos(
                speed_sp=750,
                position_sp=360,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.wiggle_motor.wait_while(Motor.STATE_RUNNING)

            self.speaker.play(
                wav_file='/home/robot/sound/Magic wand.wav').wait()

    def keep_reacting_to_colors(self):
        while True:
            self.react_to_color()

    def follow_beacon(self):
        """
        Simple "Follow Me" method
        (built by NeXTSTORM and first used in EV3-D4 project)
        """
        ...

    def keep_following_beacon(self):
        while True:
            self.follow_beacon()

    def main(self):
        while True:
            self.drive_once_by_ir_beacon()

            self.kungfu_manoeuvre_if_touched_or_remote_controlled()

            self.react_to_color()


if __name__ == '__main__':
    KRAZ3 = Kraz3()

    KRAZ3.main()
