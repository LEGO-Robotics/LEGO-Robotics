#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop

from time import sleep


class R3ptar(EV3Brick):
    def __init__(
            self,
            turn_motor_port: Port = Port.A,
            move_motor_port: Port = Port.B,
            scare_motor_port: Port = Port.D,
            touch_sensor_port: Port = Port.S1, color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1):
        self.turn_motor = Motor(port=turn_motor_port,
                                positive_direction=Direction.CLOCKWISE)
        self.move_motor = Motor(port=move_motor_port,
                                positive_direction=Direction.CLOCKWISE)
        self.scare_motor = Motor(port=scare_motor_port,
                                 positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)
        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_sensor = InfraredSensor(port=ir_sensor_port)
        self.ir_beacon_channel = ir_beacon_channel


    def drive_once_by_ir_beacon(self, speed: float = 1000):
        ir_beacons_pressed = set(self.ir_sensor.buttons(channel=self.ir_beacon_channel))

        if ir_beacons_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
            self.move_motor.run(speed=speed)

        elif ir_beacons_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
            self.move_motor.run(speed=-speed)

        elif ir_beacons_pressed == {Button.LEFT_UP}:
            self.turn_motor.run(speed=-500)

            self.move_motor.run(speed=speed)

        elif ir_beacons_pressed == {Button.RIGHT_UP}:
            self.turn_motor.run(speed=500)

            self.move_motor.run(speed=speed)

        elif ir_beacons_pressed == {Button.LEFT_DOWN}:
            self.turn_motor.run(speed=-500)

            self.move_motor.run(speed=-speed)

        elif ir_beacons_pressed == {Button.RIGHT_DOWN}:
            self.turn_motor.run(speed=500)

            self.move_motor.run(speed=-speed)

        else:
            self.turn_motor.hold()

            self.move_motor.stop()


    def bite_by_ir_beacon(self, speed: float = 1000):
        if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.speaker.play_file(file=SoundFile.SNAKE_HISS)

            self.scare_motor.run_time(
                speed=speed,
                time=1000,
                then=Stop.HOLD,
                wait=True)

            self.scare_motor.run_time(
                speed=-300,
                time=1000,
                then=Stop.COAST,
                wait=True)

            while Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                pass


    def run_away_if_chased(self):
        if self.color_sensor.reflection() > 30:
            self.move_motor.run_time(
                speed=500,
                time=4000,
                then=Stop.HOLD,
                wait=True)

            for i in range(2):
                self.turn_motor.run_time(
                    speed=500,
                    time=1000,
                    then=Stop.HOLD,
                    wait=True)

                self.turn_motor.run_time(
                    speed=-500,
                    time=1000,
                    then=Stop.HOLD,
                    wait=True)


    def bite_if_touched(self):
        if self.touch_sensor.pressed():
            self.speaker.play_file(file=SoundFile.SNAKE_HISS)

            self.scare_motor.run_time(
                speed=1000,
                time=1000,
                then=Stop.HOLD,
                wait=True)

            self.scare_motor.run_time(
                speed=-300,
                time=1000,
                then=Stop.COAST,
                wait=True)


    def main(self, speed: float = 1000):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

            self.bite_by_ir_beacon(speed=speed)

            self.bite_if_touched()
                
            self.run_away_if_chased()


if __name__ == '__main__':
    R3PTAR = R3ptar()
        
    R3PTAR.main(speed=1000)
