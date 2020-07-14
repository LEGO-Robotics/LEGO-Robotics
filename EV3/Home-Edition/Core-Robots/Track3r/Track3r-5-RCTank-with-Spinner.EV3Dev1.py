#!/usr/bin/env python3


from track3r_rc_tank_ev3dev1 import Track3r


class Track3rWithSpinner(Track3r):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            medium_motor_port=medium_motor_port)
        
        self.remote.on_beacon = self.spinner


    def spin(self, state):
        if state:
            self.medium_motor.run_forever(speed_sp=50)

        else:
            self.medium_motor.stop()

    
if __name__ == '__main__':
    TRACK3R_WITH_SPINNER = Track3rWithSpinner()

    TRACK3R_WITH_SPINNER.main()
