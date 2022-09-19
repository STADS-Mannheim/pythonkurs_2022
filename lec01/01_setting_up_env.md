# Conda als Paket- und Dependency-Manager

- Lade [Anaconda](https://www.anaconda.com) herunter und führe den Installationsmanager mit den Standardeinstellungen aus.
- Falls du einen Windows Rechner hast, öffne im Suchfeld "Systemumgebungsvariablen bearbeiten". Anschließend klicke auf das Feld Umgebungsvariablen. Wähle nun Path aus und klicke auf bearbeiten. Klicke auf Neu und füge den Pfad zu \anaconda3\Scripts hinzu, also z. B. "C:\Users\lucaslinden\anaconda3\Scripts". Als nächstes öffne das Terminal (cmd im Suchfeld eingeben) und gebe folgendes ein:
    ```shell
    conda init --all 
    ````
Bestätige mit Enter. Sobald der Befehl ausgeführt ist, starte das Terminal neu. 
- Nun initialisieren wir das Environment. Ab hier, müssen auch die MAC Nutzer wieder mitarbeiten ;-) Führe nacheinander folgende Befehle aus (Falls die Meldung Proceed ([y]/n)? erscheint, gebe y ein und bestätige mit Enter):
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
- Als letztes wollen wir noch jupyter zu unserem Environment hinzufügen. Dazu führe den Befehl
    ```shell
    conda install jupyter 
    ```
  aus. Super, nun ist unser environment bereit und wir können das Terminal schließen. 
- Jetzt wählen wir das erzeugte Environment als Python Interpreter für unser Projekt in PyCharm. Dazu öffnen wir Pycharm und erstellen ein neues Projekt. Wähle den Reiter "Pure Python" und passe im Location Feld den Namen zu Pfad + "\Pythonkurs" an. Als nächstes wählen wir unser conda environment aus. Klicke hierzu auf den Reiter Python Interpreter und wähle "Previously configured interpreter" aus. Klicke auf Add Interpreter, anschließend auf Add local interpreter. Nun wähle Conda Environment aus. Wähle unser environment pythonkurs aus und klicke auf ok. Entferne den Haken bei Create a main.py welcome script und klicke auf create. Super, du hast nun dein erstes PyCharm Projekt erstellt.
- Zulezt wollen wir noch den Interpreter für die console einstellen. Klicke hierzu auf PyCharm > Preferences > Build, Execution, Deployment > Console > Python Console und wähle als Interpreter unser Environment aus.  

