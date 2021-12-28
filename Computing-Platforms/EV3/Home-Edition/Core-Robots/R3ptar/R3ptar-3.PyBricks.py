#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Color, Direction, Port, Stop

from random import randint
from time import sleep


BRICK = EV3Brick()

MEDIUM_MOTOR = Motor(port=Port.A,
                     positive_direction=Direction.CLOCKWISE)
TAIL_MOTOR = Motor(port=Port.B,
                   positive_direction=Direction.CLOCKWISE)
CHEST_MOTOR = Motor(port=Port.D,
                    positive_direction=Direction.CLOCKWISE)

IR_SENSOR = InfraredSensor(port=Port.S4)


CHEST_MOTOR.run_time(
    speed=-300,
    time=1000,
    then=Stop.HOLD,
    wait=True)

while True:
    if IR_SENSOR.distance() < 30:
        BRICK.light.on(color=Color.RED)

        MEDIUM_MOTOR.stop()

        TAIL_MOTOR.stop()

        BRICK.speaker.play_file(file=SoundFile.SNAKE_HISS)

        CHEST_MOTOR.run_time(
            speed=1000,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        MEDIUM_MOTOR.run(speed=1000)

        TAIL_MOTOR.run(speed=-1000)

        CHEST_MOTOR.run_time(
            speed=-300,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        sleep(2)

        MEDIUM_MOTOR.run_time(
            speed=-1000,
            time=1000,
            then=Stop.HOLD,
            wait=True)

        sleep(1)

    else:
        BRICK.light.on(color=Color.ORANGE)

        TAIL_MOTOR.run(speed=1000)

        MEDIUM_MOTOR.run_time(
            speed=randint(-30, 30),
            time=0.2 * 1000,
            then=Stop.COAST,
            wait=True) 
