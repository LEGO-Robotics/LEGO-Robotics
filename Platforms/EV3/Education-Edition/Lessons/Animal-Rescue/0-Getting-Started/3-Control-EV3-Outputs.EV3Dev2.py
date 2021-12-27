#!/usr/bin/env python3
# (Display not yet working in MicroPython as of 2020)


from ev3dev2.display import Display
from ev3dev2.led import Leds

from time import sleep


SCREEN = Display()
LEDS = Leds()


SCREEN.image_filename(
    filename='/home/robot/image/Hurt.bmp',
    clear_screen=True)
SCREEN.update()

sleep(0.5)

SCREEN.image_filename(
    filename='/home/robot/image/Neutral.bmp',
    clear_screen=True)
SCREEN.update()

LEDS.animate_flash(
    color=Leds.RED,
    groups=(Leds.LEFT, Leds.RIGHT),
    sleeptime=0.5,
    duration=5,
    block=True)
