#!/usr/bin/env micropython


from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import InfraredSensor, TouchSensor
from ev3dev2.sound import Sound


class SuperTurtle:
    def __init__(
            self,
            left_leg_motor_port: str = OUTPUT_B, right_leg_motor_port: str = OUTPUT_C,
            shooting_motor_port: str = OUTPUT_A,
            ir_sensor_port: str = INPUT_4, ir_beacon_channel: int = 1,
            touch_sensor_port: str = INPUT_1):
        self.tank_driver = MoveTank(left_motor_port=left_leg_motor_port,
                                    right_motor_port=right_leg_motor_port,
                                    motor_class=LargeMotor)

        self.shooting_motor = MediumMotor(address=shooting_motor_port)

        self.touch_sensor = TouchSensor(address=touch_sensor_port)

        self.ir_sensor = InfraredSensor(address=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

        self.speaker = Sound()


    def drive_by_ir_beacon(self, channel: int = 1, speed: float = 100):
        if self.ir_sensor.top_left(channel=self.ir_beacon_channel) and self.ir_sensor.top_right(channel=self.ir_beacon_channel):
            # go forward
            self.tank_driver.on_for_seconds(
                left_speed=-speed,
                right_speed=0,
                seconds=1,
                brake=True,
                block=True)

            self.tank_driver.on_for_seconds(
                left_speed=0,
                right_speed=-speed,
                seconds=1,
                brake=True,
                block=True)

        elif self.ir_sensor.bottom_left(channel=self.ir_beacon_channel) and self.ir_sensor.bottom_right(channel=self.ir_beacon_channel):
            # go backward
            self.tank_driver.on_for_seconds(
                left_speed=speed,
                right_speed=0,
                seconds=1,
                brake=True,
                block=True)

            self.tank_driver.on_for_seconds(
                left_speed=0,
                right_speed=speed,
                seconds=1,
                brake=True,
                block=True)

        elif self.ir_sensor.top_left(channel=self.ir_beacon_channel) and self.ir_sensor.bottom_right(channel=self.ir_beacon_channel):
            # turn around left
            self.tank_driver.on_for_seconds(
                left_speed=0,
                right_speed=-speed,
                seconds=1,
                brake=True,
                block=True)

            self.tank_driver.on_for_seconds(
                left_speed=speed,
                right_speed=0,
                seconds=1,
                brake=True,
                block=True)

        elif self.ir_sensor.top_right(channel=self.ir_beacon_channel) and self.ir_sensor.bottom_left(channel=self.ir_beacon_channel):
            # turn around right
            self.tank_driver.on_for_seconds(
                left_speed=-speed,
                right_speed=0,
                seconds=1,
                brake=True,
                block=True)

            self.tank_driver.on_for_seconds(
                left_speed=0,
                right_speed=speed,
                seconds=1,
                brake=True,
                block=True)

        elif self.ir_sensor.top_left(channel=self.ir_beacon_channel):
            # turn left
            self.tank_driver.on(
                left_speed=0,
                right_speed=-speed)

        elif self.ir_sensor.top_right(channel=self.ir_beacon_channel):
            # turn right
            self.tank_driver.on(
                left_speed=-speed,
                right_speed=0)

        elif self.ir_sensor.bottom_left(channel=self.ir_beacon_channel):
            # left backward
            self.tank_driver.on(
                left_speed=0,
                right_speed=speed)

        elif self.ir_sensor.bottom_right(channel=self.ir_beacon_channel):
            # right backward
            self.tank_driver.on(
                left_speed=speed,
                right_speed=0)

        else:
            self.tank_driver.off(brake=False)


    def shoot_objects_by_ir_beacon(self, channel: int = 1, speed: float = 1):
        if self.ir_sensor.beacon(channel=channel):
            self.shooting_motor.on_for_rotations(
                speed=speed,
                rotations=6,
                block=True,
                brake=True)

            while self.ir_sensor.beacon(channel=channel):
                pass

        else:
            self.shooting_motor.off(brake=False)


    def seek_the_fruit(self, distance: float = 10):
        if self.ir_sensor.proximity <= distance:
            self.speaker.play_file(
                wav_file='/home/robot/sound/Fanfare.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)


    def run_if_chased(self, speed: float = 100, how_many_steps: int = 3):
        if self.touch_sensor.is_pressed:
            # go forward
            for i in range(how_many_steps):
                self.tank_driver.on_for_seconds(
                    left_speed=-speed,
                    right_speed=0,
                    seconds=1,
                    brake=True,
                    block=True)

                self.tank_driver.on_for_seconds(
                    left_speed=0,
                    right_speed=-speed,
                    seconds=1,
                    brake=True,
                    block=True)


SUPER_TURTLE = SuperTurtle(left_leg_motor_port=OUTPUT_B,
                           right_leg_motor_port=OUTPUT_C,
                           shooting_motor_port=OUTPUT_A,
                           ir_sensor_port=INPUT_4,
                           touch_sensor_port=INPUT_1)

while True:
    SUPER_TURTLE.drive_by_ir_beacon(
        channel=1,
        speed=100)

    SUPER_TURTLE.shoot_objects_by_ir_beacon(
        channel=1,
        speed=100)

    SUPER_TURTLE.seek_the_fruit(distance=10)

    SUPER_TURTLE.run_if_chased(
        speed=100,
        how_many_steps=3)
