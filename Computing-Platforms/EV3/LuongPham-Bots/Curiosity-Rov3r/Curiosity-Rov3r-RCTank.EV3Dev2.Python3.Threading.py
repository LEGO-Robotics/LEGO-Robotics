#!/usr/bin/env python3


from ev3dev2.motor import \
    Motor, LargeMotor, MediumMotor, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.display import Display
from ev3dev2.sound import Sound

from ev3dev2.control.rc_tank import RemoteControlledTank

from threading import Thread


class CuriosityRov3r(RemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity=Motor.POLARITY_NORMAL,
            speed=1000,
            channel=ir_beacon_channel)
            
        self.medium_motor = MediumMotor(address=medium_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.dis = Display()
        self.noise = Sound()

    
    def spin_fan(self, speed: float = 100):
        while True:
            if self.color_sensor.reflected_light_intensity > 20:
                self.medium_motor.on(
                    speed=speed,
                    brake=False,
                    block=False)

            else:
                self.medium_motor.off(brake=True)
                

    def say_when_touched(self):
        while True:
            if self.touch_sensor.is_pressed:
                self.dis.image_filename(
                    filename='/home/robot/image/Angry.bmp',
                    clear_screen=True)
                self.dis.update()

                self.noise.play_file(
                    wav_file='/home/robot/sound/No.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                self.medium_motor.on_for_seconds(
                    speed=-50,
                    seconds=3,
                    brake=True,
                    block=True)


    def main(self):
        Thread(target=self.say_when_touched,
               daemon=True).start()

        Thread(target=self.spin_fan,
               daemon=True).start()

        super().main()   # RemoteControlledTank.main()
            

if __name__ == '__main__':
    CURIOSITY_ROV3R = CuriosityRov3r()

    CURIOSITY_ROV3R.main()
