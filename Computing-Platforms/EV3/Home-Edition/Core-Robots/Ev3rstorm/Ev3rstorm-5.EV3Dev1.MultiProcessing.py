#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4, 
    Screen, Sound
)

from multiprocessing import Process
from PIL import Image


class Ev3rstorm:
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B, right_foot_motor_port: str = OUTPUT_C,
            bazooka_blast_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.left_foot_motor = LargeMotor(address=left_foot_motor_port)
        self.right_foot_motor = LargeMotor(address=right_foot_motor_port)
        
        self.bazooka_blast_motor = MediumMotor(address=bazooka_blast_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.remote_control = RemoteControl(sensor=self.ir_sensor,
                                            channel=ir_beacon_channel)

        self.screen = Screen()
        self.speaker = Sound()


    def drive_once_by_ir_beacon(
            self,
            speed: float = 1000   # degrees per second
        ):
        # forward
        if self.remote_control.red_up and self.remote_control.blue_up:
            self.left_foot_motor.run_forever(speed_sp=speed)
            self.right_foot_motor.run_forever(speed_sp=speed)

        # backward
        elif self.remote_control.red_down and self.remote_control.blue_down:
            self.left_foot_motor.run_forever(speed_sp=-speed)
            self.right_foot_motor.run_forever(speed_sp=-speed)

        # turn left on the spot
        elif self.remote_control.red_up and self.remote_control.blue_down:
            self.left_foot_motor.run_forever(speed_sp=-speed)
            self.right_foot_motor.run_forever(speed_sp=speed)

        # turn right on the spot
        elif self.remote_control.red_down and self.remote_control.blue_up:
            self.left_foot_motor.run_forever(speed_sp=speed)
            self.right_foot_motor.run_forever(speed_sp=-speed)

        # turn left forward
        elif self.remote_control.red_up:
            self.right_foot_motor.run_forever(speed_sp=speed)

        # turn right forward
        elif self.remote_control.blue_up:
            self.left_foot_motor.run_forever(speed_sp=speed)

        # turn left backward
        elif self.remote_control.red_down:
            self.right_foot_motor.run_forever(speed_sp=-speed)

        # turn right backward
        elif self.remote_control.blue_down:
            self.left_foot_motor.run_forever(speed_sp=-speed)

        # otherwise stop
        else:
            self.left_foot_motor.stop(stop_action=Motor.STOP_ACTION_COAST)
            self.right_foot_motor.stop(stop_action=Motor.STOP_ACTION_COAST)

    def keep_driving_by_ir_beacon(
            self,
            speed: float = 1000   # degrees per second
        ):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)


    def blast_bazooka_whenever_touched(self):
        while True:
            if self.touch_sensor.is_pressed:
                if self.color_sensor.ambient_light_intensity < 5:   # 15 not dark enough
                    self.speaker.play(wav_file='/home/robot/sound/Up.wav').wait()

                    self.bazooka_blast_motor.run_to_rel_pos(
                        speed_sp=1000,   # degrees per second
                        position_sp=-3 * 360,   # degrees
                        stop_action=Motor.STOP_ACTION_HOLD)

                else:
                    self.speaker.play(wav_file='/home/robot/sound/Down.wav').wait()

                    self.bazooka_blast_motor.run_to_rel_pos(
                        speed_sp=1000,   # degrees per second
                        position_sp=3 * 360,   # degrees
                        stop_action=Motor.STOP_ACTION_HOLD)

                while self.touch_sensor.is_pressed:
                    pass
                

    def main(self,
             driving_speed: float = 1000   # degrees per second
            ):
        self.screen.image.paste(im=Image.open('/home/robot/image/Target.bmp'))
        self.screen.update()
    
        Process(target=self.blast_bazooka_whenever_touched,
                daemon=True).start()

        self.keep_driving_by_ir_beacon(speed=driving_speed)


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()
