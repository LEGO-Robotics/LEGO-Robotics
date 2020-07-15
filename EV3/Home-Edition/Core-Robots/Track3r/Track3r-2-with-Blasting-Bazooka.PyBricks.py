#!/usr/bin/env pybricks-micropython


from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Stop

from track3r_pybricks import Track3r


class Track3rWithBlastingBazooka(Track3r):
    def blast_bazooka_by_ir_beacon(
            self, 
            speed: float = 1000   # degrees per second
        ):
        if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.medium_motor.run_angle(
                speed=speed,
                rotation_angle=3 * 360,   # about 3 rotations for 1 shot
                then=Stop.HOLD,
                wait=True) 

            self.speaker.play_file(file=SoundFile.LAUGHING_1)
               
            while Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
                pass

        else:
            self.medium_motor.stop()


    def main(self, 
             speed: float = 1000   # degrees per second
            ):
        self.screen.load_image(ImageFile.PINCHED_MIDDLE)
            
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

            self.blast_bazooka_by_ir_beacon(speed=speed)


if __name__ == "__main__":
    TRACKER_WITH_BLASTING_BAZOOKA = Track3rWithBlastingBazooka()

    TRACKER_WITH_BLASTING_BAZOOKA.main()
    