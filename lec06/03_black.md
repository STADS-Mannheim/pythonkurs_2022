# Code Formattierung mit Black

`black` ist ein automatische Code-Formattierer, der den Code nach einer Untermenge des PEP 8 Standards formattiert.

`black` kann wieder installiert werden via `poetry add black` oder `pip install black`.


## Beispiel

Folgenden Code speichern wir als `lec06/03_black_formatted.py`.

```python
"""
An diesem Beispiel kann man das Reformatting von Black sehen.
"""

import pandas as pd; import numpy as np


def any_function(x):
    i=0
    
    while i<10:
     print(f'Aktuelle Zahl: {i}')
     i=i=1


dictionary = {1: 'ein sehr langer string steht beispielsweise hier in diesem dictionary',
2: np.array([[1,2,3,4,5,6], [10,11,12,13,14,15,16]]),
3: lambda x: x**3}
```
Wir führen die Formattierung mit Black aus
```bash
(.venv)> black lec06/05_black_formatted.py 
reformatted lec06/05_black_formatted.py
All done! ✨ 🍰 ✨
1 file reformatted.
```
Unsere Datei wird mit dem formattierten Code überschrieben und sieht jetzt wie folgt aus:
```python
"""
An diesem Beispiel kann man das Reformatting von Black sehen.
"""

import pandas as pd
import numpy as np


def any_function(x):
    i = 0

    while i < 10:
        print(f"Aktuelle Zahl: {i}")
        i = i = 1


dictionary = {
    1: "ein sehr langer string steht beispielsweise hier in diesem dictionary",
    2: np.array([[1, 2, 3, 4, 5, 6], [10, 11, 12, 13, 14, 15, 16]]),
    3: lambda x: x ** 3,
}
```

Black kann beispielsweise auch in VSCode als Formatter on Save eingestellt werden oder
in Precommit integriert werden.