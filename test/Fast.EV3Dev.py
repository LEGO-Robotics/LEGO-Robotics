#!/usr/bin/env micropython


# import os
# import sys
# sys.path.append(os.path.expanduser('~'))
from util.ev3dev_fast.ev3fast import (   
    Motor, LargeMotor, MediumMotor,
    MotorSet, MoveTank, MoveSteering,
    SpeedValue, SpeedPercent, SpeedNativeUnits,
    SpeedRPS, SpeedRPM, SpeedDPS, SpeedDPM,
    Sensor, TouchSensor, ColorSensor, UltrasonicSensor, GyroSensor
)
