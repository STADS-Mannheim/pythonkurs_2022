########################################################################################################################
# Python Einführung - Übungen
########################################################################################################################

# Beantworte die einzelnen Fragen. Hilfe bietet dir das Handout, wenn Du nicht weiter weißt


########################################################################################################################
# Aufgabe 1
# Rechne 7^4 (7 hoch 4)?



########################################################################################################################
# Aufgabe 2
# Zerlege(split) den String:
s = "Hallo wie geht es dir heute?"
# in eine Liste  und gebe diese aus:
# Ausgabe: ['Hallo', 'wie', 'geht', 'es', 'dir', 'heute?']



########################################################################################################################
# Aufgabe 3
# Gegeben sind folgende Variablen:
stadt = "Heidelberg"
einwohner = 155000
flaeche_in_km2 = 109

# Benutze .format() um den folgenden String auszudrucken:
# Die Stadt Heidelberg hat 155000 Einwohner auf einer Flaeche von 109 Quadratkilometern.


########################################################################################################################
# Aufgabe 4
# Lass dir von dieser mehrdimensionalen Liste das Element 'hello' ausgeben
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


########################################################################################################################
# Aufgabe 5
# Lass dir von diesem mehrdimensionalen Dictionary das Element 'hello' ausgeben **
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

########################################################################################################################
# Aufgabe 6
# Was unterscheidet hauptsächlich ein Tuple von einer Liste?

# Erstelle eine Funktion mit dem Namen domainGet, die die E-Mail-Domain aus dem folgenden String extrahiert:
email = "user@domain.com"
# Hier: "user@domain.com" gibt zurück: domain.com

########################################################################################################################
# Aufgabe 7
# Erstelle eine Funktion mit dem Namen look_for_money, welche True zurück gibt, wenn das Wort 'money' in dem
# input-String enthalten ist. Großschreibung soll berücksichtigt werden, aber wenn ein Zeichen an dem Wort hängt nicht
# (Bsp: 'money,' wird nicht berücksichtigt).
# count_money('Money all I need is money Money, dude!') soll also 2 zurückgeben.


#######################################################################################################################
# Aufgabe 8
# Benutze lambda Ausdrücke und die filter() Funktion um Wörter aus einer Liste zu filtern,
# welche nicht mit dem Buchstaben 's' beginnen. Beispiel:
seq = ['schatz','freund','sind','immer','wichtig']
# soll zu folgendem gefiltert werden: ['schatz','sind']


#######################################################################################################################
# Aufgabe 9
# Du fährst ein wenig zu schnell, und ein Polizist hält dich auf. Schreibe eine Funktion, um eines von 3 möglichen
# Ergebnissen zurückzugeben: "Kein Ticket", "Kleines Ticket" oder "Grosses Ticket". Wenn deine Geschwindigkeit 100
# oder weniger beträgt, ist das Ergebnis "Kein Ticket". Wenn die Geschwindigkeit zwischen 101 und einschließlich 120
# liegt, ist das Ergebnis "Kleines Ticket". Wenn die Geschwindigkeit 121 oder mehr beträgt, ist das Ergebnis
# "Grosses Ticket". Es sei denn, es ist dein Geburtstag (kodiert als boolescher Wert in den Parametern der Funktion)
# -- an deinem Geburtstag kann deine Geschwindigkeit in allen Fällen um 10 höher sein.
# Beispiel:  caught_speeding(101, True) gibt 'Kein Ticket', aber   caught_speeding(101, False) 'Kleines Ticket'

def caught_speeding(speed, is_birthday):
    # hier dein Code!
