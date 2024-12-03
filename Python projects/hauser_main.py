import pickle
from haus import Haus, Wolkenkratzer


hauser = []
try:
    hauser = pickle.load(open("hauser.pkl", "rb"))
except FileNotFoundError:
    print("konte datei nicht finden")
except Exception as e:
    print("Fehler beim laden der Daten:", e)

print("folgende Häuser sind bereits vorhanden:")
for h in hauser:
    print(h)

hauser.append(Haus("Hauptstrasse 1", 10, 2))
hauser.append(Wolkenkratzer("Hauptstrasse 2", 12, 3, "Skyline"))

# hinzufügen von haus und speichern in pickle
pickle.dump(hauser, open("hauser.pkl", "wb"))


