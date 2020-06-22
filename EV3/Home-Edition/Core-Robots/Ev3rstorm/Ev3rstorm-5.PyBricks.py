#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.parameters import Button, Color, Direction, Port, Stop


class Ev3rstorm(EV3Brick):
    WHEEL_DIAMETER = 26
    AXLE_TRACK = 102


    def __init__(
            self,
            left_foot_motor_port: Port = Port.B,
            right_foot_motor_port: Port = Port.C,
            shooting_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4,
            ir_beacon_channel: int = 1):
        self.driver = DriveBase(left_motor=Motor(port=left_foot_motor_port,
                                                 positive_direction=Direction.CLOCKWISE),
                                right_motor=Motor(port=right_foot_motor_port,
                                                  positive_direction=Direction.CLOCKWISE),
                                wheel_diameter=self.WHEEL_DIAMETER,
                                axle_track=self.AXLE_TRACK)
        self.driver.settings(
            straight_speed=300,
            straight_acceleration=300,
            turn_rate=90,
            turn_acceleration=90)

        self.shooting_motor = Motor(port=shooting_motor_port, 
                                    positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)

        self.ir_beacon_channel = ir_beacon_channel


    def drive_by_ir_beacon(self, speed: float = 100):
        ir_beacon_buttons_pressed = set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

        # forward
        if ir_beacon_buttons_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
            self.driver.drive(
                speed=speed,
                turn_rate=0)

        # backward
        elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.driver.drive(
                speed=-speed,
                turn_rate=0)

        # turn left on the spot
        elif ir_beacon_buttons_pressed == {Button.LEFT_UP, Button.RIGHT_DOWN}:
            self.driver.drive(
                speed=0,
                turn_rate=-90)

        # turn right on the spot
        elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN, Button.RIGHT_UP}:
            self.driver.drive(
                speed=0,
                turn_rate=90)

        # turn left forward
        elif ir_beacon_buttons_pressed == {Button.LEFT_UP}:
            self.driver.drive(
                speed=speed,
                turn_rate=-90)

        # turn right forward
        elif ir_beacon_buttons_pressed == {Button.RIGHT_UP}:
            self.driver.drive(
                speed=speed,
                turn_rate=90)

        # turn left backward
        elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN}:
            self.driver.drive(
                speed=-speed,
                turn_rate=90)

        # turn right backward
        elif ir_beacon_buttons_pressed == {Button.RIGHT_DOWN}:
            self.driver.drive(
                speed=-speed,
                turn_rate=-90)

        # otherwise stop
        else:
            self.driver.stop()


    def shoot_when_touched(self):
        if self.touch_sensor.pressed():
            if self.color_sensor.ambient() <= 15:
                self.speaker.play_file(file=SoundFile.UP)
                    
                self.shooting_motor.run_angle(
                    speed=100,
                    rotation_angle=-3 * 360,
                    then=Stop.HOLD,
                    wait=True)

            else:
                self.speaker.play_file(file=SoundFile.DOWN)
                    
                self.shooting_motor.run_angle(
                    speed=100,
                    rotation_angle=3 * 360,
                    then=Stop.HOLD,
                    wait=True)
 

    def main(self):
        self.screen.load_image(ImageFile.TARGET)
    
        while True:
            self.drive_by_ir_beacon()
            
            self.shoot_when_touched()


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()
