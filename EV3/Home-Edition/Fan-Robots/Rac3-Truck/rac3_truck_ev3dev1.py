#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    InfraredSensor, RemoteControl, INPUT_4,
    Sound
)

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (
    LargeMotor as FastLargeMotor,
    MediumMotor as FastMediumMotor
)

from time import sleep


class Rac3Truck:
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            polarity: str = Motor.POLARITY_INVERSED,
            steer_motor_port: str = OUTPUT_A,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast=False):
        if fast:
            self.left_motor = FastLargeMotor(address=left_motor_port)
            self.right_motor = FastLargeMotor(address=right_motor_port)

            self.steer_motor = FastMediumMotor(address=steer_motor_port)

        else:
            self.left_motor = LargeMotor(address=left_motor_port)
            self.right_motor = LargeMotor(address=right_motor_port)

            self.steer_motor = MediumMotor(address=steer_motor_port)

        self.left_motor.polarity = self.right_motor.polarity = polarity

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.remote_control = RemoteControl(sensor=self.ir_sensor,
                                            channel=ir_beacon_channel)

        self.speaker = Sound()

    def reset(self):
        """
        Always begin with Reset.
        This puts the steering wheel centred in the middle.
        Then you can drive with MoveTank. Mind the speed settings!
        """
        self.steer_motor.run_timed(
            speed_sp=300,
            time_sp=1500,
            stop_action=Motor.STOP_ACTION_COAST)
        self.steer_motor.wait_while(Motor.STATE_RUNNING)

        self.steer_motor.run_to_rel_pos(
            speed_sp=500,
            position_sp=-120,
            stop_action=Motor.STOP_ACTION_HOLD)
        self.steer_motor.wait_while(Motor.STATE_RUNNING)

        self.steer_motor.reset()

    def left(self):
        """
        Steer to the Left. This only turns the steering wheel.
        So after steering, use MoveTank to drive. Mind the speed settings!
        """
        if self.steer_motor.position > -65:
            self.steer_motor.run_forever(speed_sp=-200)

            while self.steer_motor.position > -65:
                pass

        self.steer_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

    def steer_left(self):
        if self.steer_motor.position > -65:
            self.steer_motor.run_to_abs_pos(
                speed_sp=-200,
                position_sp=-65,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.steer_motor.wait_while(Motor.STATE_RUNNING)

        else:
            self.steer_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

    def right(self):
        """
        Steer to the Right. This only turns the steering wheel.
        So after steering, use MoveTank to drive. Mind the speed settings!
        """
        if self.steer_motor.position < 65:
            self.steer_motor.run_forever(speed_sp=200)

            while self.steer_motor.position < 65:
                pass

        self.steer_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

    def steer_right(self):
        if self.steer_motor.position < 65:
            self.steer_motor.run_to_abs_pos(
                speed_sp=200,
                position_sp=65,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.steer_motor.wait_while(Motor.STATE_RUNNING)

        else:
            self.steer_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

    def center(self):
        """
        When you want to go forwards again, use Center.
        """
        if self.steer_motor.position < -7:
            self.steer_motor.run_forever(speed_sp=200)

            while self.steer_motor.position < 4:
                pass

        elif self.steer_motor.position > 7:
            self.steer_motor.run_forever(speed_sp=-200)

            while self.steer_motor.position > -4:
                pass

        self.steer_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        sleep(0.1)

    def steer_center(self):
        if self.steer_motor.position < -7:
            self.steer_motor.run_to_abs_pos(
                speed_sp=200,
                position_sp=4,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.steer_motor.wait_while(Motor.STATE_RUNNING)

        elif self.steer_motor.position > 7:
            self.steer_motor.run_to_abs_pos(
                speed_sp=-200,
                position_sp=-4,
                stop_action=Motor.STOP_ACTION_HOLD)
            self.steer_motor.wait_while(Motor.STATE_RUNNING)

        self.steer_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)

        sleep(0.1)

    def drive_once_by_ir_beacon(self, speed: float = 800):
        """
        Remote-control your Rac3 Truck with the IR Beacon
        """
        # forward
        if self.remote_control.red_up and self.remote_control.blue_up:
            self.left_motor.run_forever(speed_sp=speed)
            self.right_motor.run_forever(speed_sp=speed)

            self.steer_center()

        # backward
        elif self.remote_control.red_down and self.remote_control.blue_down:
            self.left_motor.run_forever(speed_sp=-speed)
            self.right_motor.run_forever(speed_sp=-speed)

            self.steer_center()

        # turn left forward
        elif self.remote_control.red_up:
            self.left_motor.run_forever(speed_sp=600)
            self.right_motor.run_forever(speed_sp=1000)

            self.steer_left()

        # turn right forward
        elif self.remote_control.blue_up:
            self.left_motor.run_forever(speed_sp=1000)
            self.right_motor.run_forever(speed_sp=600)

            self.steer_right()

        # turn left backward
        elif self.remote_control.red_down:
            self.left_motor.run_forever(speed_sp=-600)
            self.right_motor.run_forever(speed_sp=-1000)

            self.steer_left()

        # turn right backward
        elif self.remote_control.blue_down:
            self.left_motor.run_forever(speed_sp=-1000)
            self.right_motor.run_forever(speed_sp=-600)

            self.steer_right()

        # otherwise stop
        else:
            self.left_motor.stop(stop_action=Motor.STOP_ACTION_COAST)
            self.right_motor.stop(stop_action=Motor.STOP_ACTION_COAST)

            self.steer_center()

    def keep_driving_by_ir_beacon(self, speed: float = 800):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

    def main(self):
        """
        You can control your truck with the IR Beacon
        """
        self.reset()

        sleep(1)

        self.keep_driving_by_ir_beacon()


if __name__ == '__main__':
    RAC3_TRUCK = Rac3Truck()

    RAC3_TRUCK.main()
