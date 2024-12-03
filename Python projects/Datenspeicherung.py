import pickle

class Haus:
    ANZAHL_HAUS = 0
    def __init__(self, adresse, hoehe, etage):
        self.__adresse = str(adresse)
        self.__hoehe = float(hoehe)
        self.__etage = int(etage)
        Haus.ANZAHL_HAUS += 1

    @property
    def Get_Adresse(self):
        return self.__adresse

    @property
    def Get_Hoehe(self):
        return self.__hoehe

    @property
    def Get_Etage(self):
        return self.__etage

    def __str__(self):
        return f"Adresse: {self.__adresse}, Hoehe: {self.__hoehe}, Etage: {self.__etage}"

    def __lt__(self, other):
        return self.__hoehe < other.__hoehe



class Wolkenkratzer(Haus):
    ANZAHL_WOLKENKRATZER = 0

    def __init__(self, adresse, hoehe, etage, name):
        super().__init__(adresse, hoehe, etage)
        self.__name = str(name)
        Wolkenkratzer.ANZAHL_WOLKENKRATZER += 1

    @property
    def Get_Name(self):
        return self.__name

    def __str__(self):
        return f"Adresse: {self.Get_Adresse}, Hoehe: {self.Get_Hoehe}, Etage: {self.Get_Etage}, Name: {self.Get_Name}"


def main():
    Haus1 = Haus("Kirchengasse 3", 16.27, 5)
    print(Haus1)
    # >>> Adresse: Kirchengasse 3, Hoehe: 16.27, Etage: 5
    print(Haus1.Get_Adresse)
    # >>> Kirchengasse 3
    print(Haus.ANZAHL_HAUS)

    Haus2 = Haus("Kellergasse 1",18.3,6)
    print(Haus1 < Haus2)
    # >>> True
    print(Haus.ANZAHL_HAUS)
    # >>> 2

    Wolkenkratzer1 = Wolkenkratzer("Donau-City-Straße 7", 220.3, 60, "DC-Tower")
    print(Wolkenkratzer1)
    # >>> Adresse: Donau-City-Straße 7, Hoehe: 220.3, Etage: 60, Name: DC-Tower

    haeuser = []
    #haeuser.append(Haus1)
    print(haeuser)
    #lade die Daten aus der Datei
    haeuser = pickle.load(open("haeuser.dat", "rb"))
    print(haeuser)
    haeuser.append(Haus2)
    print(haeuser)
    haeuser.append(Wolkenkratzer1)
    print(haeuser)
    #pickle.dump(haeuser, open("haeuser.dat", "wb"))



if __name__ == '__main__':
    main()
