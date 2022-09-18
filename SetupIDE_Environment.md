# Get Started Teil 1: Setting up development environment

Die Schritte 1-3 können unabhängig voneinander durchgeführt werden. 

Wir haben dir auch zwei Videos vorbereitet, in denen die Installation erklärt wird und du siehst, wo du klicken musst.
* [Windows](https://youtu.be/qn96nt-9jaU)
* [Mac](https://youtu.be/9h5V4XxNm_4)

## Step 1: Installiere Git und trete Github Classroom bei

- Installiere [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) beschrieben und wähle die vorausgewählten Standardeinstellungen.
- Erstelle dir einen [Github-Account](https://github.com/join).

## Step 2: Installiere VS-Code als IDE

- Installiere die aktuelle Version von [VS Code](https://code.visualstudio.com) (=Visual Studio Code). Folge dazu den Installationsanweisungen für dein Betriebssystem. Führe die .exe-Datei aus, die du heruntergeladen hast und folge den Voreinstellungen im Installationsprozess.

## Step 3: Installiere Python und Poetry
- Installiere [Python Version 3.10.7](https://www.python.org/downloads/). Lade auch hier die Version für dein Betriebssystem herunter und folge (unter Windows) den Voreinstellungen beim Ausführen der .exe-Datei. Eine Einstellung musst du dabei ändern - und zwar, wenn du den Installer öffnest, wähle [beim Installer](https://docs.python.org/3/_images/win_installer.png) ```Add Python 3.8 to PATH``` aus.
- Melde dich am Computer ab und melde dich erneut an.
- Installiere [Poetry](https://python-poetry.org/docs/#installation). Folge dabei unbedingt den `osx / linux / bashonwindows install instructions` auf der Webseite.
- Melde dich am Computer ab und melde dich erneut an.
- Führe nun den folgenden Befehl im Terminal aus
    ```shell
    > poetry config virtualenvs.in-project true
    ````

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

## Step 2: Setting up VS Code Workspace
- Öffne VSCode.
- Öffne in VSCode den Ordner, in den du das repository geklont hast mit `Open Folder`, z.B. ```C:\Users\moritzkern\projects\uni\pythonkurs2020_1_get_started_%username%```
- Speichere den nun erstellten Workspace (`File > Save Workspace As...`). Gebe einen beliebigen Dateinamen z.B. `pythonkurs.code-workspace` an.
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
