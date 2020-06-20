#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import ImageFile
from pybricks.parameters import Button, Direction, Port, Stop


class IRBeaconDriverMixin:
    def __init__(
            self,
            left_motor_port: Port = Port.B,
            right_motor_port: Port = Port.C,
            ir_sensor_port: Port = Port.S4,
            ir_beacon_channel: int = 1):
        self.driver = DriveBase(left_motor=Motor(port=left_motor_port,
                                                 positive_direction=Direction.CLOCKWISE),
                                right_motor=Motor(port=right_motor_port,
                                                  positive_direction=Direction.CLOCKWISE),
                                wheel_diameter=self.WHEEL_DIAMETER,
                                axle_track=self.AXLE_TRACK)

        self.ir_sensor = InfraredSensor(ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel
    
    def drive_by_ir_beacon(
            self,
            speed: float = 100,     # mm/s
            turn_rate: float = 90   # rotational speed deg/s
        ):
        ir_beacon_button_pressed = set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

        # forward
        if ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
            self.driver.drive(
                speed=speed,
                turn_rate=0)

        # backward
        elif ir_beacon_button_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.driver.drive(
                speed=-speed,
                turn_rate=0)

        # turn left on the spot
        elif ir_beacon_button_pressed == {Button.LEFT_UP, Button.RIGHT_DOWN}:
            self.driver.drive(
                speed=0,
                turn_rate=-turn_rate)

        # turn right on the spot
        elif ir_beacon_button_pressed == {Button.RIGHT_UP, Button.LEFT_DOWN}:
            self.driver.drive(
                speed=0,
                turn_rate=turn_rate)

        # turn left forward
        elif ir_beacon_button_pressed == {Button.LEFT_UP}:
            self.driver.drive(
                speed=speed,
                turn_rate=-turn_rate)

        # turn right forward
        elif ir_beacon_button_pressed == {Button.RIGHT_UP}:
            self.driver.drive(
                speed=speed,
                turn_rate=turn_rate)

        # turn left backward
        elif ir_beacon_button_pressed == {Button.LEFT_DOWN}:
            self.driver.drive(
                speed=-speed,
                turn_rate=turn_rate)

        # turn right backward
        elif ir_beacon_button_pressed == {Button.RIGHT_DOWN}:
            self.driver.drive(
                speed=-speed,
                turn_rate=-turn_rate)

        # stop
        else:
            self.driver.stop()


class Ev3rstorm(EV3Brick, IRBeaconDriverMixin):
    WHEEL_DIAMETER = 26
    AXLE_TRACK = 102

    def __init__(
            self,
            left_motor_port: Port = Port.B,
            right_motor_port: Port = Port.C,
            shooting_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1,
            color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4,
            ir_beacon_channel: int = 1):
        super().__init__()

        IRBeaconDriverMixin.__init__(
            self,
            left_motor_port=left_motor_port,
            right_motor_port=right_motor_port,
            ir_sensor_port=ir_sensor_port,
            ir_beacon_channel=ir_beacon_channel)
        
        self.shooting_motor = Motor(port=shooting_motor_port,
                                    positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(touch_sensor_port)
        self.color_sensor = ColorSensor(color_sensor_port)

    def shoot_if_touched(self):
        N_ROTATIONS_PER_SHOT = 3
        ROTATIONAL_DEGREES_PER_SHOT = N_ROTATIONS_PER_SHOT * 360

        if self.touch_sensor.pressed():
            if self.color_sensor.ambient() < 15:
                self.speaker.play_file(file='/home/robot/sound/Up.wav')

                self.shooting_motor.run_angle(
                    speed=2 * ROTATIONAL_DEGREES_PER_SHOT,   # shoot quickly in half a second
                    rotation_angle=ROTATIONAL_DEGREES_PER_SHOT,
                    then=Stop.HOLD,
                    wait=True)

            else:
                self.speaker.play_file(file='/home/robot/sound/Down.wav')

                self.shooting_motor.run_angle(
                    speed=2 * ROTATIONAL_DEGREES_PER_SHOT,   # shoot quickly in half a second
                    rotation_angle=-ROTATIONAL_DEGREES_PER_SHOT,
                    then=Stop.HOLD,
                    wait=True)


    def main(self):
        while True:
            self.drive_by_ir_beacon()
            self.shoot_if_touched()


if __name__ == '__main__':
    EV3RSTORM = Ev3rstorm()
    EV3RSTORM.main()
