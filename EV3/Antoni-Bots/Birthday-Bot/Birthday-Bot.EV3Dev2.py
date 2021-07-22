#!/usr/bin/env micropython


import json

from ev3dev2.sound import Sound


HAPPY_BIRTHDAY_SONG = json.load(open('Happy-Birthday-Song.json'))


class BirthdayBot:
    def __init__(self):
        self.speaker = Sound()

    def play_happy_birthday(self):
        self.speaker.play_song(
            song=HAPPY_BIRTHDAY_SONG,
            tempo=120,
            delay=0.05)

    def main(self):
        while True:
            self.play_happy_birthday()


if __name__ == '__main__':
    BIRTHDAY_BOT = BirthdayBot()

    BIRTHDAY_BOT.main()
