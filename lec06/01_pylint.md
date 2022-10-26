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
```conda activate pythonkurs```. Anschließend installiere pylint mit ```pip install pylint```. Gebe als nächstes ```which pylint``` bzw. ```where pylint``` ein und kopiere den ausgegebenen Pfad. Nun öffne PyCharm. Navigiere zu PyCharm > Preferences > Tools > External Tools. Nun klicke auf das + Symbol und ergänze pylint. Ergänze die Felder wie folgt:
- Name: pylint
- Description: Pylint as an external tool
- Program: Dein kopierter Pfad (Speicherort von Pylint)
- Arguments /Parameters: ```$FilePath$```
- Working Directory: ``` $ProjectFileDir$ ```

Eine detailierte Beschreibung mit Bildern findest du auch [hier](https://stackoverflow.com/questions/38134086/how-to-run-pylint-with-pycharm).
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
    
Jetzt klicken wir in PyCharm mit rechts auf die Datei ec06/ex02_pylint_example.py und steuern zu External Tools > pylint. Wir erhalten folgenden Output:

```bash
************* Module 02_pylint_example
lec06/02_pylint_example.py:1:0: C0114: Missing module docstring (missing-module-docstring)
lec06/02_pylint_example.py:1:0: C0103: Module name "02_pylint_example" doesn't conform to snake_case naming style (invalid-name)
lec06/02_pylint_example.py:3:0: W0611: Unused numpy imported as np (unused-import)

------------------------------------------------------------------
Your code has been rated at 7.00/10 (previous run: 7.00/10, +0.00)
```
Wenn wir uns jetzt dafür interessieren, was mit der Fehlermeldung genau gemeint ist, können wir im Terminal folgdendes ausführen
    
```bash
(.venv)> pylint --help-msg=missing-module-docstring
:missing-module-docstring (C0114): *Missing module docstring*
Used when a module has no docstring.Empty modules do not require a docstring.
This message belongs to the basic checker.
```

