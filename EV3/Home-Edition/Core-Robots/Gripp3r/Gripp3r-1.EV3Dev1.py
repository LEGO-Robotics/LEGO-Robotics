#!/usr/bin/env python3


from ev3dev.ev3 import (
    MediumMotor, OUTPUT_A,
    Sound
)

from time import sleep


MEDIUM_MOTOR = MediumMotor(address=OUTPUT_A)
SPEAKER = Sound()


