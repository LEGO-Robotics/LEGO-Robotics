#!/usr/bin/env python3
# (MicroPython does not yet support Display as of 2020)


from ev3dev2.sound import Sound

from time import sleep

from track3r_ev3dev2 import Track3r


class Track3rWithHeavyHammer(Track3r):
    def hammer_by_ir_beacon(self):
        if self.ir_sensor.beacon(channel=self.ir_beacon_channel):
            self.screen.image_filename(
                filename='/home/robot/image/Angry.bmp',
                clear_screen=True)
            self.screen.update()
        
            self.medium_motor.on_for_seconds(
                seconds=0.3,
                speed=100,
                block=True,
                brake=True)

            self.speaker.play_file(
                wav_file='/home/robot/sound/Laughing 2.wav',
                volume=100,
                play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

            self.medium_motor.on_for_seconds(
                speed=-20,
                seconds=1, 
                block=True,
                brake=True)

        else:
            self.screen.image_filename(
                filename='/home/robot/image/Crazy 1.bmp',
                clear_screen=True)
            self.screen.update()
            
            self.medium_motor.on_for_seconds(
                speed=75,
                seconds=0.1,
                block=True,
                brake=True)

            sleep(0.1)

            self.screen.image_filename(
                filename='/home/robot/image/Crazy 2.bmp',
                clear_screen=True)
            self.screen.update()

            self.medium_motor.on_for_seconds(
                speed=-30,   # -10 too soft
                seconds=0.2,
                brake=False,
                block=True)


    def main(self, speed: float = 100):
        self.medium_motor.on_for_seconds(
            speed=-20,  
            seconds=1,   
            block=True,
            brake=True)

        # FIXME: need MultiProcessing/Threading for smoother run
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

            self.hammer_by_ir_beacon()


if __name__ == '__main__':
    TRACKER_WITH_HEAVY_HAMMER = Track3rWithHeavyHammer()

    TRACKER_WITH_HEAVY_HAMMER.main()
