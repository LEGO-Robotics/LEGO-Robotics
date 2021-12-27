#!/usr/bin/env pybricks-micropython


from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Stop

from time import sleep

from track3r_pybricks import Track3r


class Track3rWithHeavyHammer(Track3r):
    def hammer_by_ir_beacon(self):
        if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.screen.load_image(ImageFile.ANGRY)

            self.medium_motor.run_time(
                speed=1000,   # deg/s
                time=1000,   # ms
                then=Stop.HOLD,
                wait=True)

            self.speaker.play_file(file=SoundFile.LAUGHING_2)

            self.medium_motor.run_time(
                speed=-1000,   # deg/s
                time=1000,   # ms
                then=Stop.HOLD,
                wait=True)

        else:
            self.screen.load_image(ImageFile.CRAZY_1)

            self.medium_motor.run_time(
                speed=1000,   # deg/s
                time=0.3 * 1000,   # ms
                then=Stop.HOLD,
                wait=True)

            sleep(0.1)

            self.screen.load_image(ImageFile.CRAZY_2)

            self.medium_motor.run_time(
                speed=-1000,   # deg/s
                time=0.3 * 1000,   # ms
                then=Stop.COAST,
                wait=True)


    def main(self, speed: float = 1000):
        self.medium_motor.run_time(
            speed=-200,   # deg/s
            time=1000,   # ms
            then=Stop.HOLD,
            wait=True)

        while True:
            self.drive_once_by_ir_beacon(speed=speed)

            self.hammer_by_ir_beacon()


if __name__ == '__main__':
    TRACKER_WITH_HEAVY_HAMMER = Track3rWithHeavyHammer()

    TRACKER_WITH_HEAVY_HAMMER.main(speed=1000)
