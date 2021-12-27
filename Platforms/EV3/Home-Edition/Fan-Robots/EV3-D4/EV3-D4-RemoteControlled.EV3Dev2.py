#!/usr/bin/env python3


from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.control.rc_tank import RemoteControlledTank


class EV3D4RemoteControlled(RemoteControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A,
            speed: float = 400,
            ir_beacon_channel: int = 1):
        super().__init__(
            left_motor=left_motor_port, right_motor=right_motor_port,
            polarity='inversed',
            speed=speed,
            channel=ir_beacon_channel)
            
        self.medium_motor = MediumMotor(address=medium_motor_port)
        self.medium_motor.reset()


if __name__ == '__main__':
    EV3D4_REMOTE_CONTROLLED = EV3D4RemoteControlled()
    
    EV3D4_REMOTE_CONTROLLED.main()
