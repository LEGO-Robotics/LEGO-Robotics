#!/usr/bin/env python3


from ev3dev.ev3 import MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev.helper import RemoteControlledTank


class EV3D4RemoteControlled(RemoteControlledTank):
    """
    Base class for all Track3r variations.
    The only difference in the child classes are in how the medium motor is handled.
    To enable the medium motor toggle the beacon button on the EV3 remote.
    """
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A):
        super().__init__(
            left_motor=left_motor_port, right_motor=right_motor_port,
            polarity='inversed')
            
        self.medium_motor = MediumMotor(address=medium_motor_port)
        self.medium_motor.reset()


if __name__ == '__main__':
    EV3D4_REMOTE_CONTROLLED = EV3D4RemoteControlled()
    
    EV3D4_REMOTE_CONTROLLED.main()
