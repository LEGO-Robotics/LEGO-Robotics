#!/usr/bin/env python3


__all__ = 'Track3r',


from ev3dev.ev3 import Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev.helper import RemoteControlledTank


class Track3r(RemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A):
        super().__init__(
            left_motor=left_motor_port, right_motor=right_motor_port,
            polarity=Motor.POLARITY_NORMAL)
            
        self.medium_motor = MediumMotor(address=medium_motor_port)


if __name__ == '__main__':
    TRACK3R = Track3r()

    TRACK3R.main()
