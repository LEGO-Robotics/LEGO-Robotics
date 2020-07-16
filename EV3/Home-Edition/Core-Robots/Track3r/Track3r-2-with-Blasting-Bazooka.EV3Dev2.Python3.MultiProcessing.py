#!/usr/bin/env python3
# (MicroPython does not yet support Display as of 2020)


from ev3dev2.sound import Sound

from multiprocessing import Process

from track3r_ev3dev2 import Track3r


class Track3rWithBlastingBazooka(Track3r):
    def blast_bazooka_by_ir_beacon(self, channel: int = 1, speed: float = 100):
        while True:
            if self.ir_sensor.beacon(channel=channel):
                self.medium_motor.on_for_rotations(
                    speed=speed,
                    rotations=3,   # about 3 rotations for 1 shot
                    block=True,
                    brake=True)

                self.speaker.play_file(
                    wav_file='/home/robot/sound/Laughing 1.wav',
                    volume=100,
                    play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

                while self.ir_sensor.beacon(channel=channel):
                    pass

            else:
                self.medium_motor.off(brake=True)


    def main(self, speed: float = 100):
        self.screen.image_filename(
            filename='/home/robot/image/Pinch middle.bmp',
            clear_screen=True)
        self.screen.update()

        Process(target=self.blast_bazooka_by_ir_beacon,
                daemon=True).start()

        self.keep_driving_by_ir_beacon(speed=speed)


if __name__ == '__main__':
    TRACKER_WITH_BLASTING_BAZOOKA = Track3rWithBlastingBazooka()

    TRACKER_WITH_BLASTING_BAZOOKA.main()
