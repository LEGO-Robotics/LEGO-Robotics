#!/usr/bin/env micropython


from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.led import Leds


IR_SENSOR = InfraredSensor(address=INPUT_4)

LEDS = Leds()


def detect_object(
        distance: float = 30,
        flashing_color = Leds.RED,
        flashing_duration: float = 2):
    if IR_SENSOR.proximity <= distance:
        LEDS.animate_flash(
            color=flashing_color,
            sleeptime=0.5,
            duration=flashing_duration,
            block=True)

    else:
        LEDS.all_off()

 
while True:
    detect_object(
        distance=10,
        flashing_color=Leds.AMBER,
        flashing_duration=4.2)
