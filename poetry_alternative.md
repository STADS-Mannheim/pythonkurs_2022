# Vorgehen wenn poetry nicht funktioniert

## 1. erstelle manuell ein Virtual environment
öffne neues terminal
```shell
> python -m venv env
```
(falls python --version 2.7. ausgibt verwende: python3 -m venv env)

## 2. aktiviere es
Mac:
```shell
> source env/bin/activate
```
Windows
```shell
> env\Scripts\activate
```
\
File > Save Workspace As ...
## Libraries Installieren
wenn die virtuelle Umgebung aktiviert ist (am Anfang der Zeile steht (env))

```shell
> pip install -r requirements.txt
```
einzelne Pakete können einfach über
```shell
> pip install numpy
```
installiert werden  


