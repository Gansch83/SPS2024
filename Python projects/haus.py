import pickle

class Haus:

    Anzahl = 0

    def __init__(self, adresse, hoehe, etagen_zahl):
        self.adresse = adresse
        self.hoehe = hoehe
        self.etagen_zahl = etagen_zahl
        Haus.Anzahl += 1

    def get_Adresse(self):
        return self.adresse

    def __lt__(self, other):
        return self.hoehe < other.hoehe

    def __str__(self):
        return "Adresse: {}\nHoehe: {}\nEtagen: {}".format(self.adresse, self.hoehe, self.etagen_zahl)

    def __del__(self):
        Haus.Anzahl -= 1


class Wolkenkratzer(Haus):

    def __init__(self, adresse, hoehe, etagen_zahl, name):
        super().__init__(adresse, hoehe, etagen_zahl)
        self.name = name

    def __str__(self):
        return "Name: {}\nAdresse: {}\nHoehe: {}\nEtagen: {}".format(self.name, self.adresse, self.hoehe, self.etagen_zahl)
