# Übung 1.1
print("\n\nÜbung 1.1\n")
eingabe = input("Bitte geben Sie die Anzahl ein: ")

print("Sie haben", eingabe, "eingegeben.")

for i in range(int(eingabe)):
    print("\n", end="")
    for l in range(int(eingabe)):
        print("*", end="")

#for i in range(int(eingabe)):
#    print("\n**********", end="")

# Übung 1.2
print("\n\nÜbung 1.2\n")
chaos = ["Hello", "world", "is", "always", "a", "good", "start"]
str1 = ""

for j in chaos:
    print(j, end=" ")
    if len(j) > len(str1):
        str1 = j

print("\nLongest word is:", str1)

# Übung 1.3
print("\n\nÜbung 1.3\n")

beispiel = [1,2,3,4,5,2,6,8,2,4,1,0,6]
#Ausgabe der liste ohne duplikate
print("Liste ohne Duplikate:", list(set(beispiel))) #set() entfernt Duplikate


# Übung 1.4
print("\n\nÜbung 1.4\n")

str2 = "4.52;1.23;8.65;1.4"
dic = {}

numbers = str2.split(";")
print(numbers)
print(dic.items())
for k in numbers:
    print(round(float(k)))
    dic.update({round(float(k)) : k})
    print(dic.items())

print(dic.items())
#da key "1" bereits vorhanden, wird der Wert 1.23 mit dem letzten Wert 1.4 überschrieben



# Übung 2.1
print("\n\nÜbung 2.1\n")

#funktion für die Berechnung der Fibonacci-Zahlen
def fib(n):
    a, b = 0, 1
    for p in range(n):
        a, b = b, a + b
        print(a)
    return a

eing = input("Fibonacci-Zahlen für: ")

print("Fibonacci-Zahlen: " , eing,  " = ", fib(int(eing)))



# Übung 3.1
print("\n\nÜbung 3.1\n")

def calc(a, b):

    print ("Addition: ", a, " + ", b, " = ", a + b)
    print ("Subtraktion: ", a, " - ", b, " = ", a - b)
    print ("Multiplikation: ", a, " * ", b, " = ", a * b)
    if b == 0:
        print ("naughty boy..., no division by zero")
    else:
        print ("Division: ", a, " / ", b, " = ", a / b)

inp1 = input("Bitte geben Sie die erste Zahl ein: ")
inp2 = input("Bitte geben Sie die zweite Zahl ein: ")
calc(int(inp1), int(inp2))

# Übung 3.2
print("\n\nÜbung 3.2\n")

# Funktion für die Prüfung auf Primzahlen
def prime2(n):
    if n < 2:
        return False
    for t in range(2, n):
        if n % t == 0:
            return False
    return True

list4 = [323, 1, 2, 43, 97, 71717117, 737373737373737]

for u in list4:
    if prime2(u):
        print(u, "is a prime number")
    else:
        print(u, "is not a prime number")


# Übung Folien File öffnen
print("\n\nÜbung Folien File öffnen\n")

