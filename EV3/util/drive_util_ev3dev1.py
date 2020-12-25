#!/usr/bin/env python3


__all__ = 'IRBeaconRemoteControlledTank',


from ev3dev.ev3 import \
    Motor, LargeMotor, OUTPUT_B, OUTPUT_C, \
    InfraredSensor, RemoteControl, BeaconSeeker, INPUT_4, \
    Screen

from .ev3dev_fast.ev3fast import LargeMotor as FastLargeMotor

from .ir_beacon_util_ev3dev1 import ir_beacon_measurements_reliable


class IRBeaconRemoteControlledTank:
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            polarity: str = Motor.POLARITY_NORMAL,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            fast: bool = False,
            debug: bool = False):
        self.debug = debug
        if debug:
            self.screen = Screen()

        if fast:
            self.left_motor = FastLargeMotor(address=left_motor_port)
            self.right_motor = FastLargeMotor(address=right_motor_port)
        else:
            self.left_motor = LargeMotor(address=left_motor_port)
            self.right_motor = LargeMotor(address=right_motor_port)

        self.left_motor.polarity = self.right_motor.polarity = polarity

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.tank_drive_remote_control = \
            RemoteControl(
                sensor=self.ir_sensor,
                channel=ir_beacon_channel)
        self.beacon_seeker = \
            BeaconSeeker(
                sensor=self.ir_sensor,
                channel=ir_beacon_channel)

    def drive_once_by_ir_beacon(
            self,
            speed: float = 1000   # degrees per second
            ):
        # forward
        if self.tank_drive_remote_control.red_up and \
                self.tank_drive_remote_control.blue_up:
            self.left_motor.run_forever(speed_sp=speed)
            self.right_motor.run_forever(speed_sp=speed)

        # backward
        elif self.tank_drive_remote_control.red_down and \
                self.tank_drive_remote_control.blue_down:
            self.left_motor.run_forever(speed_sp=-speed)
            self.right_motor.run_forever(speed_sp=-speed)

        # turn left on the spot
        elif self.tank_drive_remote_control.red_up and \
                self.tank_drive_remote_control.blue_down:
            self.left_motor.run_forever(speed_sp=-speed)
            self.right_motor.run_forever(speed_sp=speed)

        # turn right on the spot
        elif self.tank_drive_remote_control.red_down and \
                self.tank_drive_remote_control.blue_up:
            self.left_motor.run_forever(speed_sp=speed)
            self.right_motor.run_forever(speed_sp=-speed)

        # turn left forward
        elif self.tank_drive_remote_control.red_up:
            self.right_motor.run_forever(speed_sp=speed)

        # turn right forward
        elif self.tank_drive_remote_control.blue_up:
            self.left_motor.run_forever(speed_sp=speed)

        # turn left backward
        elif self.tank_drive_remote_control.red_down:
            self.right_motor.run_forever(speed_sp=-speed)

        # turn right backward
        elif self.tank_drive_remote_control.blue_down:
            self.left_motor.run_forever(speed_sp=-speed)

        # otherwise stop
        else:
            self.left_motor.stop(stop_action=Motor.STOP_ACTION_COAST)
            self.right_motor.stop(stop_action=Motor.STOP_ACTION_COAST)

    # this method must be used in a parallel process/thread
    # in order not to block other operations
    def keep_driving_by_ir_beacon(
            self,
            speed: float = 1000   # degrees per second
            ):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

    def follow_ir_beacon_once(
            self,
            speed: float = 1000,   # degrees per second
            target_distance: float = 10):
        heading, distance = self.beacon_seeker.heading_and_distance
        _ir_beacon_measurements_reliable = \
            ir_beacon_measurements_reliable(
                heading_angle=heading,
                distance=distance)

        if self.debug:
            self.screen.clear()
            self.screen.draw.text(
                xy=(0, 0),
                text='HA={}, D={}'.format(heading, distance)
                     if _ir_beacon_measurements_reliable
                     else 'x HA={}, D={}'.format(heading, distance),
                fill=None,
                font=None,
                anchor=None,
                spacing=4,
                align='center',
                direction=None,
                features=None,
                language=None,
                stroke_width=0,
                stroke_fill=None)
            self.screen.update()

        if _ir_beacon_measurements_reliable:
            if heading < -3:
                self.left_motor.run_timed(
                    speed_sp=-speed,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_COAST)
                self.right_motor.run_timed(
                    speed_sp=speed,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_COAST)
                self.left_motor.wait_while(Motor.STATE_RUNNING)
                self.right_motor.wait_while(Motor.STATE_RUNNING)

            elif heading > 3:
                self.left_motor.run_timed(
                    speed_sp=speed,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_COAST)
                self.right_motor.run_timed(
                    speed_sp=-speed,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_COAST)
                self.left_motor.wait_while(Motor.STATE_RUNNING)
                self.right_motor.wait_while(Motor.STATE_RUNNING)

            if distance > target_distance:
                self.left_motor.run_timed(
                    speed_sp=speed,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_COAST)
                self.right_motor.run_timed(
                    speed_sp=speed,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_COAST)
                self.left_motor.wait_while(Motor.STATE_RUNNING)
                self.right_motor.wait_while(Motor.STATE_RUNNING)

            else:
                self.left_motor.run_timed(
                    speed_sp=-speed,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_COAST)
                self.right_motor.run_forever(
                    speed_sp=-speed,
                    time_sp=1000,
                    stop_action=Motor.STOP_ACTION_COAST)
                self.left_motor.wait_while(Motor.STATE_RUNNING)
                self.right_motor.wait_while(Motor.STATE_RUNNING)

    # this method must be used in a parallel process/thread
    # in order not to block other operations
    def keep_following_ir_beacon(
            self,
            speed: float = 1000,   # degrees per second
            target_distance: float = 10):
        while True:
            self.follow_ir_beacon_once(
                speed=speed,
                target_distance=target_distance)


if __name__ == '__main__':
    IR_BEACON_REMOTE_CONTROLLED_TANK = \
        IRBeaconRemoteControlledTank(
            left_motor_port=OUTPUT_B,   # OR: OUTPUT_C
            right_motor_port=OUTPUT_C,    # OR: OUTPUT_B
            polarity=Motor.POLARITY_NORMAL,   # OR: Motor.POLARITY_INVERSED
            debug=True)

    # IR_BEACON_REMOTE_CONTROLLED_TANK.keep_driving_by_ir_beacon(speed=1000)
    # OR:
    IR_BEACON_REMOTE_CONTROLLED_TANK.keep_following_ir_beacon(speed=1000)
