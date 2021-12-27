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
drive_l = Motor(Port.B)
drive_r = Motor(Port.C)

# Auto center steering wheels.
steer_motor.run_until_stalled(250)
steer_motor.reset_angle(80)
steer_motor.run_target(300,0)

speed = 0
left = 0

# Now you can simply read values!
while True:
    steer_motor.track_target(wheel.steering() * -0.5 + wheel.right_thumb())

    if wheel.left_paddle() > 15:
        speed = wheel.left_paddle() * -10
    else:
        speed = wheel.right_paddle() * 10

    drive_l.dc(speed)
    drive_r.dc(speed)
