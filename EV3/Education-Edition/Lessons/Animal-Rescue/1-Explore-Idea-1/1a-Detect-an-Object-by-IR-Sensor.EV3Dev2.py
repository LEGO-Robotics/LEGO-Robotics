#!/usr/bin/env micropython


from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.led import Leds


IR_SENSOR = InfraredSensor(address=INPUT_4)

LEDS = Leds()


while IR_SENSOR.proximity >= 30:
    pass

LEDS.animate_flash(
    color=Leds.RED,
    sleeptime=0.5,
    duration=2.0,
    block=True)
