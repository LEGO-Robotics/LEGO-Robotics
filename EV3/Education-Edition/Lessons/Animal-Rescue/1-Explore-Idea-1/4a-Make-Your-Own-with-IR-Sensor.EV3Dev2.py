#!/usr/bin/env micropython


from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.sound import Sound


IR_SENSOR = InfraredSensor(address=INPUT_4)
SPEAKER = Sound()


def detect_object(
        distance: float = 30,
        sound_to_play: str = 'Hi'):
    if IR_SENSOR.proximity <= distance:
        SPEAKER.play_file(
            wav_file='/home/robot/sound/{}.wav'.format(sound_to_play),
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

 
while True:
    detect_object(
        distance=30,
        sound_to_play='Magic wand')
