import time
#Datentypen - type vs id
print("********** Datentypen **********")
a = 1
print("Infos zur Variable a")
print(type(a))
print(id(a))

#Kopie oder Zeiger
print("********** Kopie / Zeiger **********")
a = 342
b = a
print("a (342): ", id(a), "b (b = a): ", id(b))
b = 265
print("a (342): ", id(a), "b (265): ", id(b))

#Strings
print("********** Strings **********")
print("Ein Satz\n mit Zeilenumbruch")

a = "Hallo"
b = "Du"
c = "Ein Satz /t mit tab"

print(a + b)
print("Ein Satz\t mit tab")

print("Ein Satz\n mit Zeilenumbruch")

s = "Unix\nWindows\r\nMac\rLetzte Zeile"
print(s.splitlines())
s = "Dieser String wird durchsucht"
print(s.split())
print(s.split("e"))
print(s.find("haha"))
print(s.find("w"))
print(s.count("e"))
print(s.replace("wird", "wurde"))
print(s)
print(s.lower())
print(s.upper())
s = "    \t\n  \rUmgeben von Whitespaces   \t\t\r"
print(s)
print(s.strip())

#Formatierungen
print("********** Formatierung **********")
text = "Es ist {:d}:{:d} Uhr".format(13,37)
text2 = "Es ist {:d}:{:d} Uhr".format(time.localtime().tm_hour,time.localtime().tm_min)
print(text)
print(text2)

print("Gleitkommazahl {:+10.2f}".format(2.2))

#Kollektionen
print("********** Kollektionen **********")

a = {1,3,3,4, "hello", "world", "hello"}
print(a)

woerterbuch = {"Germany" : "Deutschland", "Spain" : "Spanien", }
print(woerterbuch["Germany"])

print(woerterbuch.items())
print(woerterbuch.keys())
print(woerterbuch.values())

#Kontrollstrukturen
print("********** Kontrollstrukturen **********")

d: dict[str, int] = {"a": 1, "b": 2, "c": 3}

for i in d:
    print(i, "->", d[i])

# Creating a dictionary
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

# Printing the dictionary using print()
print(fruit_colors)

# Output: {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}

# Printing a dictionary using a loop and the items() method
for key, value in fruit_colors.items():
    print(key, ":", value)

# Output:
# apple : red
# banana : yellow
# grape : purple