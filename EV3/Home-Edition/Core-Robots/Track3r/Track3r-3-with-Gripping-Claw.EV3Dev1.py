#!/usr/bin/env python3


from track3r_ev3dev1 import Track3r


class Track3rWithGrippingClaw(Track3r):
    is_gripping = False
    
    def grip_or_release_claw_by_ir_beacon(
            self,
            speed: float = 1000   # deg/s
        ):
        if self.remote_control.beacon:
            if self.is_gripping:
                self.medium_motor.run_forever(speed_sp=-speed)

                self.speaker.play(wav_file='/home/robot/sound/Air release.wav').wait()

                self.is_gripping = False

            else:
                self.medium_motor.run_forever(speed_sp=speed)

                self.speaker.play(wav_file='/home/robot/sound/Airbrake.wav').wait()

                self.is_gripping = True

            while self.remote_control.beacon:
                pass


    def main(self,
             speed: float = 1000   # deg/s
            ):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

            self.grip_or_release_claw_by_ir_beacon(speed=speed)


if __name__ == '__main__':
    TRACKER_WITH_GRIPPING_CLAW = Track3rWithGrippingClaw()

    TRACKER_WITH_GRIPPING_CLAW.main()
