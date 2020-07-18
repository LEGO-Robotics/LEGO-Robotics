#!/usr/bin/env python3


from ev3dev.ev3 import Motor

from PIL import Image
from time import sleep

from track3r_ev3dev1 import Track3r


class Track3rWithHeavyHammer(Track3r):
    def hammer_by_ir_beacon(self):
        if self.remote_control.beacon:
            self.screen.image.paste(im=Image.open('/home/robot/image/Angry.bmp'))
            self.screen.update()
        
            self.medium_motor.run_timed(
                speed_sp=1000,   # deg/s
                time_sp=0.3 * 1000,   # ms 
                stop_action=Motor.STOP_ACTION_HOLD)
            self.medium_motor.wait_while(Motor.STATE_RUNNING)

            self.speaker.play(wav_file='/home/robot/sound/Laughing 2.wav').wait()

            self.medium_motor.run_timed(
                speed_sp=-200,   # deg/s
                time_sp=1000,   # ms 
                stop_action=Motor.STOP_ACTION_HOLD)
            self.medium_motor.wait_while(Motor.STATE_RUNNING)

        else:
            self.screen.image.paste(im=Image.open('/home/robot/image/Crazy 1.bmp'))
            self.screen.update()

            self.medium_motor.run_timed(
                speed_sp=750,   # deg/s
                time_sp=0.1 * 1000,   # ms 
                stop_action=Motor.STOP_ACTION_HOLD)
            self.medium_motor.wait_while(Motor.STATE_RUNNING)

            sleep(0.1)

            self.screen.image.paste(im=Image.open('/home/robot/image/Crazy 2.bmp'))
            self.screen.update()

            self.medium_motor.run_timed(
                speed_sp=-300,   # deg/s (-100 too soft)
                time_sp=0.2 * 1000,   # ms 
                stop_action=Motor.STOP_ACTION_COAST)
            self.medium_motor.wait_while(Motor.STATE_RUNNING)


    def main(self,
             speed: float = 1000   # deg/s
            ):
        # FIXME: need MultiProcessing/Threading for smoother run

        while True:
            self.drive_once_by_ir_beacon(speed=speed)

            self.hammer_by_ir_beacon()


if __name__ == '__main__':
    TRACKER_WITH_HEAVY_HAMMER = Track3rWithHeavyHammer()

    TRACKER_WITH_HEAVY_HAMMER.main()
