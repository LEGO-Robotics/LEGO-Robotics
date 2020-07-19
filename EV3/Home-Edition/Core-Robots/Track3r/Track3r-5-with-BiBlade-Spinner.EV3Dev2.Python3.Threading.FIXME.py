#!/usr/bin/env python3
# (MicroPython does not yet support Display as of May 2020)


from threading import Thread

from track3r_ev3dev2 import Track3r


class Track3rWithBiBladeSpinner(Track3r):
    def spin_blade_by_ir_beacon(self, speed: float = 100):
        while True:
            if self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                self.medium_motor.on(
                    speed=speed,
                    block=False,
                    brake=False)

            else:
                self.medium_motor.off(brake=False)


    def main(self, speed: float = 100):
        Thread(target=self.spin_blade_by_ir_beacon,
               daemon=True).start()

        self.keep_driving_by_ir_beacon(speed=speed)

            
if __name__ == '__main__':
    TRACKER_WITH_BIBLADE_SPINNER = Track3rWithBiBladeSpinner()

    TRACKER_WITH_BIBLADE_SPINNER.main()
