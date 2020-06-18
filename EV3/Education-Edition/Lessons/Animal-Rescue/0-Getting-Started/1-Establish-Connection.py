#!/usr/bin/env micropython


from ev3dev2.sound import Sound


SPEAKER = Sound()


SPEAKER.play_file(
    wav_file='/home/robot/sound/Hi.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
