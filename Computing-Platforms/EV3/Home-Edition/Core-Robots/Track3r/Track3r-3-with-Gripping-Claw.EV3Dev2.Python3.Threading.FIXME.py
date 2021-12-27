#!/usr/bin/env python3
# (MicroPython does not yet support Display as of 2020)


from ev3dev2.sound import Sound

from threading import Thread

from track3r_ev3dev2 import Track3r


class Track3rWithGrippingClaw(Track3r):
    is_gripping = False
    
    def grip_or_release_claw_by_ir_beacon(self, speed: float = 100):
        while True:
            if self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                if self.is_gripping:
                    self.medium_motor.on(
                        speed=-speed,
                        block=False,
                        brake=False)

                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Air release.wav',
                        volume=100,
                        play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

                    self.is_gripping = False

                else:
                    self.medium_motor.on(
                        speed=speed,
                        block=False,
                        brake=False)

                    self.speaker.play_file(
                        wav_file='/home/robot/sound/Airbrake.wav',
                        volume=100,
                        play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

                    self.is_gripping = True

                while self.ir_sensor.beacon(channel=self.ir_beacon_channel):
                    pass


    def main(self, speed: float = 100):
        Thread(target=self.grip_or_release_claw_by_ir_beacon,
               daemon=True).start()

        self.keep_driving_by_ir_beacon(speed=speed)

        # FIXME: bug when multiple Threads access same Sensor
        # ValueError: invalid literal for int() with base 10: ''


if __name__ == '__main__':
    TRACKER_WITH_GRIPPING_CLAW = Track3rWithGrippingClaw()

    TRACKER_WITH_GRIPPING_CLAW.main()
