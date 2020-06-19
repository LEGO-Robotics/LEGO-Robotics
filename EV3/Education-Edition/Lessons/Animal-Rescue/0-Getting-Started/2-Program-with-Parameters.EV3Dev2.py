#!/usr/bin/env micropython


from ev3dev2.sound import Sound


SPEAKER = Sound()


SPEAKER.play_file(
    wav_file='/home/robot/sound/Fanfare.wav',
    volume=50,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

SPEAKER.play_file(
    wav_file='/home/robot/sound/LEGO.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Green.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

SPEAKER.play_file(
    wav_file='/home/robot/sound/EV3.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Good.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Boo.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Activate.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

SPEAKER.play_file(
    wav_file='/home/robot/sound/Blip 1.wav',
    volume=100,
    play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
