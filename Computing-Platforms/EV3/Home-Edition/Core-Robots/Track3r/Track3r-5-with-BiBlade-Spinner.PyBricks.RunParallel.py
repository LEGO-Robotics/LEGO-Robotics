#!/usr/bin/env pybricks-micropython



from pybricks.parameters import Button, Stop

from track3r_pybricks import Track3r

from threading import Thread

from pybricks.experimental import run_parallel


class Track3rWithBiBladeSpinner(Track3r):
    def spin_blade_by_ir_beacon(
            self,
            speed: float = 1000   # deg/s
        ):
        while True:
            if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                self.medium_motor.run(speed=speed)

            else:
                self.medium_motor.stop()

            
    def main(self, speed: float = 1000):
        run_parallel(
            self.spin_blade_by_ir_beacon,
            self.keep_driving_by_ir_beacon)        
           
           
if __name__ == '__main__':
    TRACKER_WITH_BIBLADE_SPINNER = Track3rWithBiBladeSpinner()

    TRACKER_WITH_BIBLADE_SPINNER.main()
