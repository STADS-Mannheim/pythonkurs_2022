# Poetry als Paket- und Dependency-Manager

- Installiere [Anaconda](https://python-poetry.org/docs/#installation](https://www.anaconda.com). Folge den Standardeinstellungen der exe Datei.
- Führe nun die folgenden Befehle im Terminal aus.
    ```shell
    conda create --name pythonkurs 
    ````
- Jetzt initialisiere das virtuelle Environment
    ```shell
    shell> poetry install
    Creating virtualenv pythonkurs2020-part1 in /%path_to_folder%/pythonkurs2020_1_get_started/.venv
    Installing dependencies from lock file

    No dependencies to install or update
    ```
    *(alternativ) Falls du alternativ ein neues Paket initialisiertst, verwende folgenden Befehl*
    ```shell
    shell> poetry init
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
