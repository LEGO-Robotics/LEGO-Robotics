#!/usr/bin/env python3


from ev3dev.ev3 import InfraredSensor, BeaconSeeker, INPUT_4, Screen

from time import sleep

from util.ir_beacon_util_ev3dev1 import ir_beacon_measurements_reliable


BEACON_SEEKER = BeaconSeeker(sensor=InfraredSensor(address=INPUT_4),
                             channel=1)
SCREEN = Screen()

while True:
    heading, distance = BEACON_SEEKER.heading_and_distance

    SCREEN.clear()
    SCREEN.draw.text(
        xy=(0, 0),
        text='HA={}, D={}'.format(heading, distance)
             if ir_beacon_measurements_reliable(heading_angle=heading,
                                                distance=distance)
             else 'x HA={}, D={}'.format(heading, distance),
        fill=None,
        font=None,
        anchor=None,
        spacing=4,
        align='center',
        direction=None,
        features=None,
        language=None,
        stroke_width=0,
        stroke_fill=None)
    SCREEN.update()

    sleep(0.3)
