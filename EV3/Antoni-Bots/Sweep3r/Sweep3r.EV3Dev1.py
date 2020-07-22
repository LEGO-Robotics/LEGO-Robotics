#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4,
    Screen, Sound
)

from PIL import Image


class Sweep3r():
    def __init__(
            self,
            right_foot_motor_port: str = OUTPUT_C, left_foot_motor_port: str = OUTPUT_B,
            medium_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.right_foot_motor = LargeMotor(address=right_foot_motor_port)
        self.left_foot_motor = LargeMotor(address=left_foot_motor_port)

        self.medium_motor = MediumMotor(address=medium_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.screen = Screen()

        self.speaker = Sound()

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.remote_control = RemoteControl(sensor=self.ir_sensor,
                                            channel=ir_beacon_channel)

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


    def hammer_by_ir_beacon(self):
        if self.remote_control.beacon:
            self.screen.image.paste(im=Image.open('/home/robot/image/Angry.bmp'))
            self.screen.update()
            
            self.medium_motor.run_timed(
                speed_sp=1000,   # deg/s
                time_sp=0.3 * 1000,   # ms 
                stop_action=Motor.STOP_ACTION_HOLD)
            self.medium_motor.wait_while(Motor.STATE_RUNNING)

            self.speaker.play(wav_file='/home/robot/sound/Laughing 2.wav').wait()

            self.medium_motor.run_timed(
                speed_sp=-200,   # deg/s
                time_sp=1000,   # ms 
                stop_action=Motor.STOP_ACTION_HOLD)
            self.medium_motor.wait_while(Motor.STATE_RUNNING)

    def move_when_touched(self, speed_sp: str = 1000):    
        if self.touch_sensor.is_pressed:
           self.right_foot_motor.run_timed(
               time_sp=1000,
               speed_sp=speed_sp)

           self.right_foot_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)

    def spin_when_see_smothing(self, speed_sp: str = 1000):
        if self.color_sensor.reflected_light_intensity < 3:
            self.left_foot_motor.run_timed(
                time_sp=1000,
                speed_sp=speed_sp)

        self.left_foot_motor.stop(stop_action=Motor.STOP_ACTION_BRAKE)
                      
    def main(self,
             speed_sp: float = 1000   # degrees per second
            ):
        self.screen.image.paste(im=Image.open('/home/robot/image/Target.bmp'))
        self.screen.update()
    
        while True:
            self.drive_once_by_ir_beacon(speed=speed_sp)

            self.move_when_touched(speed_sp=speed_sp)

            self.spin_when_see_smothing(speed_sp=speed_sp)


if __name__ == '__main__':
    SWEEP3R = Sweep3r()

    SWEEP3R.main()
