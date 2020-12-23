#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4,
    Leds, Screen, Sound
)

from PIL import Image
from random import choice, randint
from threading import Thread
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


class EV3D4(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_C, right_motor_port: str = OUTPUT_B,
            head_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel,
            polarity=Motor.POLARITY_INVERSED,
            fast=fast)

        if fast:
            self.head_motor = FastMediumMotor(address=head_motor_port)

            self.touch_sensor = FastTouchSensor(address=touch_sensor_port)

            self.color_sensor = FastColorSensor(address=color_sensor_port)

        else:
            self.head_motor = MediumMotor(address=head_motor_port)

            self.touch_sensor = TouchSensor(address=touch_sensor_port)

            self.color_sensor = ColorSensor(address=color_sensor_port)

        self.remote_control = RemoteControl(sensor=self.ir_sensor,
                                            channel=ir_beacon_channel)

        self.leds = Leds()
        self.screen = Screen()
        self.speaker = Sound()

        self.state = 0

    def action_1(self):
        self.state = 1

        for _ in range(2):
            self.screen.image.paste(
                im=Image.open('/home/robot/image/Dial 0.bmp'))
            self.screen.update()

            self.speaker.play(
                wav_file='/home/robot/sound/Blip 2.wav')

            self.leds.set_color(
                group=Leds.LEFT,
                color=Leds.ORANGE,
                pct=1)
            self.leds.set_color(
                group=Leds.RIGHT,
                color=Leds.ORANGE,
                pct=1)

            sleep(0.1)

            self.leds.set_color(
                group=Leds.LEFT,
                color=Leds.GREEN,
                pct=1)
            self.leds.set_color(
                group=Leds.RIGHT,
                color=Leds.GREEN,
                pct=1)

            sleep(0.1)

            self.leds.set_color(
                group=Leds.LEFT,
                color=Leds.RED,
                pct=1)
            self.leds.set_color(
                group=Leds.RIGHT,
                color=Leds.RED,
                pct=1)

            sleep(0.1)

        self.speaker.play(
            wav_file='/home/robot/sound/Blip 3.wav').wait()

    def action_2(self):
        self.screen.image.paste(
            im=Image.open('/home/robot/image/Dial 1.bmp'))
        self.screen.update()

        self.speaker.play(
            wav_file='/home/robot/sound/Confirm.wav').wait()

        self.speaker.play(
            wav_file='/home/robot/sound/Walk.wav').wait()

        self.shake_head(left_first=True)

        self.leds.set_color(
            group='LEFT',
            color='RED',
            pct=1)
        self.leds.set_color(
            group='RIGHT',
            color='RED',
            pct=1)

    def action_3(self):
        self.screen.image.paste(
            im=Image.open('/home/robot/image/Dial 3.bmp'))
        self.screen.update()

        self.speaker.play(
            wav_file='/home/robot/sound/Overpower.wav').wait()

        self.speaker.play(
            wav_file='/home/robot/sound/Arm 1.wav').wait()

        self.speaker.play(
            wav_file='/home/robot/sound/Servo 2.wav').wait()

        self.shake_head(
            left_first=False,
            n_times=3)

        self.speaker.play(
            wav_file='/home/robot/sound/Blip 3.wav').wait()

    def action_4(self):
        self.screen.image.paste(
            im=Image.open('/home/robot/image/Dial 4.bmp'))
        self.screen.update()

        self.shake_head(
            left_first=True,
            n_times=2)

        self.speaker.play(
            wav_file='/home/robot/sound/Power down.wav').wait()

        self.speaker.play(
            wav_file='/home/robot/sound/Ready.wav').wait()

        self.speaker.play(
            wav_file='/home/robot/sound/Blip 2.wav').wait()

        self.speaker.play(
            wav_file='/home/robot/sound/Blip 1.wav').wait()

        self.speaker.play(
            wav_file='/home/robot/sound/Blip 3.wav').wait()

    def action_5(self):
        for _ in range(3):
            self.screen.image.paste(
                im=Image.open('/home/robot/image/EV3.bmp'))
            self.screen.update()

            self.leds.set_color(
                group='LEFT',
                color='ORANGE',
                pct=1)
            self.leds.set_color(
                group='RIGHT',
                color='ORANGE',
                pct=1)

            self.speaker.play(
                wav_file='/home/robot/sound/Blip 1.wav').wait()

            self.speaker.play(
                wav_file='/home/robot/sound/Blip 2.wav').wait()

            self.leds.set_color(
                group='LEFT',
                color='RED',
                pct=1)
            self.leds.set_color(
                group='RIGHT',
                color='RED',
                pct=1)

            self.speaker.play(
                wav_file='/home/robot/sound/Blip 4.wav').wait()

            self.leds.set_color(
                group='LEFT',
                color='GREEN',
                pct=1)
            self.leds.set_color(
                group='RIGHT',
                color='GREEN',
                pct=1)

            self.speaker.play(
                wav_file='/home/robot/sound/Blip 3.wav').wait()

    def shake_head(self, left_first: bool = True, n_times: int = 1):
        position_sign = 1 if left_first else -1

        for _ in range(n_times):
            self.head_motor.run_to_rel_pos(
                speed_sp=500,
                position_sp=position_sign * 100,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.head_motor.wait_while(Motor.STATE_RUNNING)

            self.head_motor.run_to_rel_pos(
                speed_sp=500,
                position_sp=-position_sign * 200,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.head_motor.wait_while(Motor.STATE_RUNNING)

            self.head_motor.run_to_rel_pos(
                speed_sp=500,
                position_sp=position_sign * 100,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.head_motor.wait_while(Motor.STATE_RUNNING)

    def main_switch_loop(self, driving_speed: float = 750):
        """
        This is the Main Switch Loop that allows you to control EV3-D4 using
        the Remote and at the same time it helps EV3-D4 to utilise its B+C
        motors when these are not used when driving EV3-D4 with Remote Control.

        The logic is simple:
        If buttons of Remote Control are pressed then EV3-D4 goes (B+C motors)
        wherever you command it, else it moves according to the behavioural
        state that is changed upon interacting with its Touch Sensor, else stop
        B+C motors.
        """
        while True:
            if not self.remote_control.any():
                self.left_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)
                self.right_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

                if self.state == 1:
                    self.left_motor.run_to_rel_pos(
                        speed_sp=driving_speed,
                        position_sp=-1.5 * 360,
                        stop_action=Motor.STOP_ACTION_HOLD)
                    self.right_motor.run_to_rel_pos(
                        speed_sp=driving_speed,
                        position_sp=1.5 * 360,
                        stop_action=Motor.STOP_ACTION_HOLD)
                    self.left_motor.wait_while(Motor.STATE_RUNNING)
                    self.right_motor.wait_while(Motor.STATE_RUNNING)

                    self.left_motor.run_to_rel_pos(
                        speed_sp=driving_speed,
                        position_sp=1.5 * 360,
                        stop_action=Motor.STOP_ACTION_HOLD)
                    self.right_motor.run_to_rel_pos(
                        speed_sp=driving_speed,
                        position_sp=-1.5 * 360,
                        stop_action=Motor.STOP_ACTION_HOLD)
                    self.left_motor.wait_while(Motor.STATE_RUNNING)
                    self.right_motor.wait_while(Motor.STATE_RUNNING)

                elif self.state == 2:
                    self.left_motor.run_to_rel_pos(
                        speed_sp=driving_speed,
                        position_sp=-0.5 * 360,
                        stop_action=Motor.STOP_ACTION_HOLD)
                    self.right_motor.run_to_rel_pos(
                        speed_sp=driving_speed,
                        position_sp=-0.5 * 360,
                        stop_action=Motor.STOP_ACTION_HOLD)
                    self.left_motor.wait_while(Motor.STATE_RUNNING)
                    self.right_motor.wait_while(Motor.STATE_RUNNING)

                    self.left_motor.run_to_rel_pos(
                        speed_sp=driving_speed,
                        position_sp=0.5 * 360,
                        stop_action=Motor.STOP_ACTION_HOLD)
                    self.right_motor.run_to_rel_pos(
                        speed_sp=driving_speed,
                        position_sp=0.5 * 360,
                        stop_action=Motor.STOP_ACTION_HOLD)
                    self.left_motor.wait_while(Motor.STATE_RUNNING)
                    self.right_motor.wait_while(Motor.STATE_RUNNING)

                elif self.state == 3:
                    self.left_motor.run_to_rel_pos(
                        speed_sp=driving_speed,
                        position_sp=0.5 * 360,
                        stop_action=Motor.STOP_ACTION_HOLD)
                    self.right_motor.run_to_rel_pos(
                        speed_sp=driving_speed,
                        position_sp=0.5 * 360,
                        stop_action=Motor.STOP_ACTION_HOLD)
                    self.left_motor.wait_while(Motor.STATE_RUNNING)
                    self.right_motor.wait_while(Motor.STATE_RUNNING)

                    self.left_motor.run_to_rel_pos(
                        speed_sp=driving_speed,
                        position_sp=-0.5 * 360,
                        stop_action=Motor.STOP_ACTION_HOLD)
                    self.right_motor.run_to_rel_pos(
                        speed_sp=driving_speed,
                        position_sp=-0.5 * 360,
                        stop_action=Motor.STOP_ACTION_HOLD)
                    self.left_motor.wait_while(Motor.STATE_RUNNING)
                    self.right_motor.wait_while(Motor.STATE_RUNNING)

                self.state = 0

            elif self.remote_control.beacon:
                self.shake_head(left_first=choice((False, True)))

            else:
                self.drive_once_by_ir_beacon(speed=driving_speed)

    def color_sensor_loop(self):
        """
        This is the Color Sensor Loop that supports 4 different behaviors that
        are triggered RANDOMLY!!!
        """
        while True:
            if self.color_sensor.color == ColorSensor.COLOR_RED:
                random_number = randint(1, 4)

                if random_number == 1:
                    self.action_1()

                elif random_number == 2:
                    self.action_2()

                elif random_number == 3:
                    self.action_3()

                elif random_number == 4:
                    self.action_4()

    def touch_sensor_loop(self):
        """
        This is the Touch Sensor Loop that supports 5 different behaviors that
        are triggered RANDOMLY!!!
        """
        while True:
            if self.touch_sensor.is_pressed:
                random_number = randint(1, 5)

                if random_number == 1:
                    self.action_1()

                elif random_number == 2:
                    self.state = 2
                    self.action_2()

                elif random_number == 3:
                    self.state = 3
                    self.action_3()

                elif random_number == 4:
                    self.state = 2
                    self.action_4()

                elif random_number == 5:
                    self.state = 3
                    self.action_5()

    def main(self, driving_speed: float = 750):
        Thread(
            target=self.color_sensor_loop,
            daemon=True).start()

        Thread(
            target=self.touch_sensor_loop,
            daemon=True).start()

        self.main_switch_loop(driving_speed=driving_speed)


if __name__ == '__main__':
    ev3_d4 = EV3D4()

    ev3_d4.main()
