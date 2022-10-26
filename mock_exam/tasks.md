# Übungsklausur

* Klausurtyp: Open-Book-Exam. 
* Bearbeitungszeit: 45 Minuten (+ 10 Minuten für Download & Upload)
* Erreichbare Punkte: 45
* Bestehensgrenze: 25 Punkte

Der Code muss in Python >=3.8.5 mit numpy >=1.19.2, pandas >=1.1.3, matplotlib >=3.3.2, seaborn >=0.11.0 bzw. plotly >=4.12.0 lauffähig sein. Falls weitere Pakete oder andere Versionen verwendet werden, muss die jeweilige Version angegeben werden.

## Aufgabe 1: Grundlagen  *(18 Punkte)*
* Erstellen Sie eine Python-Datei mit dem Namen `<Nachname>_<Vorname>_mockexam.py` (z.B. `musterman_max_mockexam.py`) und bearbeiten in dieser Datei die Aufgabe.

### Aufgabe 1a: Get Started *(2 Punkte)*

* Definieren Sie die beiden Variablen `a` und `b` als `3` bzw. `5` *(1 Punkt)*
* Geben Sie das Ergebnis von (a-b)/(a+b) aus. (Tipp: print) *(1 Punkt)*

### Aufgabe 1b: Einfache Funktion *(6 Punkte)*

* Definieren Sie eine Funktion `berechnung`, die die Variablen `a` und `b` als Input hat.  *(1 Punkt)*
* Die Funktion soll prüfen, ob die Summe von `a` und `b` gleich 0 ist, 
    *falls dies der Fall ist: Printe `a+b muss ungleich 0 sein.` und gebe `None` zurück. *(2 Punkte)*
    * andernfalls, gebe das Ergebnis von  `(a-b)/(a+b)` zurück. *(2 Punkte)*
* Werten Sie die Funktion aus für die Inputkombination  (a=0, b=0) und (a=1, b=2) *(1 Punkt)*


### Aufgabe 1c: Datentypen *(6 Punkte)*


* Erstellen Sie eine Variable `x` als Float mit dem Wert 0. *(1 Punkt)*
* Definieren Sie die variable `x_is_float` als `TRUE`, falls `x` vom Typ `float`, andernfalls als `FALSE`. Tipp: Verwenden Sie dazu die Funktion `isinstance`. *(1 Punkt)*
* Erstellen Sie ein `dictionary` mit dem Namen `farben` mit folgendem Mapping *(3 Punkte)*
    * "red" -> (255, 0, 0)
    * "green" -> (0, 255, 0)
    * "blue" -> (0, 0, 255)
* Lassen Sie sich das Element mit dem Key `green` ausgeben. *(1 Punkt)*

### Aufgabe 1d: Schleifen *(4 Punkte)*
* Erstellen Sie mit einer for-Schleife folgende Ausgabe (... ausgeschrieben) *(4 Punkte)*
    ```
    1
    12
    123
    1234
    ...
    123456789
    ```

## Aufgabe 2: Wichtige Pakete *(27 Punkte)*

### Aufgabe 2a: Numpy *(7 Punkte)*
* Erstellen Sie geschickt einen Vektor `v`, der wie folgt aussieht. *(1 Punkt)*
    ```
    [  0,   4,   8,  12,  16, ..., 196]
    ```
* Erstellen Sie eine Matrix `m` der Dimension (50,50), die auf ihren Diagonalen überall eine 1 hat sonst nur Nullen. *(1 Punkt)*
* Setzen Sie das letzte Element rechts unten in der Matrix `m` auf `NA`. *(1 Punkt)*
* Initialisieren Sie einen Zufallszahlengenerator. *(1 Punkt)*
* Verwenden Sie den Zufallszahlengenerator, um einen Vektor `z` der Dimension (1,50) mit unabhängig normalverteilten Zufallsvariablen zu erzeugen. *(1 Punkt)*
* Wenden Sie elementenweise die Exponentialfuktion auf `z` an und speichern Sie den Vektor als `z_exp`. *(1 Punkte)*
* Berechnen Sie mit das Matrixprodukt von `z_exp` und `m`. *(1 Punkt)*

### Aufgabe 2b: Pandas Basics *(9 Punkte)*

Für diese Aufgabe benötigen Sie den Datensatz [pendler.csv](pendler.csv).

* Importieren Sie den Datensatz `pendler.csv`. *Tipp:* Setzen Sie die folgenden Parameter beim Import mit Pandas `sep=";"` und  `thousands="."`. *(2 Punkte)*
* Lassen Sie sich die ersten 5 Zeilen ausgeben. *(1 Punkt)*
* Aus wie vielen Zeilen und Spalten besteht der Datensatz? *(1 Punkt)*
* Löschen Sie die Spalte `Gemeindekennziffer` und setzen Sie die Spalte `Name` als Index. Speichern Sie den so erhaltenen Datensatz ab und verwenden ihn für die folgenden Aufgaben. *(2 Punkte)*
* Erstellen Sie eine neue Spalte `Nettopendler`, die sich als Differenz aus der Spalte `Einpendler` und `Auspendler` ergibt. *(1 Punkt)*
* Geben Sie die 5 Städte aus mit den größten Nettopendlern. Wie viele Nettopendler hat Mannheim? *(2 Punkte)*

### Aufgabe 2c: Pandas Advanced *(6 Punkte)*
* Erstellen Sie eine neue Spalte `Einpendlerquote`, indem Sie die Spalte `Einpendler` durch `Erwerbstaetige_am_Arbeitsort` teilen. *(1 Punkt)*
* Geben Sie die Korrelation zwischen  `Erwerbstaetige_am_Arbeitsort` und `Einpendlerquote` an. *(2 Punkte)*
* Filtern Sie den Datensatz nach Städten mit mindestens 10.000 Erwerbstätigen am Arbeitsort. Welcher Ort hat die höchste Einpendlerquote? Wie hoch ist diese Quote? *(3 Punkte)*


### Aufgabe 2d: Grafiken *(5 Punkte)*

* Erstellen Sie einen Scatterplot mit den Einpendlern auf der x-Achse und den Auspendlern auf der y-Achse. Sie dürfen dabei ein Paket Ihrer Wahl verwenden (z.B. Pandas, Matplotlib, Seaborn, Plotly). *(5 Punkte)*

## Abgabe

Senden Sie die *beiden* von Ihnen erstellten Dateien bis Abgabeschluss per E-Mail an [kurse@stads.de](mailto:kurse@stads.de).
