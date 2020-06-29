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
            left_foot_motor_port: Port = Port.B, right_foot_motor_port: Port = Port.C,
            shooting_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1, color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        self.drive_base = DriveBase(left_motor=Motor(port=left_foot_motor_port,
                                                     positive_direction=Direction.CLOCKWISE),
                                    right_motor=Motor(port=right_foot_motor_port,
                                                      positive_direction=Direction.CLOCKWISE),
                                    wheel_diameter=self.WHEEL_DIAMETER,
                                    axle_track=self.AXLE_TRACK)
        self.drive_base.settings(
            straight_speed=300,   # milimeters per second
            straight_acceleration=300,
            turn_rate=90,   # degrees per second
            turn_acceleration=90)

        self.shooting_motor = Motor(port=shooting_motor_port, 
                                    positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)
        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel


    def drive_once_by_ir_beacon(
            self,
            speed: float = 1000   # milimeters per second
        ):
        ir_beacon_buttons_pressed = set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

        # forward
        if ir_beacon_buttons_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
            self.drive_base.drive(
                speed=speed,
                turn_rate=0   # degrees per second
            )

        # backward
        elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.drive_base.drive(
                speed=-speed,
                turn_rate=0   # degrees per second
            )

        # turn left on the spot
        elif ir_beacon_buttons_pressed == {Button.LEFT_UP, Button.RIGHT_DOWN}:
            self.drive_base.drive(
                speed=0,
                turn_rate=-90   # degrees per second
            )

        # turn right on the spot
        elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN, Button.RIGHT_UP}:
            self.drive_base.drive(
                speed=0,
                turn_rate=90   # degrees per second
            )

        # turn left forward
        elif ir_beacon_buttons_pressed == {Button.LEFT_UP}:
            self.drive_base.drive(
                speed=speed,
                turn_rate=-90   # degrees per second
            )

        # turn right forward
        elif ir_beacon_buttons_pressed == {Button.RIGHT_UP}:
            self.drive_base.drive(
                speed=speed,
                turn_rate=90   # degrees per second
            )

        # turn left backward
        elif ir_beacon_buttons_pressed == {Button.LEFT_DOWN}:
            self.drive_base.drive(
                speed=-speed,
                turn_rate=90   # degrees per second
            )

        # turn right backward
        elif ir_beacon_buttons_pressed == {Button.RIGHT_DOWN}:
            self.drive_base.drive(
                speed=-speed,
                turn_rate=-90   # degrees per second
            )

        # otherwise stop
        else:
            self.drive_base.stop()


    def shoot_when_touched(self):
        if self.touch_sensor.pressed():
            if self.color_sensor.ambient() < 5:   # 15 not dark enough
                self.speaker.play_file(file=SoundFile.UP)
                    
                self.shooting_motor.run_angle(
                    speed=1000,   # degrees per second
                    rotation_angle=-3 * 360,   # degrees
                    then=Stop.HOLD,
                    wait=True)

            else:
                self.speaker.play_file(file=SoundFile.DOWN)
                    
                self.shooting_motor.run_angle(
                    speed=1000,   # degrees per second
                    rotation_angle=3 * 360,   # degrees
                    then=Stop.HOLD,
                    wait=True)
 

    def main(self,
             driving_speed: float = 1000   # mm/s
            ):
        self.screen.load_image(ImageFile.TARGET)
    
        while True:
            self.drive_once_by_ir_beacon(speed=driving_speed)
            
            self.shoot_when_touched()


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()

    EV3RSTORM.main()
