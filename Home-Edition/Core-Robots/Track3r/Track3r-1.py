#!/usr/bin/env python3
# (MicroPython does not yet support Display)


from ev3dev2.motor import LargeMotor
from ev3dev2.display import Display


SCREEN = Display()


SCREEN.image_filename(
    filename='/home/robot/image/Pinch left.bmp',
    clear_screen=True,
    x1=0, y1=0,
    # x2=177, y2=127   # ref: https://sites.google.com/site/ev3python/learn_ev3_python/screen
       # commented out because of ValueError: images do not match
)
