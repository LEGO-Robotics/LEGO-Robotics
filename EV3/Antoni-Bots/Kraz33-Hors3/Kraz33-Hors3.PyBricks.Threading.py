#!/usr/bin/env pybricks-micropython


from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.parameters import Button, Direction, Port, Stop

from threading import Thread


class Kraz33Hors3:
    def __init__(
            self,
            back_foot_motor_port: Port = Port.C, front_foot_motor_port: Port = Port.B,
            gear_motor_port: Port = Port.A,
            touch_sensor_port: Port = Port.S1, color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        self.front_foot_motor = Motor(port=front_foot_motor_port,
                                      positive_direction=Direction.CLOCKWISE)
        self.back_foot_motor = Motor(port=back_foot_motor_port,
                                     positive_direction=Direction.COUNTERCLOCKWISE)

        self.gear_motor = Motor(port=gear_motor_port)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)
        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel


    def drive_once_by_ir_beacon(
            self,
            speed: float = 1000   # deg/s
        ):
        ir_beacons_pressed = set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

        # forward
        if ir_beacons_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
            self.front_foot_motor.run_time(
                speed=speed,
                time=1000,   # ms
                then=Stop.COAST,
                wait=False)

            self.back_foot_motor.run_time(
                speed=speed,
                time=1000,   # ms
                then=Stop.COAST,
                wait=True)

        # backward
        elif ir_beacons_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.front_foot_motor.run_time(
                speed=-speed,
                time=1000,   # ms
                then=Stop.COAST,
                wait=False)

            self.back_foot_motor.run_time(
                speed=-speed,
                time=1000,   # ms
                then=Stop.COAST,
                wait=True)

        # move crazily
        elif ir_beacons_pressed == {Button.BEACON}:
            self.front_foot_motor.run_time(
                speed=speed / 3,
                time=1000,   # ms
                then=Stop.COAST,
                wait=False)

            self.back_foot_motor.run_time(
                speed=-speed / 3,
                time=1000,   # ms
                then=Stop.COAST,
                wait=True)

    def keep_driving_by_ir_beacon(
            self,
            speed: float = 1000   # deg/s
        ):
        while True: 
            self.drive_once_by_ir_beacon(speed=speed)


    def back_whenever_touched(
            self,
            speed: float = 1000   # deg/s
        ):
        while True:
            if self.touch_sensor.pressed():
                self.front_foot_motor.run_time(
                    speed=-speed,
                    time=1000,   # ms
                    then=Stop.COAST,
                    wait=False)

                self.back_foot_motor.run_time(
                    speed=-speed,
                    time=1000,   # ms
                    then=Stop.COAST,
                    wait=True)


    def main(self,
             speed: float = 1000   # deg/s
            ):
        Thread(target=self.back_whenever_touched).start()    

        self.keep_driving_by_ir_beacon(speed=speed)


if __name__ == '__main__':
    KRAZ33_HORS3 = Kraz33Hors3()
    
    KRAZ33_HORS3.main()
