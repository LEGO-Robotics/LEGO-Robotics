#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Direction, Port, Stop


MEDIUM_MOTOR = Motor(port=Port.A,
                     positive_direction=Direction.CLOCKWISE)

IR_SENSOR = InfraredSensor(port=Port.S4)

EV3_BRICK = EV3Brick()


is_gripping = False

MEDIUM_MOTOR.run_time(
    speed=500,
    time=1000,
    then=Stop.HOLD,
    wait=True)


while True:
    if Button.BEACON in IR_SENSOR.buttons(channel=1):
        if is_gripping:
            MEDIUM_MOTOR.run_time(
                speed=1000,
                time=2000,
                then=Stop.HOLD,
                wait=True)

            EV3_BRICK.speaker.play_file(file=SoundFile.AIR_RELEASE)

            is_gripping = False

        else:
            MEDIUM_MOTOR.run_time(
                speed=-1000,
                time=2000,
                then=Stop.HOLD,
                wait=True)

            EV3_BRICK.speaker.play_file(file=SoundFile.AIRBRAKE)

            is_gripping = True

        while Button.BEACON in IR_SENSOR.buttons(channel=1):
            pass
