#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_4,
    Sound
)
from ev3dev.helper import RemoteControlledTank

from multiprocessing import Process


class Gripp3r(RemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            grip_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor=left_motor_port, right_motor=right_motor_port,
            polarity=Motor.POLARITY_NORMAL)

        self.grip_motor = MediumMotor(address=grip_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel
        self.beacon = RemoteControl(sensor=self.ir_sensor,
                                    channel=ir_beacon_channel)

        self.speaker = Sound()


    def grip_or_release_by_ir_beacon(self, speed: float = 50):
        while True:
            if self.beacon.beacon:
                if self.touch_sensor.is_pressed:
                    self.speaker.play(wav_file='/home/robot/sound/Air release.wav')

                    self.grip_motor.run_timed(
                        speed_sp=500,
                        time_sp=1000,
                        stop_action=Motor.STOP_ACTION_BRAKE)
                    self.grip_motor.wait_while(Motor.STATE_RUNNING)

                else:
                    self.speaker.play(wav_file='/home/robot/sound/Airbrake.wav')

                    self.grip_motor.run_forever(speed_sp=-500)

                    while not self.touch_sensor.is_pressed:
                        pass
            
                    self.grip_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)

                while self.beacon.beacon:
                    pass

        
    def main(self):
        self.grip_motor.run_timed(
            speed_sp=-500,
            time_sp=1000,
            stop_action=Motor.STOP_ACTION_BRAKE)
        self.grip_motor.wait_while(Motor.STATE_RUNNING)

        Process(target=self.grip_or_release_by_ir_beacon,
                daemon=True).start()

        super().main()
            

if __name__ == '__main__':
    GRIPP3R = Gripp3r()

    GRIPP3R.main()
