"""
An diesem Beispiel kann man das Reformatting von Black sehen.
"""

import pandas as pd
import numpy as np


def any_function(x):
    i = 0

    while i < 10:
        print(f"Aktuelle Zahl: {i}")
        i = i + 1


dictionary = {
    1: "ein sehr langer string steht beispielsweise hier in diesem dictionary",
    2: np.array([[1, 2, 3, 4, 5, 6], [10, 11, 12, 13, 14, 15, 16]]),
    3: lambda x: x ** 3,
}
