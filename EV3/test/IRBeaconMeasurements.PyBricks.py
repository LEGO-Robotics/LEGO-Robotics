#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import InfraredSensor
from pybricks.parameters import Port
from pybricks.tools import wait

from util.ir_beacon_util_pybricks import ir_beacon_measurements_reliable


EV3_BRICK = EV3Brick()
IR_SENSOR = InfraredSensor(port=Port.S4)

while True:
    distance, angle = IR_SENSOR.beacon(channel=1)
    reliable = ir_beacon_measurements_reliable(heading_angle=angle,
                                               distance=distance)

    EV3_BRICK.screen.clear()
    EV3_BRICK.screen.print(
        'HA={}, D={}'.format(angle, distance)
        if reliable
        else 'x HA={}, D={}'.format(angle, distance))

    wait(300)
