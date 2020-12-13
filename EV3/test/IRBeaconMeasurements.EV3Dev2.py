#!/usr/bin/env micropython


from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.console import Console

from time import sleep

from util.ir_beacon_util_ev3dev2 import ir_beacon_measurements_reliable


IR_SENSOR = InfraredSensor(address=INPUT_4)
CONSOLE = Console()

while True:
    heading, distance = IR_SENSOR.heading_and_distance(channel=1)

    CONSOLE.text_at(
        text='HA={}, D={}'.format(heading, distance)
             if ir_beacon_measurements_reliable(heading_angle=heading,
                                                distance=distance)
             else 'x HA={}, D={}'.format(heading, distance),
        column=1, row=1,
        reset_console=True,
        inverse=False,
        alignment='L')

    sleep(0.3)
