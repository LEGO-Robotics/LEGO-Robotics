#!/usr/bin/env python3
# (Display not yet working in MicroPython as of June 2020)


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, InfraredSensor, TouchSensor
from ev3dev2.display import Display
from ev3dev2.sound import Sound

from multiprocessing import Process


class Ev3rstorm:
    def __init__(
            self,
            left_leg_motor_port: str = OUTPUT_B,
            right_leg_motor_port: str = OUTPUT_C,
            shooting_motor_port: str = OUTPUT_A,
            touch_sensor_port: str = INPUT_1,
            color_sensor_port: str = INPUT_3,
            ir_sensor_port: str = INPUT_4,
            ir_beacon_channel: int = 1):
        self.tank_driver = MoveTank(left_motor_port=left_leg_motor_port,
                                    right_motor_port=right_leg_motor_port,
                                    motor_class=LargeMotor)

        self.shooting_motor = MediumMotor(shooting_motor_port)

        self.touch_sensor = TouchSensor(touch_sensor_port)
        self.color_sensor = ColorSensor(color_sensor_port)

        self.ir_sensor = InfraredSensor(ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.screen = Display()
        self.speaker = Sound()


    # following method must be used in a parallel process in order not to block other operations
    def drive_by_ir_beacon(self, speed: float = 100):
        while True:
            if self.ir_sensor.top_left(self.ir_beacon_channel) and self.ir_sensor.top_right(self.ir_beacon_channel):
                # go forward
                self.tank_driver.on(
                    left_speed=speed,
                    right_speed=speed)
            
            elif self.ir_sensor.bottom_left(self.ir_beacon_channel) and self.ir_sensor.bottom_right(self.ir_beacon_channel):
                # go backward
                self.tank_driver.on(
                    left_speed=-speed,
                    right_speed=-speed)

            elif self.ir_sensor.top_left(self.ir_beacon_channel) and self.ir_sensor.bottom_right(self.ir_beacon_channel):
                # turn around left
                self.tank_driver.on(
                    left_speed=-speed,
                    right_speed=speed)

            elif self.ir_sensor.top_right(self.ir_beacon_channel) and self.ir_sensor.bottom_left(self.ir_beacon_channel):
                # turn around right
                self.tank_driver.on(
                    left_speed=speed,
                    right_speed=-speed)

            elif self.ir_sensor.top_left(self.ir_beacon_channel):
                # turn left
                self.tank_driver.on(
                    left_speed=0,
                    right_speed=speed)

            elif self.ir_sensor.top_right(self.ir_beacon_channel):
                # turn right
                self.tank_driver.on(
                    left_speed=speed,
                    right_speed=0)

            elif self.ir_sensor.bottom_left(self.ir_beacon_channel):
                # left backward
                self.tank_driver.on(
                    left_speed=0,
                    right_speed=-speed)

            elif self.ir_sensor.bottom_right(self.ir_beacon_channel):
                # right backward
                self.tank_driver.on(
                    left_speed=-speed,
                    right_speed=0)

            else:
                self.tank_driver.off(brake=False)


    # following method must be used in a parallel process in order not to block other operations
    def shoot_when_touched(self):
        self.screen.image_filename(
            filename='/home/robot/image/Target.bmp',
            clear_screen=True)

        while True:
            self.touch_sensor.wait_for_pressed()

            if self.color_sensor.ambient_light_intensity < 15:
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


EV3RSTORM = Ev3rstorm(left_leg_motor_port=OUTPUT_B,
                      right_leg_motor_port=OUTPUT_C,
                      shooting_motor_port=OUTPUT_A,
                      touch_sensor_port=INPUT_1,
                      color_sensor_port=INPUT_3,
                      ir_sensor_port=INPUT_4,
                      ir_beacon_channel=1)

Process(target=EV3RSTORM.drive_by_ir_beacon).start()
Process(target=EV3RSTORM.shoot_when_touched).start()
