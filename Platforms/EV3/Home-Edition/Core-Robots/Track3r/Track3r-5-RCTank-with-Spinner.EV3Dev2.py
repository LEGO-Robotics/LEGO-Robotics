#!/usr/bin/env python3


from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C

from track3r_rc_tank_ev3dev2 import Track3r


class Track3rWithSpinner(Track3r):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            medium_motor_port=medium_motor_port)
        
        self.remote.on_channel1_beacon = self.spin


    def spin(self, state):
        if state:
            self.medium_motor.run_forever(speed_sp=50)

        else:
            self.medium_motor.stop()

    
if __name__ == '__main__':
    TRACK3R_WITH_SPINNER = Track3rWithSpinner()

    TRACK3R_WITH_SPINNER.main()
