# Get Started Teil 1: Setting up development environment

Die Schritte 1-3 können unabhängig voneinander durchgeführt werden. 

Wir haben dir auch zwei Videos vorbereitet, in denen die Installation erklärt wird und du siehst, wo du klicken musst.
* [Windows](https://youtu.be/qn96nt-9jaU)
* [Mac](https://youtu.be/9h5V4XxNm_4)

## Step 1: Installiere Git und trete Github Classroom bei

- Installiere [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) beschrieben und wähle die vorausgewählten Standardeinstellungen.
- Erstelle dir einen [Github-Account](https://github.com/join).

## Step 2: Installiere PyCharm als IDE

- Installiere die aktuelle Version von [PyCharm Community Edition](https://www.jetbrains.com/de-de/pycharm). Folge dazu den Installationsanweisungen für dein Betriebssystem. Führe die .exe-Datei aus, die du heruntergeladen hast und folge den Voreinstellungen im Installationsprozess.

## Step 3: Installiere Python und Anaconda 
- Installiere [Python Version 3.10.7](https://www.python.org/downloads/). Lade auch hier die Version für dein Betriebssystem herunter und folge (unter Windows) den Voreinstellungen beim Ausführen der .exe-Datei. Eine Einstellung musst du dabei ändern - und zwar, wenn du den Installer öffnest, wähle [beim Installer](https://docs.python.org/3/_images/win_installer.png) ```Add Python 3.10 to PATH``` aus.
- Melde dich am Computer ab und melde dich erneut an.
- Lade [Anaconda](https://www.anaconda.com) herunter. Nach dem Download führe die exe Datei aus und übernehme die empfohlenen Einstellungen. 
- Melde dich am Computer ab und melde dich erneut an. 
- Bevor wir nun das Terminal erstellen, müssen Windows Nutzer einen zusätzlichen Schritt durchführen (für Mac nicht relevant). Öffne in der Suchleiste Systemumgebungsvariablen bearbeiten. Anschließend klicke auf das Feld Umgebungsvariablen. Wähle nun Path aus und klicke auf bearbeiten. Klicke auf Neu und füge den Pfad zu "dein Pfad" + \anaconda3\Scripts hinzu. Anschließend klicke auf ok und schließe die Einstellungen wieder. Nun musst du dein Terminal öffnen (gebe dazu cmd im Suchfeld ein und bestätige mit Enter). Führe den Befehl conda init --all mit Enter aus. 
- Nun erstellen wir unser conda environment. Öffne dazu dein Terminal (wieder) und gebe folgendes ein: conda create --name pythonkurs. Führe den Befehl mit Enter aus. Wenn du die Meldung Proceed ([y]/n)? erhältst, gebe y ein.
- Super, nun haben wir unser environment erstellt. Zunächst wollen wir dieses öffnen. Gebe dafür in der Konsole conda activate pythonkurs ein. Im Terminal erkennst du nun, dass du das environment geöffnet hast. 
- Im nächsten Schritt wollen wir unser environment mit all den Packages befüllen, die wir im Verlauf des Kurses benötigen. Lade dafür die Requirements.txt Datei herunter und führe folgende Befehle im Terminal aus: conda install pip und anschließend conda install -r "Pfad zur requirements Datei".
- Abschließend installieren wir noch jupyter. Führe dazu den Befehl conda install jupyter aus. 
- Glückwunsch, du hast nun dein conda environment installiert. Schließe es wieder mit conda deactivate. Nun kannst du das Terminal schließen. 
 
# Get Started Teil 2: Setting up Pythonkurs Projekt


## Step 1: Clone Repository
- Erzeuge dir das Assignment Repository im [Classroom](https://classroom.github.com/a/DmEOgn_0). Ggfs. musst du dich noch beim Vorgang authentifizieren.
- Öffne die Git Bash (oder das Terminal) und navigiere mit `cd` zum Ordner, in dem du dein Pythonkurs-Repository ablegen möchtest, z.B.
    ```shell
    > cd C:\Users\moritzkern\projects\uni
    ```
- Klone unser das eben erzeugte Repository wie folgt. Ersetze dabei %githubname% durch den Namen des erzeugten Repositories. Den Namen des Repositories siehst du, wenn du auf `Code`in Github klickst.
    ```shell
    > git clone https://github.com/STADS-Mannheim/%repositoryname%
    ```
    Du wirst nach deinem Github Nutzernamen und -Passwort gefragt und musst die beiden eingeben.

## Step 2: Setting up PyCharm Workspace
- Öffne PyCharm.
- Erstelle ein neues Projekt, indem du auf New Project klickst.
- Wähle den Reiter "Pure Python" und passe im Location Feld den Namen zu Pfad + "\Pythonkurs" an.
- Als nächstes wählen wir unser conda environment aus. Klicke hierzu auf den Reiter Python Interpreter und wähle "Previously configured interpreter" aus. Wenn du auf den Auswahlpfeil klickst, sollte dir dein environment pythonkurs angezeigt werden. Wähle dieses aus und klicke auf create. Falls dir das environment nicht angezeigt wirst, musst du die python Datei in deinem environment Ordner manuell auswählen.
- Öffne in PyCharm den Ordner, in den du das Repository geklont hast mit `File > Open Folder`, z.B. ```C:\Users\moritzkern\projects\uni\pythonkurs2020_1_get_started_%username%```
- Installiere die folgenden Extensions in VSCode aus dem Extension Marketplace.  
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [Live Share Extension Pack](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack)
    - Wenn du den Links hier folgst, musst du einmal im Browser und einmal in VS Code den grünen `Install` Button drücken und dazwischen die entsprechenden Freigaben bei Aufforderung erteilen.

## Step 3: Installiere das Poetry-Projekt

- Öffne in VSCode das Terminal (`Terminal -> New Terminal`). Wähle dabei unter Windows nicht die Powershell, das könnte zu Problemen führen. Führe `poetry install` aus.
    ```shell
    > poetry install
    Creating virtualenv pythonkurs2020-part1 in C:\Users\moritzkern\projects\uni\pythonkurs2020_1_get_started\.venv
    Installing dependencies from lock file

    Package operations: 62 installs, 0 updates, 0 removals

    - Installing ipython-genutils (0.2.0)
    ...
    ```


Herzlichen Glückwunsch, du hast das Setup abgeschlossen und alle technischen Voraussetzungen für den Pythonkurs sind geschaffen! :)
