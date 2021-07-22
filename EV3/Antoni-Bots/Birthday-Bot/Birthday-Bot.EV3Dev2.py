#!/usr/bin/env micropython


from ev3dev2.sound import Sound


class BirthdayBot:
    def __init__(self):
        self.speaker = Sound()

    def play_happy_birthday(self):
        self.speaker.speak(
            text='Happy Birthday to You!',
            volume=100,
            play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

    def main(self):
        while True:
            self.play_happy_birthday()


if __name__ == '__main__':
    BIRTHDAY_BOT = BirthdayBot()

    BIRTHDAY_BOT.main()
