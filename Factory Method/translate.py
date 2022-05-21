from time import sleep


class FrenchLocalizer:

    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle": "cyclette"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class SpanishLocalizer:

    def __init__(self):
        self.translations = {"car": "carro", "bike": "bicicleta",
                             "cycle": "ciclo"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:

    def __init__(self):
        self.translations = {"car": "car", "bike": "bike",
                             "cycle": "cycle"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


if __name__ == "__main__":

    # main method to call others
    localizer = {
        'french': FrenchLocalizer,
        'spanish': SpanishLocalizer,
        'english': EnglishLocalizer
    }

    while True:
        print('-----------')
        print('1) Write the language')
        language = input()
        print('2) Write the word')
        word = input()
        instance_localize = localizer.get(language)()
        translate = instance_localize.localize(word)
        print(f'{word} - {translate}')
        sleep(3)
