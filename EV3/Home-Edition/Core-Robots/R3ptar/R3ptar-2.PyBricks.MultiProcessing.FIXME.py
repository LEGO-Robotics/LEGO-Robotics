#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor    
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Direction, Port, Stop  

from multiprocessing import Process
from time import sleep


BRICK = EV3Brick()

LARGE_MOTOR = Motor(port=Port.D,
                    positive_direction=Direction.CLOCKWISE)
MEDIUM_MOTOR = Motor(port=Port.A,
                     positive_direction=Direction.CLOCKWISE)

IR_SENSOR = InfraredSensor(port=Port.S4)


def rattle():
    while True:
        MEDIUM_MOTOR.run_time(
            speed=100,
            time=1000,
            then=Stop.COAST,
            wait=True)
            
        BRICK.speaker.play_file(file=SoundFile.SNAKE_RATTLE)

        MEDIUM_MOTOR.run_time(
            speed=-100,
            time=1000,
            then=Stop.COAST,
            wait=True)

        sleep(1)


def scare_people():
    while True:
        if IR_SENSOR.distance() < 30:
            LARGE_MOTOR.run_time(
                speed=1000,
                time=1000,
                then=Stop.COAST,
                wait=True)

        else:
            LARGE_MOTOR.run_time(
                speed=-300,
                time=1000,
                then=Stop.COAST,
                wait=True)


Process(target=scare_people).start()

rattle()

# FIXME: OSError: [Errno 5] EIO: 
# Unexpected hardware input/output error with a motor or sensor:
# --> Try unplugging the sensor or motor and plug it back in again.
# --> To see which sensor or motor is causing the problem,
#     check the line in your script that matches
#     the line number given in the 'Traceback' above.
# --> Try rebooting the hub/brick if the problem persists.
#
# OR
#
# scare_people() Process dies / becomes non-responsive
