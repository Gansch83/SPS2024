class Konto:
   """ Beispiel eines einfachen Kontos """

   def __init__(self, inhaber, kontonummer, kontostand):
      """ Konstruktor """
      self.__Inhaber = inhaber
      self.__Kontonummer = kontonummer
      self.__Kontostand = kontostand

   def ueberweisung(self, ziel, betrag):
      """ Mach eine Ueberweisung """
      print (".. Transfer    :", self.__Inhaber, "->", ziel.__Inhaber, betrag)
      self.__Kontostand -= betrag
      ziel.__Kontostand += betrag

   def einzahlen(self, betrag):
      """ Mach eine Einzahlung """
      print (".. Einzahlen   :", self.__Inhaber, betrag)
      self.__Kontostand += betrag

   def auszahlen(self, betrag):
      """ Mach eine Auszahlung """
      print (".. Auszahlen   :", self.__Inhaber, betrag)
      self.__Kontostand -= betrag

   def zeige_konto(self):
      """ Zeige die Kontodaten am Bildschirm """
      print (".. Konto       :", self.__Inhaber)
      print ("   Kontonummer :", self.__Kontonummer)
      print ("   Kontostand  :", self.__Kontostand)


if __name__ == '__main__':

   print ("\nKontobeispiel mit class")

   # Erzeuge zwei Konto-Objekte
   k1 = Konto("Heinz Meier", 1234, 12000.0)
   k2 = Konto("Erwin Schmidt", 6789, 15000.0)

   # Mach was damit ...
   k1.ueberweisung(k2, 100)
   k1.auszahlen(200)
   k2.einzahlen(500)

   # Zeige Kontodaten am Bildschirm
   k1.zeige_konto()
   k2.zeige_konto()
