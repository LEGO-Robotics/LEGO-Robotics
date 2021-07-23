#!/usr/bin/env python3


from ev3dev2.motor import \
    Motor, LargeMotor, MediumMotor, MoveTank, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.sound import Sound

from ev3dev2.control.rc_tank import RemoteControlledTank

from multiprocessing import Process


class Catapult(RemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            catapult_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity=Motor.POLARITY_NORMAL,
            speed=1000,
            channel=ir_beacon_channel)
        
        self.catapult_motor = MediumMotor(address=catapult_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.speaker = Sound()

    
    def scan_colors(self):
        if self.color_sensor.color == ColorSensor.COLOR_YELLOW:
            pass

        elif self.color_sensor.color == ColorSensor.COLOR_WHITE:
            self.speaker.play_file(
                wav_file='/home/robot/sound/Good.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)


    def make_noise_when_touched(self):
        if self.touch_sensor.is_pressed:
           self.speaker.play_file(
                wav_file='/home/robot/sound/Ouch.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)


    def throw_by_ir_beacon(self):
        if self.ir_sensor.beacon(channel=self.ir_beacon_channel):
            self.catapult_motor.on_for_degrees(
                speed=-100,
                degrees=150,
                brake=True,
                block=True)

            self.catapult_motor.on_for_degrees(
                speed=100,
                degrees=150,
                brake=True,
                block=True)

            while self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                pass


    def main(self):
        self.speaker.play_file(
            wav_file='/home/robot/sound/Yes.wav',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
             
        Process(target=self.make_noise_when_touched,
                daemon=True).start()

        Process(target=self.throw_by_ir_beacon,
                daemon=True).start()

        Process(target=self.scan_colors,
                daemon=True).start()

        super().main()   # RemoteControlledTank.main()


if __name__ == '__main__':
    CATAPULT = Catapult()

    CATAPULT.main()
