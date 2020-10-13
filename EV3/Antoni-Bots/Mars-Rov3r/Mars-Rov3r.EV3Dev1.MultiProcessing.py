#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, INPUT_1, INPUT_3, INPUT_4,
    Sound, RemoteControl, InfraredSensor
)

from multiprocessing import Process

# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.drive_util_ev3dev1 import IRBeaconRemoteControlledTank


class MarsRov3r(IRBeaconRemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B,
            right_motor_port: str = OUTPUT_C,
            grip_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_motor_port,
            right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel)

        self.grip_motor = MediumMotor(address=grip_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel
        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=ir_beacon_channel)

        self.speaker = Sound()

    is_gripping = False

    def grip_or_release_claw_by_ir_beacon(self):
        while True:
            if self.beacon.beacon:
                if self.is_gripping:
                    self.grip_motor.run_timed(
                        speed_sp=1000,
                        time_sp=2000,
                        stop_action=Motor.STOP_ACTION_BRAKE)
                    self.grip_motor.wait_while(Motor.STATE_RUNNING)

                    self.speaker.play(
                        wav_file='/home/robot/sound/Air release.wav').wait()

                    self.is_gripping = False

                else:
                    self.grip_motor.run_timed(
                        speed_sp=-1000,
                        time_sp=2000,
                        stop_action=Motor.STOP_ACTION_BRAKE)
                    self.grip_motor.wait_while(Motor.STATE_RUNNING)

                    self.speaker.play(
                        wav_file='/home/robot/sound/Airbrake.wav').wait()

                    self.is_gripping = True

                while self.beacon.beacon:
                    pass

    def main(self, speed: float = 1000):
        self.grip_motor.run_timed(
            speed_sp=500,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_BRAKE)
        self.grip_motor.wait_while(Motor.STATE_RUNNING)

        Process(target=self.grip_or_release_claw_by_ir_beacon,
                daemon=True).start()

        self.keep_driving_by_ir_beacon(speed=speed)


if __name__ == '__main__':
    MARS_ROV3R = MarsRov3r()

    MARS_ROV3R.main()
