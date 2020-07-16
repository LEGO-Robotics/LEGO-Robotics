#!/usr/bin/env python3


from ev3dev.ev3 import Motor, Sound

from PIL import Image
from threading import Thread

from track3r_ev3dev1 import Track3r


class Track3rWithBlastingBazooka(Track3r):
    def blast_bazooka_by_ir_beacon(
            self, 
            speed: float = 1000   # degrees per second
        ):
        while True:
            if self.remote_control.beacon:
                self.medium_motor.run_to_rel_pos(
                    speed_sp=speed,
                    position_sp=3 * 360,   # about 3 rotations for 1 shot
                    stop_action=Motor.STOP_ACTION_HOLD)
                self.medium_motor.wait_while(Motor.STATE_RUNNING) 

                self.speaker.play(wav_file='/home/robot/sound/Laughing 1.wav').wait()
                
                while self.remote_control.beacon:
                    pass

            else:
                self.medium_motor.stop(stop_action=Motor.STOP_ACTION_HOLD)


    def main(self, 
             speed: float = 1000   # degrees per second
            ):
        self.screen.image.paste(im=Image.open('/home/robot/image/Pinch middle.bmp'))
        self.screen.update()
            
        Thread(target=self.blast_bazooka_by_ir_beacon,
               daemon=True).start()

        self.keep_driving_by_ir_beacon(speed=speed)


if __name__ == '__main__':
    TRACKER_WITH_BLASTING_BAZOOKA = Track3rWithBlastingBazooka()

    TRACKER_WITH_BLASTING_BAZOOKA.main()
