#!/usr/bin/env python3


__all__ = 'Track3r',


from ev3dev2.motor import Motor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.control.rc_tank import RemoteControlledTank


class Track3r(RemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity=Motor.POLARITY_NORMAL,
            speed=1000,
            channel=1)

        self.medium_motor = MediumMotor(address=medium_motor_port)


if __name__ == '__main__':
    TRACK3R = Track3r()

    TRACK3R.main()
