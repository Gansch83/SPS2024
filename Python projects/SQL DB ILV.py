import sqlite3
# verbinde zu (leerer) Datenbank
connection = sqlite3.connect("test_autoverwaltung.db")
# erstelle Positionsanzeiger
cursor = connection.cursor()
# erzeuge eine Tabelle
#cursor.execute("""CREATE TABLE autohaus ( marke TEXT, modell TEXT, leistung INTEGER)""")
# sende Daten
cursor.execute("""INSERT INTO autohaus VALUES ('Porsche', '911', 350)""")
# sende Daten (Alternativ)
auto = ("Skoda", "Octavia", 140)
cursor.execute("""INSERT INTO autohaus VALUES (?, ?, ?)""", auto)
auto = ("Audi", "Q3", 110)
cursor.execute("""INSERT INTO autohaus VALUES (?, ?, ?)""", auto)
# Daten abspeichern
connection.commit()
# Daten abfragen
cursor.execute("SELECT marke, modell FROM autohaus")
print (cursor.fetchall())

cursor.execute("SELECT count(*) FROM autohaus WHERE leistung  > 200")
print (cursor.fetchall())

# erzeuge eine Tabelle und verknüpfe mit tabelle autohaus

cursor.execute("""DROP TABLE besitzer;""")