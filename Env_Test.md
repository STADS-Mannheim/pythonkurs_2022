# Check your Environment 

In Vorbereitung auf unsere nächste Vorlesung möchte ich euch bitten, einmal zu testen ob die Installation der Packages beim Aufsetzen des Environments funktioniert hat. 

## Öffne unser Projekt in PyCharm 
Öffne dein Pyhtonkurs Projekt in PyCharm und klicke anschließend unten auf die Python Console. Gebe in der Konsole folgendes ein:
``` import numpy as np ```
Falls dir keine Fehlermeldung angezeigt wird, hat alles funktioniert und du bist für die nächste Vorlesung ready. Falls das Paket nicht gefunden werden kann und dir eine Fehlermeldung ausgegeben wird, gibt es zwei Möglichkeiten, wieso dies nicht funktioniert.

## 1. Möglichkeit: Du hast in PyCharm nicht den richtigen Interpreter konfiguriert
Wenn du dein Projekt in PyCharm geöffnet hast, findest du in der rechten unteren Ecke eine Leiste. Falls in dieser Leiste nur z. B. Python 3.9 steht, hast du deinen Interpreter nicht gesetzt. KLicke darauf, nun sollten dir andere Interpreter angezeigt werden. Unter anderem auch den Interpreter, den wir mit unserem Environment erstellt haben. Wähle diesen aus. Nun sollte PyCharm kurz laden. Danach kannst du Schritt 1 wiederholen und testen, ob es nun funktioniert. 

Theoretisch könnte es auch sein, dass du nur in der Pyhton Konsole den falschen Interpreter hast. Um dies zu testen, öffne bitte in PyCharm die Einstellungen. Klicke anschließend auf Build, Execution, Deployment. Dann auf Console > Python Console. Wähle bei Python Interpreter unser conda environment aus. 


## 2. Möglichkeit: Dein Environment ist leer

Öffne das Terminal / die Command Prompt (in Windows cmd eingeben) und gebe folgendes ins Terminal ein: 

```conda activate pythonkurs``` 

pythonkurs ist hier der Name deines Environments. Falls du dieses anderes benannt haben solltet, musst du natürlich pythonkurs durch deinen Namen ersetzen.

Gebe den Befehl 

```conda list``` 

aus. Als Output wird dir eine Liste mit installierten Packages angezeigt. Falls du dort numpy nicht findest, führe nun folgenden Befehl aus: 

```pip install -r C:\Users\Lucas\Documents\requirements.txt``` 

wobei du den Pfad am Ende natürlich durch den Pfad zum Speicherort deiner Requirements Datei ersetzen musst (diese findest du in dem Ordner, in den du das Repo geklont hast). Falls dies nicht funktioniert, musst du ggf. zuerst noch ```conda install pip``` ausführen. 

## 3. Falls alles nicht funktioniert....
...schreib mir bitte bis Sonntag Abend eine Mail und wir organisieren nochmal eine Sprechstunde. 

Die gute Nachricht ist, wenn das funktioniert, sollte es für den Rest des Kurses keine technischen Probleme mehr geben ;-)



