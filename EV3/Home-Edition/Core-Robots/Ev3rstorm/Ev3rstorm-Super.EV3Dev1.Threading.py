#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, InfraredSensor, RemoteControl, INPUT_1, INPUT_3, INPUT_4, 
    Leds, Screen, Sound
)

from PIL import Image
from threading import Thread


class Ev3rstorm:
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B, right_foot_motor_port: str = OUTPUT_C,
            shooting_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.left_foot_motor = LargeMotor(address=left_foot_motor_port)
        self.right_foot_motor = LargeMotor(address=right_foot_motor_port)
        
        self.shooting_motor = MediumMotor(address=shooting_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.remote_control = RemoteControl(sensor=self.ir_sensor,
                                            channel=ir_beacon_channel)

        self.leds = Leds()
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


    def detect_object_by_ir_sensor(self):
        if self.ir_sensor.proximity < 25: 
            self.leds.set_color(
                group=Leds.LEFT,
                color=Leds.RED,
                pct=1)
            self.leds.set_color(
                group=Leds.RIGHT,
                color=Leds.RED,
                pct=1)
            
            self.speaker.play(wav_file='/home/robot/sound/Object.wav').wait()
            self.speaker.play(wav_file='/home/robot/sound/Detected.wav').wait()
            self.speaker.play(wav_file='/home/robot/sound/Error alarm.wav').wait()

        else:
            self.leds.all_off()

    def keep_detecting_objects_by_ir_sensor(self):
        while True:
            self.detect_object_by_ir_sensor()
            

    def shoot_when_touched(self):
        if self.touch_sensor.is_pressed:
            if self.color_sensor.ambient_light_intensity < 5:   # 15 not dark enough
                self.speaker.play(wav_file='/home/robot/sound/Up.wav').wait()

                self.shooting_motor.run_to_rel_pos(
                    speed_sp=1000,   # degrees per second
                    position_sp=-3 * 360,   # degrees
                    stop_action=Motor.STOP_ACTION_HOLD)

            else:
                self.speaker.play(wav_file='/home/robot/sound/Down.wav').wait()

                self.shooting_motor.run_to_rel_pos(
                    speed_sp=1000,   # degrees per second
                    position_sp=3 * 360,   # degrees
                    stop_action=Motor.STOP_ACTION_HOLD)

            while self.touch_sensor.is_pressed:
                pass

    def shoot_whenever_touched(self):
        while True:
            self.shoot_when_touched()


    def main(self,
             driving_speed: float = 1000   # degrees per second
            ):
        self.screen.image.paste(im=Image.open('/home/robot/image/Target.bmp'))
        self.screen.update()

        # DON'T use IR Sensor in 2 different modes in the same program / loop
        # - https://github.com/pybricks/support/issues/62
        # - https://github.com/ev3dev/ev3dev/issues/1401
        # Thread(target=self.keep_detecting_objects_by_ir_sensor).start()

        Thread(target=self.shoot_whenever_touched).start()

        self.keep_driving_by_ir_beacon(speed=driving_speed)


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()
