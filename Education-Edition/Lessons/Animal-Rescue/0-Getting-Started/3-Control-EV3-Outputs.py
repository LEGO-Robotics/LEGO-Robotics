#!/usr/bin/env python3
# (Display not yet working in MicroPython)


from ev3dev2.display import Display
from ev3dev2.led import Leds

from time import sleep


SCREEN = Display()
LEDS = Leds()


SCREEN.image_filename(
    filename='/home/robot/image/Hurt.bmp',
    clear_screen=True)

sleep(0.5)

SCREEN.image_filename(
    filename='/home/robot/image/Neutral.bmp',
    clear_screen=True)

LEDS.animate_flash(
    color='RED',
    groups=('LEFT', 'RIGHT'),
    sleeptime=0.5,
    duration=5,
    block=True)
