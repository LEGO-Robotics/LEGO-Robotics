#!/usr/bin/env python3


from ev3dev.ev3 import (
    Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,
    TouchSensor, ColorSensor, INPUT_1, INPUT_3,
    Screen, Sound
)
from ev3dev.helper import RemoteControlledTank

from multiprocessing import Process
from PIL import Image


class Ev3rstorm(RemoteControlledTank):
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B, right_foot_motor_port: str = OUTPUT_C,
            bazooka_blast_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3):
        super().__init__(
            left_motor=left_foot_motor_port, right_motor=right_foot_motor_port,
            polarity=Motor.POLARITY_NORMAL)
        
        self.bazooka_blast_motor = MediumMotor(address=bazooka_blast_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.screen = Screen()
        self.speaker = Sound()


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


    def main(self):
        self.screen.image.paste(im=Image.open('/home/robot/image/Target.bmp'))
        self.screen.update()
    
        Process(target=self.blast_bazooka_whenever_touched,
                daemon=True).start()
        
        super().main()   # RemoteControlledTank.main()


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()
