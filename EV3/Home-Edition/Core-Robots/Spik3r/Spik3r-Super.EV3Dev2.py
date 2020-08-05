#!/usr/bin/env python3


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.display import Display
from ev3dev2.sound import Sound


class Spik3r():
    def __init__(
            self,
            sting_motor_port: str = OUTPUT_D, go_motor_port: str = OUTPUT_B,
            claw_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.sting_motor = LargeMotor(address=sting_motor_port)
        self.go_motor = LargeMotor(address=go_motor_port)
        self.claw_motor = MediumMotor(address=claw_motor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.dis = Display()
        self.speaker = Sound()


    def sting_by_ir_beacon(self):
        if self.ir_sensor.beacon(channel=self.ir_beacon_channel):
            self.sting_motor.on_for_degrees(
                speed=-75,
                degrees=220,
                brake=True,
                block=False)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Blip 1.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.sting_motor.on_for_seconds(
                speed=-100,
                seconds=1,
                brake=True,
                block=True)

            self.sting_motor.on_for_seconds(
                speed=100,
                seconds=1,
                brake=True,
                block=True)

            while self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                pass


    def be_noisy_to_people(self):
        if self.color_sensor.reflected_light_intensity > 30:
            for i in range(4):
                self.speaker.play_file(
                    wav_file='/home/robot/sound/Blip 2.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
                        

    def pinch_if_touched(self):
        if self.touch_sensor.is_pressed:
            self.claw_motor.on_for_seconds(
                speed=50,
                seconds=1,
                brake=True,
                block=True)

            self.claw_motor.on_for_seconds(
                speed=-50,
                seconds=0.3,
                brake=True,
                block=True)


    def drive_once_by_ir_beacon(self):
        if self.ir_sensor.top_left(channel=self.ir_beacon_channel) and \
                self.ir_sensor.top_right(channel=self.ir_beacon_channel):
            self.go_motor.on(
                speed=75,
                block=False,
                brake=False)

        elif self.ir_sensor.top_right(channel=self.ir_beacon_channel):
            self.go_motor.on(
                speed=-100,
                brake=False,
                block=False)

        else:
            self.go_motor.off(brake=True)


    def main(self):
        self.dis.image_filename(
            filename='/home/robot/image/Evil.bmp',
            clear_screen=True)
        self.dis.update()

        while True:
            self.drive_once_by_ir_beacon()
            self.be_noisy_to_people()
            self.sting_by_ir_beacon()
            self.pinch_if_touched()


if __name__ == '__main__':
    SPIK3R = Spik3r()

    SPIK3R.main()
