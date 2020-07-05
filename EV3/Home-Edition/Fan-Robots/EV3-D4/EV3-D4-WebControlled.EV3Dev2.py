#!/usr/bin/env python3


from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.control.webserver import WebControlledTank


class EV3D4WebControlled(WebControlledTank):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A,
            speed: float = 400,
            ir_beacon_channel: int = 1):
        super().__init__(self,
            left_motor=left_motor_port, right_motor=right_motor_port,
            port_number=8000,
            motor_class=LargeMotor)

        self.medium_motor = MediumMotor(address=medium_motor)
        self.medium_motor.reset()


if __name__ == '__main__':
    EV3D4_WEB_CONTROLLED = EV3D4WebControlled()
    
    EV3D4_WEB_CONTROLLED.main()
