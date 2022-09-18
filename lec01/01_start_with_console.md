# Start mit Python Console

Nutze das in PyCharm integrierte Terminal. 

Gebe im Terminal je nach Betriebssystem (ausprobieren) ein

```shell
> where python
```
oder
```shell
> which python
```

Anschließend solltest du alle angezeigt bekommen, wo dein Betriebssystem eine Python-Installation findet. Falls die Liste leer ist, dann ist bei der Installation was schiefgelaufen.

Wir checken nun, dass wir die richtige Python Version 3.8.5 installiert haben, indem wir ins Terminal eingeben
```shell
bash> python --version
Python 3.8.5

bash> #dies ist vorerst auch in Ordnung
bash> python --version 
Python 2.7.16
bash> python3 --version
Python 3.8.5

```
Nun starten wir Python, indem wir `python` ins Terminal eingeben. Jetzt wird Python ausgeführt und du solltest folgenden (oder einen ähnlichen) Konsolenoutput erhalten.

```shell
bash> python
Python 3.8.5 (default, Aug 22 2020, 10:36:09) 
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

## Fehlerbehandlung: 
Falls nicht die richtige Python-Version gefunden wird, dann muss in den Umgebungsvariablen unter Windows hinzugefügt werden in die PATH-Variable ganz oben `C:\Users\%username%\AppData\Local\Programs\Python-38-32\python.exe`. Anschließend abmelden und wieder neu anmelden.\
Für Mac-User führt folgenden Befehl im Terminal aus und startet ein neues Terminal Fenster:
echo -n 'export PATH="/Library/Frameworks/Python.framework/Versions/3.8/bin:${PATH}"' >> ~/.zshrc

Falls immer noch fehler auftreten, versucht es mit [pyenv](https://github.com/pyenv/pyenv#readme) bzw. für windows [pyenv](https://github.com/pyenv-win/pyenv-win#readme).\
pyenv ist das empfohlene und gängigste Tool zum einfachen Verwalten globaler und lokaler Python Versionen.  
Hier eine kurze pyenv [Anleitung](pyenv.md) für macOS.

# Python als Taschenrechner

Gebe nun in Python eine einfache Rechnung ein und du solltest folgenden Output erhalten.

```python
>>> 1+2
3
```

Führe nun folgende Rechnung in der Pythonkonsole aus

$$\left(\frac{1}{3} * 5 + 7.3 \right)^2$$
```python
>>> (1/3 * 5 + 7.3)**2
80.4011111111111
```

# Variablen in Python 

Variablen können per Gleichheitszeichen zugewiesen werden und mit ihnen gerechnet werden.

```python
>>> x = 1
>>> print(x)
1
>>> y = 3
>>> x + y
4
```
Das ganze geht natürlich auch für Text.

```python
>>> abc = "Dies ist ein Text"
>>> print(abc)
Dies ist ein Text
```

und für boolsche Werte

```python
>>> is_weekday = True
>>> print(is_weekday)
True
```

Ein wenig **Hintergrundwissen** zu Variablen in Python:

- Im Gegensatz zu anderen Programmiersprachen gibt es in Python kein Kommando um Variablen zu deklarieren. Eine Variable wird in dem Moment, in dem ihr der erste Wert zugewiesen wird, erzeugt. 

- Variablen müssen nicht mit einem speziellen Typ deklariert werden, der Typ ergibt sich aus dem Wert, der ihr zugewiesen wird. Der Typ einer Variablen ist nicht fix und kann verändert werden.


Wie dürfen wir Variablen benennen?
- Variable muss mit Buchstabe oder Unterstrich beginnen.
- Variable darf nicht mit Ziffer beginnen
- Variablen dürfen sich nur aus alphanumerische Zeichen und Unterstrichen zusammensetzen
- Variablen sind Groß- und Kleinschreibungs sensitiv

# Python schließen
Abschließend schließen wir die interaktive Pythoninstanz.
```bash
>>>exit()
bash>
```
