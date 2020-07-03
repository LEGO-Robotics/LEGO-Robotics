#!/usr/bin/env python3
# (Display not yet working in MicroPython as of 2020)


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor, InfraredSensor
from ev3dev2.display import Display
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

from random import randint
from threading import Thread


class Ev3rstorm:
    def __init__(
            self,
            left_foot_motor_port: str = OUTPUT_B, right_foot_motor_port: str = OUTPUT_C,
            bazooka_blast_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1, color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1):
        self.tank_driver = MoveTank(left_motor_port=left_foot_motor_port,
                                    right_motor_port=right_foot_motor_port,
                                    motor_class=LargeMotor)

        self.bazooka_blast_motor = MediumMotor(address=bazooka_blast_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)
        self.color_sensor = ColorSensor(address=color_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.leds = Leds()
        self.speaker = Sound()
        self.screen = Display()


    def drive_once_by_ir_beacon(self, speed: float = 100):
        # forward
        if self.ir_sensor.top_left(self.ir_beacon_channel) and self.ir_sensor.top_right(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=speed,
                right_speed=speed)

        # backward
        elif self.ir_sensor.bottom_left(self.ir_beacon_channel) and self.ir_sensor.bottom_right(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=-speed)

        # turn left on the spot
        elif self.ir_sensor.top_left(self.ir_beacon_channel) and self.ir_sensor.bottom_right(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=speed)

        # turn right on the spot
        elif self.ir_sensor.top_right(self.ir_beacon_channel) and self.ir_sensor.bottom_left(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=speed,
                right_speed=-speed)

        # turn left forward
        elif self.ir_sensor.top_left(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=0,
                right_speed=speed)

        # turn right forward
        elif self.ir_sensor.top_right(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=speed,
                right_speed=0)

        # turn left backward
        elif self.ir_sensor.bottom_left(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=0,
                right_speed=-speed)

        # turn right backward
        elif self.ir_sensor.bottom_right(self.ir_beacon_channel):
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=0)

        # otherwise stop
        else:
            self.tank_driver.off(brake=False)

    def keep_driving_by_ir_beacon(self, speed: float = 100):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

    
    def dance_whenever_ir_beacon_pressed(self):
        while True:
            while self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                self.tank_driver.on_for_seconds(
                    left_speed=randint(-100, 100),
                    right_speed=randint(-100, 100),
                    seconds=1,
                    brake=False,
                    block=True)
                    

    def keep_detecting_objects_by_ir_sensor(self):
        while True:
            if self.ir_sensor.proximity < 25: 
                self.leds.animate_police_lights(
                    color1=Leds.ORANGE,
                    color2=Leds.RED,
                    group1=Leds.LEFT,
                    group2=Leds.RIGHT,
                    sleeptime=0.5,
                    duration=5,
                    block=False)
                
                self.speaker.play_file(
                    wav_file='/home/robot/sound/Object.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                self.speaker.play_file(                                  
                    wav_file='/home/robot/sound/Detected.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                self.speaker.play_file(
                    wav_file='/home/robot/sound/Error alarm.wav',
                    volume=100,
                    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            else:
                self.leds.all_off()


    def blast_bazooka_whenever_touched(self):
        while True:
            if self.touch_sensor.is_pressed:
                if self.color_sensor.ambient_light_intensity < 5:   # 15 not dark enough
                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Up.wav',
                        volume=100,
                        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                    self.bazooka_blast_motor.on_for_rotations(
                        speed=100,
                        rotations=-3,
                        brake=True,
                        block=True)

                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Laughing 1.wav',
                        volume=100,
                        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                else:
                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Down.wav',
                        volume=100,
                        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                    self.bazooka_blast_motor.on_for_rotations(
                        speed=100,
                        rotations=3,
                        brake=True,
                        block=True)

                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Laughing 2.wav',
                        volume=100,
                        play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

                self.touch_sensor.wait_for_released()
        
    
    def main(self, driving_speed: float = 100):
        self.screen.image_filename(
            filename='/home/robot/image/Target.bmp',
            clear_screen=True)
        self.screen.update()

        # FIXME
        # Traceback (most recent call last):
        # File "/usr/lib/python3.5/threading.py", line 914, in _bootstrap_inner
        #   self.run()
        # File "/usr/lib/python3.5/threading.py", line 862, in run
        #   self._target(*self._args, **self._kwargs)
        # File "/home/robot/Ev3rstorm/Ev3rstorm-Super.EV3Dev2.Python3.Threading.py", line 170, in dance_whenever_ir_beacon_pressed
        #   while self.ir_sensor.beacon(channel=self.ir_beacon_channel):
        # File "/usr/lib/python3/dist-packages/ev3dev2/sensor/lego.py", line 909, in beacon
        #   return 'beacon' in self.buttons_pressed(channel)
        # File "/usr/lib/python3/dist-packages/ev3dev2/sensor/lego.py", line 919, in buttons_pressed
        #   return self._BUTTON_VALUES.get(self.value(channel), [])
        # File "/usr/lib/python3/dist-packages/ev3dev2/sensor/__init__.py", line 203, in value
        #   self._value[n], value = self.get_attr_int(self._value[n], 'value' + str(n))
        # File "/usr/lib/python3/dist-packages/ev3dev2/__init__.py", line 307, in get_attr_int
        #   return attribute, int(value)
        # ValueError: invalid literal for int() with base 10: ''
        Thread(target=self.dance_whenever_ir_beacon_pressed,
               daemon=True).start()

        # DON'T use IR Sensor in 2 different modes in the same program / loop
        # - https://github.com/pybricks/support/issues/62
        # - https://github.com/ev3dev/ev3dev/issues/1401
        # Thread(target=self.keep_detecting_objects_by_ir_sensor,
        #        daemon=True).start()

        Thread(target=self.blast_bazooka_whenever_touched,
               daemon=True).start()

        self.keep_driving_by_ir_beacon(speed=driving_speed)


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()
