#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import ImageFile
from pybricks.parameters import Button, Direction, Port, Stop

from multiprocessing import Process


class Ev3rstorm(EV3Brick):
    WHEEL_DIAMETER = 26
    AXLE_TRACK = 102

    def __init__(
            self,
            left_leg_motor_port: Port = Port.B,
            right_leg_motor_port: Port = Port.C,
            shooting_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4,
            ir_beacon_channel: int = 1):
        super().__init__()

        self.driver = DriveBase(left_motor=Motor(port=left_leg_motor_port,
                                                 positive_direction=Direction.CLOCKWISE),
                                right_motor=Motor(port=right_leg_motor_port,
                                                  positive_direction=Direction.CLOCKWISE),
                                wheel_diameter=self.WHEEL_DIAMETER,
                                axle_track=self.AXLE_TRACK)

        self.shooting_motor = Motor(shooting_motor_port)

        self.touch_sensor = TouchSensor(touch_sensor_port)
        self.color_sensor = ColorSensor(color_sensor_port)

        self.ir_sensor = InfraredSensor(ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel

    # following method must be used in a parallel process in order not to block other operations
    def keep_driving_by_ir_beacon(self, speed: float = 100, turn_rate: float = 100):
        while True:
            ir_beacon_button_pressed = set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

            # go forward
            if ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
                self.driver.drive(
                    drive_speed=speed,
                    turn_rate=0)

            # go backward
            elif ir_beacon_button_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
                self.driver.drive(
                    drive_speed=-speed,
                    turn_rate=0)

            # turn left on the spot
            elif ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_DOWN}:
                self.driver.drive(
                    drive_speed=0,
                    turn_rate=-turn_rate)

            # turn right on the spot
            elif ir_beacon_button_pressed == {Button.RIGHT_UP, Button.LEFT_DOWN}:
                self.driver.drive(
                    drive_speed=0,
                    turn_rate=turn_rate)

            # turn left forward
            elif ir_beacon_button_pressed == {Button.LEFT_UP}:
                self.driver.drive(
                    drive_speed=speed,
                    turn_rate=-turn_rate)

            # turn right forward
            elif ir_beacon_button_pressed == {Button.RIGHT_UP}:
                self.driver.drive(
                    drive_speed=speed,
                    turn_rate=turn_rate)

            # turn left backward
            elif ir_beacon_button_pressed == {Button.LEFT_DOWN}:
                self.driver.drive(
                    drive_speed=-speed,
                    turn_rate=-turn_rate)

            # turn right backward
            elif ir_beacon_button_pressed == {Button.RIGHT_DOWN}:
                self.driver.drive(
                    drive_speed=-speed,
                    turn_rate=turn_rate)

            else:
                self.driver.stop()


    # following method must be used in a parallel process in order not to block other operations
    def shoot_whenever_touched(self):
        while True:
            
            # wait for TouchSensor being press
            while not self.touch_sensor.pressed():
                pass

            if self.color_sensor.ambient() < 15:
                self.speaker.play_file(filename='/home/robot/sound/Up.wav')

                self.shooting_motor.run_angle(
                    speed=100,
                    rotation_angle=3 * 360,
                    then=Stop.HOLD,
                    wait=True)

            else:
                self.speaker.play_file(filename='/home/robot/sound/Down.wav')

                self.shooting_motor.run_angle(
                    speed=100,
                    rotations=3 * 360,
                    then=Stop.HOLD,
                    wait=True)


    def main(self):
        Process(target=self.keep_driving_by_ir_beacon).start()
        Process(target=self.shoot_whenever_touched).start()


if __name__ == "__main__":
    EV3RSTORM = Ev3rstorm()
    EV3RSTORM.main()
