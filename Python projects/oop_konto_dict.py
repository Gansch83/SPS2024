def neues_konto(inhaber, kontonummer, kontostand):
    print(".. neues Konto :", inhaber)
    return {
        "Inhaber": inhaber,
        "Kontonummer": kontonummer,
        "Kontostand": kontostand
    }


def geldtransfer(quelle, ziel, betr):
    print(".. Transfer    :", quelle["Inhaber"], "->", ziel["Inhaber"], betr)
    quelle["Kontostand"] -= betr
    ziel["Kontostand"] += betr


def einzahlen(konto, betrag):
    print(".. Einzahlen   :", konto["Inhaber"], betrag)
    konto["Kontostand"] += betrag


def auszahlen(konto, betrag):
    print(".. Auszahlen   :", konto["Inhaber"], betrag)
    konto["Kontostand"] -= betrag


def zeige_konto(konto):
    print(".. Konto       :", konto["Inhaber"])
    print("   Kontonummer :", konto["Kontonummer"])
    print("   Kontostand  :", konto["Kontostand"])


if __name__ == '__main__':
    print("\nKontobeispiel mit dict")
    k1 = neues_konto("Heinz Meier", 1234, 12000.0)
    k2 = neues_konto("Erwin Schmidt", 6789, 15000.0)
    geldtransfer(k1, k2, 100)
    auszahlen(k1, 200)
    einzahlen(k2, 500)
    zeige_konto(k1)
    zeige_konto(k2)




