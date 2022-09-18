# Conda als Paket- und Dependency-Manager

- Lade [Anaconda](https://www.anaconda.com) herunter und führe den Installationsmanager mit den Standardeinstellungen aus.
- Falls du einen Windows Rechner hast, öffne im Suchfeld "Systemumgebungsvariablen bearbeiten". Anschließend klicke auf das Feld Umgebungsvariablen. Wähle nun Path aus und klicke auf bearbeiten. Klicke auf Neu und füge den Pfad zu \anaconda3\Scripts hinzu, also z. B. "C:\Users\lucaslinden\anaconda3\Scripts". Als nächstes öffne das Terminal (cmd im Suchfeld eingeben) und gebe folgendes ein:
    ```shell
    conda init --all 
    ````
Bestätige mit Enter. Sobald der Befehl ausgeführt ist, starte das Terminal neu. 
- Nun initialisieren wir das Environment. Ab hier, müssen auch die MAC Nutzer wieder mitarbeiten ;-) Führe nacheinander folgende Befehle aus:
    ```shell
    conda create --name pythonkurs
    ````
    ```shell
    conda activate pythonkurs 
    ```
    ```shell
    conda install pip
    ```
    ```shell
    pip install -r requirements.txt
    ```
- Nun wählen wir das erzeugte Environment als Python Interpreter für unser Projekt in VSCode. Dazu wähle in der [Kommandopalette](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_command-palette) *"Select Python Interpreter"* aus und wähle nun den Interpreter im Ordner `.venv` in deinem Projektverzeichnis.
- Öffne nun im Terminal eine neue Session mit *"+"*. Das Terminal sollte jetzt im venv öffnen:
    ```shell
    (.venv)> waiting
    ```

# Installiere Dev-Dependencies
Wir installieren jetzt
* [pylint](https://www.pylint.org) zur statischen Code-Analyse
* [Jupyter Notebook](https://jupyter.org) als interaktives Coding-Notizbuch.
```
bash> poetry add pylint notebook jupyter_contrib_nbextensions --dev

Using version ^2.6.0 for pylint
Using version ^6.1.4 for notebook
Using version ^0.5.1 for jupyter_contrib_nbextensions

Updating dependencies
Resolving dependencies... (3.0s)

Writing lock file


Package operations: 62 installs, 0 updates, 0 removals

  - Installing ipython-genutils (0.2.0)
    ...
  - Installing pylint (2.6.0)
```
