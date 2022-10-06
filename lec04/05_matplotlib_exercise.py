# Matplotlib Uebungen 

# Nehmt euch hierfuer nun Zeit, Matplotlib kann anfangs schwierig zu verstehen sein. Dies sind relativ einfache Diagramme, 
# aber es trotzdem nicht einfach, wenn man das erste Mal mit matplotlib arbeitet. Außerdem keine Sorge, falls ihr die Syntax von Matplotlib 
# frustrierend findet. Wir werden als naechstes Seaborn kennenlernen. Seaborn ist weitaus handlicher und perfekt fuer Data Science Anwendungen. 
# Seaborn baut allerdings auf matplotlib auf, weswegen es wichtig ist matplotlib kennengelernt zu haben.

# HINWEIS: ALLE BEFEHLE ZUM PLOTTEN EINER FIGUR SOLLTEN SICH ALLE IN DERSELBEN ZELLE BEFINDEN. DIE TRENNUNG IN MEHRERE ZELLEN KANN DAZU FUEHREN, DASS NICHTS ERSCHEINT.

# Übungen
# Folge den Anweisungen, um die Diagramme mit diesen Daten neu zu erstellen:

# Daten

import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2

# Importiere matplotlib.pyplot als plt.
import matplotlib.pyplot as plt

########################################################################################################################
# Aufgabe 1
# Führe diese Schritte aus:
    # - Erstelle ein Figure-Objekt namens fig mit plt.figure().
    # - Verwende add_axes, um eine Achse zur Figuren-Leinwand bei [0,0,1,1] hinzuzufuegen. Nenne diese neue Achse ax.
    # - Plotte (x,y) auf den Achsen und waehle als Beschriftung die Werte von x (20er Schritte) und y (25er Schritte). Füge
    #   als Titel 'Titel' hinzu.


########################################################################################################################
# Aufgabe 2
# 2a)
# Erstelle ein Figurenobjekt und setze zwei Achsen darauf, ax1 und ax2. ax1 bei [0,0,1,1] und ax2 bei [0.2,0.5,.2,.2].


# 2b)
# Plotte nun (x,y) auf beiden Achsen. Und rufe dein Figurenobjekt auf, um es zu zeigen.


########################################################################################################################
# Aufgabe 3
# Erstelle eine Darstellung, indem du zwei Achsen zu einem Figurenobjekt bei[0,0,1,1] und[0.2,0.5,.4,.4] hinzufuegst.


########################################################################################################################
# Aufgabe 4
# 4a)
# Verwende plt.subplots(nrows=1, ncols=2), um eine Darstellung mit zwei Plots zu erstellen, die horizontal nebeneinander sind. Wähle als Werte für 
# x und y 0 bis 1.0 (0.2er Schritte).


# 4b)
# Plotte nun (x,y) und (x,z) auf den Achsen. Spiele mit der Linienbreite und dem Stil herum. Außerdem sorge dafuer,
# dass es keine Ueberlappung gibt.


# 4c)
# Ueberpruefe, ob du die Groesse der Darstellung aendern kannst, indem du das Argument figsize() in plt.subplots()
# hinzufuegst. Kopiere deinen vorherigen Code**
