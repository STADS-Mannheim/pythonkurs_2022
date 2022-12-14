# Projekt aktualisieren 

Nachdem wir nun unsere Entwicklungsumgebung aufgesetzt haben und ein Projekt in PyCharm initialisiert haben, können wir nun mit dem Inhalt des Kurses starten. Ich werde wöchentlich die neuen Lectures in dieses Repo hochladen. Bitte ladet diese vor der Vorlesung runter und fügt sie in euer PyCharm Projekt hinzu. Im Folgenden findet ihr nochmal eine Erklärung, wie dies funktioniert.

## 1. Schritt: Repo klonen
Wir haben bereits in der ersten Woche einmal das Repo geklont. Damit ihr stets alle Daten habt, müsst ihr es wöchentlich neu klonen. Dazu geht ihr wieder wie folgt vor:
* Öffnet euer Terminal / Commnand Prompt.
* Navigiert mit cd in den Ordner, in dem ihr das Projekt abspeichern wollt. Wenn ihr denselben Ordner wie bei der letzten Vorlesung nutzen wollt, müsst ihr den Ordner pythonkurs_2022 löschen, damit das Repo neu geklont werden kann. Beispiel: Ich möchte die Dateien in /Users/lucaslinden/Pythonkurs abspeichern. Also öffne ich das Terminal und gebe cd /Users/lucaslinden/Pythonkurs ein. Nun kann ich hierhin die Dateien klonen,
* Dazu gebe ich nun im dritten Schritt im Terminal ```git clone https://github.com/STADS-Mannheim/pythonkurs_2022.git```ein.
* Wenn das Klonen erfolgreich war, solltest du einen Ouptut wie diesen im Terminal / der Command Prompt sehen:
```
Klone nach 'pythonkurs_2022'...
remote: Enumerating objects: 469, done.
remote: Counting objects: 100% (428/428), done.
remote: Compressing objects: 100% (219/219), done.
remote: Total 469 (delta 255), reused 320 (delta 206), pack-reused 41
Empfange Objekte: 100% (469/469), 21.02 MiB | 12.38 MiB/s, fertig.
Löse Unterschiede auf: 100% (259/259), fertig.
```

## 2. Schritt: Füge die neuen Dateien zu deinem PyCharm Projekt hinzu
* Wenn du das Repo wie vorher beschrieben, an den selben Ort geklont hast, solltest du nun fertig sein. Du kannst dies einfach checken, indem du dein PyCharm Projekt öffnest und nachschaust, ob die neuen Dateien vorhanden sind. Falls dem nicht so ist, führe die folgenden Schritte aus:
* Öffne das Projekt, was wir letzte Woche erstellt haben, in PyCharm.
* Klicke auf File > Open. Dann navigiere zu dem Ort, wo du das geklonte Repository abgespeichert hast. Öffne den Ordner pythonkurs_2022 und klicke einmal auf den lecture Ordner, den du hinzufügen möchtest. Klicke auf open.
* Nun öffnet sich ein weiteres Fenster mit dem Titel Open Project. Wähle hier die Option Attach. 


## Anaconda und Jupyter Notebooks 
Im Ordner von Lecture 2 findet ihr Dateien mit der Endung .ipynb. Bei diesen Dateien handelt es sich um Jupyter Notebooks. In PyCharm Community Edition habt ihr leider nur Lesezugriff auf diese. Mithilfe von Anaconda könnt ihr diese Dateien auch bearbeiten. Dazu müsst ihr das Programm Anaconda Navigator öffnen. Nachdem dieser geöffnet ist, klickt ihr bei jupyter notebook auf launch. Nun öffnet sich das Terminal und anschließend euer Internet Explorer. Im Reiter Files könnt ihr nun zu euren ipynb Dateien steuern und diese öffnen. Diese könnt ihr im Folgenden bearbeiten und ausführen.


