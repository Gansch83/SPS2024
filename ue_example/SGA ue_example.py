import csv

liste = []

#lese CSV-Datei ue_example.csv ein
with open("ue_example.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    for line in csv_reader:
        print(line)
        liste.append(line)

print(liste)

#Berechnung der Summe basierend auf dem key
def summe(p_liste, key):
    tot = 0
    for i in p_liste:
        tot += float(i[key])
    return tot

Lemon = summe(liste, "Lemon")
Orange = summe(liste, "Orange")
print(Lemon)
print(Orange)