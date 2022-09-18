# Installiere Python über pyenv

## 1. Vorbereitung
### installiere [Homebrew](https://brew.sh):

```shell
> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
### installiere Python build dependencies 

```shell
> xcode-select --install)
```

```shell
> brew install openssl readline sqlite3 xz zlib
```

## 2. Installiere pyenv mit Homebrew
```shell
> brew install pyenv
```

Führe folgende Befehle im Terminal (zsh) aus:

```shell
> echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
```
```shell
> echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

... und starte ein neues Terminal Fenster.

## 3. installiere Python versionen (hier 3.10.7)

```shell
> pyenv install 2.7.8
```
setze Python3.8.5 als globale oder lokale 'Standardversion'

```shell
> pyenv global 3.10.7
```

## 4. check
```shell
> python --version
Python 3.10.7
```
