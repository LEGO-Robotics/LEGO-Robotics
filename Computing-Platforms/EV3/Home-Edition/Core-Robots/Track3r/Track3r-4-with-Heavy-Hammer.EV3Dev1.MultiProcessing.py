#!/usr/bin/env python3


from ev3dev.ev3 import Motor

from multiprocessing import Process
from PIL import Image
from time import sleep

from track3r_ev3dev1 import Track3r


class Track3rWithHeavyHammer(Track3r):
    def hammer_by_ir_beacon(self):
        while True:
            if self.remote_control.beacon:
                self.screen.image.paste(im=Image.open('/home/robot/image/Angry.bmp'))
                self.screen.update()
            
                self.medium_motor.run_timed(
                    speed_sp=1000,   # deg/s
                    time_sp=1000,   # ms 
                    stop_action=Motor.STOP_ACTION_HOLD)
                self.medium_motor.wait_while(Motor.STATE_RUNNING)

                self.speaker.play(wav_file='/home/robot/sound/Laughing 2.wav').wait()

                self.medium_motor.run_timed(
                    speed_sp=-1000,   # deg/s
                    time_sp=1000,   # ms 
                    stop_action=Motor.STOP_ACTION_HOLD)
                self.medium_motor.wait_while(Motor.STATE_RUNNING)

            else:
                self.screen.image.paste(im=Image.open('/home/robot/image/Crazy 1.bmp'))
                self.screen.update()

                self.medium_motor.run_timed(
                    speed_sp=500,   # deg/s
                    time_sp=0.1 * 1000,   # ms 
                    stop_action=Motor.STOP_ACTION_HOLD)
                self.medium_motor.wait_while(Motor.STATE_RUNNING)

                sleep(0.1)

                self.screen.image.paste(im=Image.open('/home/robot/image/Crazy 2.bmp'))
                self.screen.update()

                self.medium_motor.run_timed(
                    speed_sp=-500,   # deg/s (-100 too soft)
                    time_sp=0.1 * 1000,   # ms 
                    stop_action=Motor.STOP_ACTION_COAST)
                self.medium_motor.wait_while(Motor.STATE_RUNNING)


    def main(self,
             speed: float = 1000   # deg/s
            ):
        self.medium_motor.run_timed(
            speed_sp=-200,   # deg/s
            time_sp=1000,   # ms 
            stop_action=Motor.STOP_ACTION_HOLD)
        self.medium_motor.wait_while(Motor.STATE_RUNNING)

        Process(target=self.hammer_by_ir_beacon,
                daemon=True).start()

        self.keep_driving_by_ir_beacon(speed=speed)


if __name__ == '__main__':
    TRACKER_WITH_HEAVY_HAMMER = Track3rWithHeavyHammer()

    TRACKER_WITH_HEAVY_HAMMER.main()
