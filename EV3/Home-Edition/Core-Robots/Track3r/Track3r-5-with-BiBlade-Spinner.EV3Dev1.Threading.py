#!/usr/bin/env python3


from ev3dev.ev3 import Motor

from threading import Thread

from track3r_ev3dev1 import Track3r


class Track3rWithBiBladeSpinner(Track3r):
    def spin_blade_by_ir_beacon(
            self,
            speed: float = 1000   # deg/s
        ):
        while True:
            if self.remote_control.beacon:
                self.medium_motor.run_forever(speed_sp=speed)

            else:
                self.medium_motor.stop(stop_action=Motor.STOP_ACTION_COAST)

    def main(self,
             speed: float = 1000   # deg/s
            ):
        Thread(target=self.spin_blade_by_ir_beacon,
               daemon=True).start()
            
        self.keep_driving_by_ir_beacon(speed=speed)

           
if __name__ == '__main__':
    TRACKER_WITH_BIBLADE_SPINNER = Track3rWithBiBladeSpinner()

    TRACKER_WITH_BIBLADE_SPINNER.main()
