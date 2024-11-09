class Konto:
    """ Basis Konto Klasse """

    def __init__(self, inhaber, kontonummer, kontostand):
        """ Konstruktor, Aufruf bei Instanzierung """
        print(".. Konto anlegen")
        self._Inhaber = inhaber
        self._Kontonummer = kontonummer
        self._Kontostand = kontostand
        self.zeige_konto()

    def einzahlen(self, betrag):
        """ Mach eine Einzahlung """
        print(".. Einzahlen   : {:d} {:5.1f}".format(self._Kontonummer, betrag))
        self._Kontostand += betrag

    def auszahlen(self, betrag):
        """ Mach eine Auszahlung """
        print(".. Auszahlen   : {:d} {:5.1f}".format(self._Kontonummer, betrag))
        self._Kontostand -= betrag

    def zeige_konto(self):
        """ Zeige die Kontodaten am Bildschirm """
        print(".. Konto       :", self._Inhaber)
        print("   Kontonummer :", self._Kontonummer)
        print("   Kontostand  :", self._Kontostand)


class Girokonto(Konto):
    """ Giro Konto Klasse """

    def __init__(self, inhaber, kontonummer, kontostand, sollzinsen, habenzinsen):
        """ Giro Konstruktor, Aufruf bei Instanzierung """
        self.__Sollzinsen = sollzinsen
        self.__Habenzinsen = habenzinsen
        # initialisiere Konto
        Konto.__init__(self, inhaber, kontonummer, kontostand)

    def ueberweisung(self, ziel, betrag):
        """ Mach eine Ueberweisung """
        print(".. Transfer    : {:d} {:s} {:d} {:5.1f}".format(self._Kontonummer, "->", ziel._Kontonummer, betrag))
        self._Kontostand -= betrag
        ziel._Kontostand += betrag


class Sparkonto(Konto):
    """ Sparbuch Konto Klasse """

    def __init__(self, inhaber, kontonummer, kontostand, zinssatz):
        """ Spar Konstruktor, Aufruf bei Instanzierung """
        self.Zinssatz = zinssatz
        # initialisiere des Kontos
        Konto.__init__(self, inhaber, kontonummer, kontostand)

    def zeige_konto(self):
        """ Zeige die Kontodaten am Bildschirm, ueberschreibt Konto Funktion """
        Konto.zeige_konto(self)
        print("   Zinssatz    :", self.Zinssatz)


if __name__ == '__main__':
    print("\nKontobeispiel mit Vererbung")

    # Erzeuge zwei Konto-Objekte
    kg = Girokonto("Heinz Meier", 78340, 12000.0, 0.05, 0.01)
    ks = Sparkonto("Heinz Meier", 78341, 4000.0, 0.03)

    print("------------------------------")

    # Mach was damit ...
    kg.einzahlen(1000)
    ks.einzahlen(2000)
    kg.auszahlen(300)
    kg.ueberweisung(ks, 100)

    print("------------------------------")

    # Zeige Kontodaten am Bildschirm
    kg.zeige_konto()
    ks.zeige_konto()

