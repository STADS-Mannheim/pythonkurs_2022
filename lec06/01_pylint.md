# Pylint


# Über pylint

`pylint` ist ein hilfreiches Tool, das
* die Übereinstimmung mit dem Codingstandard prüft, d.h.
    * Zeilenlänge prüft,
    * Variablennamen nach Codingstandard prüft, 
    * den Import nicht verwendeter Module prüft.
* Fehler findet, d.h.
    * prüft, ob die deklarierten Interfaces richtig implementiert sind
    * den Import verwendeter module prüft.
    * ...
* beim Refactoring unterstützt.

Der Coding-Standard nachdem `pylint` prüft orientiert sich dabei an 
[PEP 8](https://www.python.org/dev/peps/pep-0008/), 
dem Style Guide für Python Code. Dabei steht "PEP" für "Python Enhancement Proposals".

# Installation von pylint 

Öffne das Terminal und aktiviere dein Environment mit 
```conda activate pythonkurs```. Anschließend installiere pylint mit ```pip install pylint```. Gebe als nächstes ```which pylint``` bzw. ```where pylint``` ein und kopiere den ausgegebenen Pfad. Nun öffne [https://stackoverflow.com/questions/38134086/how-to-run-pylint-with-pycharm](PyCharm). Navigiere zu PyCharm > Preferences > Tools > External Tools. Nun klicke auf das + Symbol und ergänze pylint. Ergänze die Felder wie folgt:
- Name: pylint
- Description: Pylint as an external tool
- Program: Dein kopierter Pfad (Speicherort von Pylint)
- Arguments /Parameters: ```$FilePath$```
- Working Directory: ``` $ProjectFileDir$ ```

# Erstes Beispiel

Wir legen eine Datei `lec06/ex02_pylint_example.py` mit folgendem Inhalt an.
```python
def quicksort(arr):
    print('Ich werde gerade aufgerufen.')
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    Left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if False:
        print("Tritt niemals ein")
    return quicksort(Left) + middle + quicksort(right)
```
    
Jetzt führen wir im Terminal folgenden Befehl aus und erhalten als Output

```bash
(.venv)> pylint lec06/ex02_pylint_example.py
************* Module ex02_pylint_example
lec06/ex02_pylint_example.py:1:0: C0114: Missing module docstring (missing-module-docstring)
lec06/ex02_pylint_example.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
lec06/ex02_pylint_example.py:6:4: C0103: Variable name "Left" doesn't conform to snake_case naming style (invalid-name)
lec06/ex02_pylint_example.py:9:4: W0125: Using a conditional statement with a constant value (using-constant-test)

-------------------------------------------------------------------
Your code has been rated at 6.36/10 (previous run: 10.00/10, -3.64)
```
Wenn wir uns jetzt dafür interessieren, was mit der Fehlermeldung genau gemeint ist, können wir ausführen
    
```bash
(.venv)> pylint --help-msg=missing-module-docstring
:missing-module-docstring (C0114): *Missing module docstring*
Used when a module has no docstring.Empty modules do not require a docstring.
This message belongs to the basic checker.
```

