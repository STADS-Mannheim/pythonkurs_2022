"""
Lernziel:
Schnelles Verständnis für den grundsätzlichen Syntax von Python.

Dauer:
10 Minuten
"""

# Das ist eine Pythondatei. 
# Sie endet typischerweise mit .py
# Kommentare beginnen mit # und gelten bis zum Zeilenende

# Gebe einen Text aus aus
print("Guten Abend, Mannheim!")

# Benutze Python als Taschenrechner
1 + 2
2 * (15 / 3)


# Verwende Variablen
x = 5
y = 3
z = x + y
a = "Guten Abend"
b = "Mannheim"

# Hinweise:
# - Variablen werden erzeugt zu den Zeitpunkt, 
#   zu dem sie das erste Mal einen Wert zugewiesen bekommen
# - Es gibt kein Kommando, um Variablen zu deklarieren


# Einrückung von Text ist in Python entscheidend

if 1 > 0:
    print("1>0 immer wahr, daher wird diese Zeile ausgegeben.")

if 0 > 1:
    print("Diese Zeile wird nicht ausgegeben, da 0>1 immer falsch ist.")

# Achtung 
if 0 > 1:
print("Python wirft einen Einrückungsfehler, \
    da es eine Anweisung für den if-Block erwartet.")

# Falls ihr nichts ausführen wollt, könnt ihr dies aber aktiv umgehen
if 0 > 1:
    pass
print("Jetzt entsteht kein Fehler. \
    Dieser Text zählt aber nicht mehr zum if-Block dazu")



