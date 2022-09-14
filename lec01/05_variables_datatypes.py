"""
Lernziel:
Überblick über mögliche Variablennamen, ihre Typen und Eigenschaften

Dauer:
20 Minuten
"""

################################################################################

# - Variablen kann man als Schubladen verstehen, 
#   in denen Werte gespeichert werden
# - Python kennt kein Kommando, um Variablen zu deklarieren
# - Variablen werden, wenn sie einen Wert zugewiesen bekommen, erzeugt.


alter = 19
name = "Max"
print(alter)
print(name)


# Variablen werden nicht mit einem bestimmten Typ erzeugt und können 
# ihren Typ auch noch ändern, nachdem er bereits definiert wurde

alter = 20
name = "Martina"

name = 123


################################################################################

# Variablennamen
# - Variablen sollten KURZE aber VERSTÄNDLICHE Namen erhalten
# - Variablennamen müssen mit Buchstabe oder Unterstrich("_") beginnen
# - Variablennamen dürfen nicht mit einer Zahl beginnen
# - Variablennamen dürfen nur Buchstaben, Zahlen und Unterstriche beinhalten
# - Variablennamen unterscheiden bzgl. Groß- und Kleinschreibung

# Beispiele
_ = 1
_alter = 35
hallo_das_ist_ein_langer_text = 5
alter2 = 3


# Was ist nicht erlaubt?
2alter = 25
preis€ = 5
hallo-das-ist-ein-langer-text = 5
vorname nachname = "Max Mustermann"


# Mehrere Variablen gleichzeitig bennen
x, y, z = 1,2,3
print(x+y+z)

a = b = 5
print(a)
print(b)
a = 3
print(b)

################################################################################

# Variablen ausgeben

a = "Heute ist "
b = "Dienstag"
c = " und "
d = 19
e = 20
f = " Uhr"

# String aneinenderhängen
print(a+b)
# Zahlen addieren
print(d+e)
# Unterschiedliche Typen gibt einen Error
print(a+b+c+d+f)

# Es gibt eber eine Lösung - fstrings
print(f"{a}{b}{c}{d}{e}{f}")



###############################################################################

# Variablentypen

"""
Übersicht über alle Datentypen.
Die für uns am Anfang relevantesten sind mit * hervorgehoben.
 - Text: 
    *- str (Strings)
 - Zahlen: 
    *- int (ganze Zahlen)
    *- float (Gleitkommazahlen)
     - complex (komplexe Zahlen)
 - Logische Wahrheitswerte:
    *- bool (wahr / falsch)

 - Folgen
    *- list (geordnete Menge von Elementen)
     - tuple (geordnetes Menge von Elementen, unveränderlich)
     - range  (steigende Zahlenfolge mit gleichen Abständen)
 - Abbildungen
    *- dict (Wörterbuch mit Abbildung name -> Beschreibung)
     - set (ungeordnete Menge von Elementen)
     - frozenset (ungeordnete Menge von Elementen, unveränderlich) 

 - Binäre Datentypen
     - bytes
     - bytearray
     - memoryview
"""
    
# Beispiele für die *-Fälle

# Text
x = "Universität Mannheim"
type(x)

# Zahlen
a = 3
type(a)

b = 3.5
type(b)

c = 3.0
type(c)

# Casting zur expliziten Zuweisung
d = int(3.0)
type(d)

e = int(3.5)
type(e)

f = int("2")
type(f)

g = str(3)
type(g)


# Logische Wahrheitswerte

w = True
f = False
type(w)
print(bool(1))
print(bool(0))
# leere Texte, Klammern wie (), 0, None und False werden zu falsch
# alles andere zu wahr
print(bool("Text"))
print(bool(None))

# Liste
wochentage = ["mo", "di", "mi", "do", "fr", "sa", "so"]
type(wochentage)
print(wochentage[0])



# Dictionaries
wochentage = {1: "Montag", 2: "Dienstag", 3: "Mittwoch", 4: "Donnerstag",
              5: "Freitag", 6: "Samstag", 7: "Sonntag"}

print(wochentage[6])

studiengaenge = {
   "Wifo": "Wirtschaftsinformatik", 
   "Wima": "Wirtschaftsmathematik",
   "BWL": "Betriebswirtschaftslehre",
   "MMDS": "Mannheim Master in Data Science"
   }

print(studiengaenge["BWL"])