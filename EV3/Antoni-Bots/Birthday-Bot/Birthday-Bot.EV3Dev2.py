#!/usr/bin/env micropython


import json

from ev3dev2.sound import Sound


HAPPY_BIRTHDAY_SONG = json.load(open('Happy-Birthday-Song.json'))


class BirthdayBot:
    def __init__(self):
        self.speaker = Sound()

    def say_happy_birthday(self):
        self.speaker.speak(
            text='Happy Birthday to Mommy!',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    def sing_happy_birthday(self):
        self.speaker.play_song(
            song=HAPPY_BIRTHDAY_SONG,
            tempo=120,
            delay=0)

    def main(self):
        self.say_happy_birthday()

        self.sing_happy_birthday()


if __name__ == '__main__':
    BIRTHDAY_BOT = BirthdayBot()

    BIRTHDAY_BOT.main()
