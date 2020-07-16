#!/usr/bin/env pybricks-micropython


from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button

from multiprocessing import Process

from track3r_pybricks import Track3r


class Track3rWithGrippingClaw(Track3r):
    is_gripping = False
    
    def grip_or_release_claw_by_ir_beacon(
            self,
            speed: float = 1000   # deg/s
        ):
        while True:
            if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                if self.is_gripping:
                    self.medium_motor.run(speed=-speed)

                    self.speaker.play_file(file=SoundFile.AIR_RELEASE)

                    self.is_gripping = False

                else:
                    self.medium_motor.run(speed=speed)

                    self.speaker.play_file(file=SoundFile.AIRBRAKE)

                    self.is_gripping = True

                while Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                    pass


    def main(self, speed: float = 1000):
        Process(target=self.grip_or_release_claw_by_ir_beacon).start()
        
        self.keep_driving_by_ir_beacon(speed=speed)

        # FIXME
        # OSError: [Errno 5] EIO: 
        # Unexpected hardware input/output error with a motor or sensor:
        # --> Try unplugging the sensor or motor and plug it back in again.
        # --> To see which sensor or motor is causing the problem,
        #     check the line in your script that matches
        #     the line number given in the 'Traceback' above.
        # --> Try rebooting the hub/brick if the problem persists.


if __name__ == '__main__':
    TRACKER_WITH_GRIPPING_CLAW = Track3rWithGrippingClaw()

    TRACKER_WITH_GRIPPING_CLAW.main()
