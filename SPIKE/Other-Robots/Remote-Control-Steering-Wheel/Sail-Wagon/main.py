#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

from math import sin, radians, pi, atan2, degrees
from connection import SpikePrimeStreamReader, SpikeRCWheel

# Create the connection. See README.md to find the address for your SPIKE hub.
wheel = SpikeRCWheel('38:0B:3C:A3:45:0D')

steer_motor = Motor(Port.A)


sheet_motor = Motor(Port.D)


sheet_spd = 0
left = 0
sheet_pos = 0

# Now you can simply read values!
while True:
    steer_motor.track_target(wheel.steering() * -1 + wheel.right_thumb())

    if wheel.left_paddle() > 15:
        sheet_spd = wheel.left_paddle() * -10
    else:
        sheet_spd = wheel.right_paddle() * 10

    sheet_motor.run(sheet_spd)
