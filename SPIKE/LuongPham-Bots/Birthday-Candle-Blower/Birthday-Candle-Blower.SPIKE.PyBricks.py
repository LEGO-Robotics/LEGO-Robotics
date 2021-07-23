from pybricks.hubs import PrimeHub


HAPPY_BIRTHDAY_SONG = [
    'G3/8', 'G3/8', 'A3/4', 'G3/4', 'C4/4', 'B3/2',
    'G3/8', 'G3/8', 'A3/4', 'G3/4', 'D4/4', 'C4/2',
    'G3/8', 'G3/8', 'G4/4', 'E4/4',
    'C4/8', 'C4/8', 'B3/4', 'A3/4',
    'F4/8', 'F4/8', 'E4/4', 'C4/4', 'D4/4', 'C4/2'
]


class BirthdayBot:
    def __init__(self):
        self.hub = PrimeHub()

    def say_happy_birthday(self):
        self.hub.speaker.say(text='Happy Birthday to Mommy!')

    def sing_happy_birthday(self):
        self.hub.speaker.play_notes(
            notes=HAPPY_BIRTHDAY_SONG,
            tempo=120)

    def main(self):
        self.say_happy_birthday()

        self.sing_happy_birthday()


if __name__ == '__main__':
    BIRTHDAY_BOT = BirthdayBot()

    BIRTHDAY_BOT.main()
