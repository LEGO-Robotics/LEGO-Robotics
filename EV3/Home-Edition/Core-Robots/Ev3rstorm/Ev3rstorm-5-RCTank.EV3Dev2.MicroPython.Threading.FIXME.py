#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.control.rc_tank import RemoteControlledTank
from ev3dev2.sound import Sound

from threading import Thread


class Ev3rstorm(RemoteControlledTank):
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B,
            right_foot_motor_port: str = OUTPUT_C,
            shooting_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            color_sensor_port: str = INPUT_3,
            ir_beacon_channel: int = 1):
        super().__init__(
            left_motor_port=left_foot_motor_port, right_motor_port=right_foot_motor_port,
            polarity='normal',
            speed=1000,
            channel=ir_beacon_channel)

        self.shooting_motor = MediumMotor(address=shooting_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.speaker = Sound()


    def shoot_whenever_touched(self):
        while True:
            if self.touch_sensor.is_pressed:
                if self.color_sensor.ambient_light_intensity <= 5:
                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Up.wav',
                        volume=100,
                        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                    self.shooting_motor.on_for_rotations(
                        speed=100,
                        rotations=-3,
                        brake=True,
                        block=True)

                else:
                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Down.wav',
                        volume=100,
                        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                    self.shooting_motor.on_for_rotations(
                        speed=100,
                        rotations=3,
                        brake=True,
                        block=True)

                self.touch_sensor.wait_for_released()
 
    
    def main(self):
        Thread(target=self.shoot_whenever_touched).start()

        super().main()   # RemoteControlledTank.main()
        # FIXME
        # ERROR:ev3dev2.control.rc_tank:'InfraredSensor' object has no attribute '_state'
        # Traceback (most recent call last):
        # File "ev3dev2/control/rc_tank.py", line 40, in main
        # File "ev3dev2/sensor/lego.py", line 959, in process
        # AttributeError: 'InfraredSensor' object has no attribute '_state'
        

if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()
