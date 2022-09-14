# Doc Strings und Doc Tests

Docstrings sind zum dokumentieren von Funktionen und Modulen, Klassen und Methoden gedacht. 
Auch diese sind wieder in den PEPs geregelt, genauer in [PEP 257](https://www.python.org/dev/peps/pep-0257/).

## Einzeiler

```python
def beispielfunktion():
    """This function prints example.""""
    print("example")
```

Hinweis: Dreifache Anführungszeichen werden auch bei Einzeilern verwendet.

Es gibt verschiedene Docstring Styles, wir werden hier die [Google Docstring Guide](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) vorstellen.

## Ausführlichere Doku

Bei komplizierteren Funktionen oder Funktionen, die exportiert werden, 
empfehlen wir euch eine Doku zu schreiben. Ihr findet diese Funktion auch direkt 
als [Pythonfile](07_docstringtest.md).

```python
def dichte(x: float, mean: float = 0, variance: float = 1, log: bool = False):
    """
    Calculates the density of a normally distributed random variable.

    Given the mean and the variance this function uses numpy to return the
    density of a normally distributed random variable or the logarithm of it.
    The default arguments are set to the density of the normal distribution.

    Args:
        mean:
            Default 0. mean parameter of random variable
        variance:
            Default 1. variance parameter of random variable. Must be positive.
            Be aware that the variance is the standarddeviation squared.
        log:
            Default False. If True, the log density (log likelihood) is
            returned.

    Returns:
        The (log of the) density as float.

    Examples:
        Examples should be written in the doctest format and should illustrate
        how to use the function.
        >>> dichte(0)
        0.3989422804014327
        >>> dichte(0, log=True)
        -0.9189385332046727
        >>> dichte(0.5, mean=1, variance=2**2)
        0.19637862681301155
        >>> dichte(x=0, variance=0)
        Traceback (most recent call last):
        ...
        Exception: Variance must be positive
    """
    if variance <= 0:
        raise Exception("Variance must be positive")

    density = (
        1
        / np.sqrt(2 * np.pi * variance)
        * np.exp(-0.5 * (x - mean) ** 2 / (2 * variance))
    )

    if log:
        density = np.log(density)

    return density
```


### Docstrings Test

Die Beispiele in den Docstrings können wir direkt verwenden als Tests.

```shell
(.venv)> python -m doctest -v lec06/07_docstring_test.py
...
4 passed and 0 failed.
Test passed.
```