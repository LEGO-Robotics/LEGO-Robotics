#!/usr/bin/env pybricks-micropython


from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button

from threading import Thread

from track3r_pybricks import Track3r


class Track3rWithGrippingClaw(Track3r):
    is_grabbing = False
    
    def grip_or_release_claw_by_ir_beacon(
            self,
            speed: float = 1000   # deg/s
        ):
        while True:
            if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                if self.is_grabbing:
                    self.medium_motor.run(speed=-speed)

                    self.speaker.play_file(file=SoundFile.AIR_RELEASE)

                    self.is_grabbing = False

                else:
                    self.medium_motor.run(speed=speed)

                    self.speaker.play_file(file=SoundFile.AIRBRAKE)

                    self.is_grabbing = True

                while Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                    pass


    def main(self, speed: float = 1000):
        Thread(target=self.grip_or_release_claw_by_ir_beacon).start()
        
        self.keep_driving_by_ir_beacon(speed=speed)


if __name__ == '__main__':
    TRACKER_WITH_GRIPPING_CLAW = Track3rWithGrippingClaw()

    TRACKER_WITH_GRIPPING_CLAW.main()
