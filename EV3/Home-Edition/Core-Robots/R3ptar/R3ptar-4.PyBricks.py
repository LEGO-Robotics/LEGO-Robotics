#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop

from time import sleep


HUB = EV3Brick()

MEDIUM_MOTOR = Motor(port=Port.A,
                     positive_direction=Direction.CLOCKWISE)
TAIL_MOTOR = Motor(port=Port.B,
                   positive_direction=Direction.CLOCKWISE)
CHEST_MOTOR = Motor(port=Port.D,
                    positive_direction=Direction.CLOCKWISE)

IR_SENSOR = InfraredSensor(port=Port.S4)


def drive_once_by_ir_beacon(channel: int = 1, speed: float = 1000):
    ir_beacons_pressed = set(IR_SENSOR.buttons(channel=channel))

    if ir_beacons_pressed == {Button.LEFT_UP, Button.RIGHT_UP}:
        TAIL_MOTOR.run(speed=speed)

    elif ir_beacons_pressed == {Button.LEFT_DOWN, Button.RIGHT_DOWN}:
        TAIL_MOTOR.run(speed=-speed)

    elif ir_beacons_pressed == {Button.LEFT_UP}:
        MEDIUM_MOTOR.run(speed=-500)

        TAIL_MOTOR.run(speed=speed)

    elif ir_beacons_pressed == {Button.RIGHT_UP}:
        MEDIUM_MOTOR.run(speed=500)

        TAIL_MOTOR.run(speed=speed)

    elif ir_beacons_pressed == {Button.LEFT_DOWN}:
        MEDIUM_MOTOR.run(speed=-500)

        TAIL_MOTOR.run(speed=-speed)

    elif ir_beacons_pressed == {Button.RIGHT_DOWN}:
        MEDIUM_MOTOR.run(speed=500)

        TAIL_MOTOR.run(speed=-speed)

    else:
        MEDIUM_MOTOR.hold()

        TAIL_MOTOR.stop()


def bite_by_ir_beacon(channel: int = 1, speed: float = 1000):
    if Button.BEACON in IR_SENSOR.buttons(channel=channel):
        HUB.speaker.play_file(file=SoundFile.SNAKE_HISS)

        CHEST_MOTOR.run_time(
            speed=1000,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        CHEST_MOTOR.run_time(
            speed=-300,
            time=1000,
            then=Stop.COAST,
            wait=True)

        while Button.BEACON in IR_SENSOR.buttons(channel=channel):
            pass


while True:
    drive_once_by_ir_beacon(
        channel=1,
        speed=1000)

    bite_by_ir_beacon(
        channel=1,
        speed=1000)
