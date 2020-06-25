#!/usr/bin/env python3


import subprocess
import termios, tty, sys
from ev3dev.ev3 import *


motor_left = LargeMotor('outC')
motor_right = LargeMotor('outB')
motor_a = MediumMotor('outA')


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    return ch


def cabezaderecha():
   motor_a.run_forever(speed_sp=450)


def cabezaizquierda():
   motor_a.run_forever(speed_sp=-450)


def marchaimp():
   subprocess.call(['python3', 'marchaImperial'])   


def fire():
   motor_a.run_timed(time_sp=3000, speed_sp=600)


def forward():
   motor_left.run_forever(speed_sp=450)
   motor_right.run_forever(speed_sp=450)


def back():
   motor_left.run_forever(speed_sp=-450)
   motor_right.run_forever(speed_sp=-450)


def left():
   motor_left.run_forever(speed_sp=-450)
   motor_right.run_forever(speed_sp=450)


def right():
   motor_left.run_forever(speed_sp=450)
   motor_right.run_forever(speed_sp=-450)


def stop():
   motor_left.run_forever(speed_sp=0)
   motor_right.run_forever(speed_sp=0)
   motor_a.run_forever(speed_sp=0)


while True:
   k = getch()
   print(k)
   if k == 'm':
     marchaimp()
   if k == 'g':
      cabezaderecha()
   if k == 'h':  
      cabezaizquierda()
   if k == 's':
      forward()
   if k == 'w':
      back()
   if k == 'd':
      right()
   if k == 'a':
      left()
   if k == ' ':
      stop()
   if k == 'q':
      exit()
