########################################################################################################################
# Aufgabe 1
# Importiere numpy als 'np'
# Importiere pandas als 'pd'


########################################################################################################################
# Aufgabe 2
# Lade aus der Datei `02_pandas-excelbsp.xlsx` das Sheet `BL_7-Tage-Inzidenz` als `pd.DataFrame` ein.
# Verwende das Argument `index_col=0`, um die Bundesländer als Index zu setzen für die Zeilen.


########################################################################################################################
# Aufgabe 3
# Lasse dir die ersten 5 Zeilen anzeigen (Tipp: head)


########################################################################################################################
# Aufgabe 4
# Lasse dir alle Indizenzen für den 13. Oktober (2020-10-13) ausgeben
# ...


########################################################################################################################
# Aufgabe 5
# Lasse dir das Bundesland ausgeben, in dem die höchste Inzidenz geherrscht hat am 13. Oktober
# Tipp: idxmax()


########################################################################################################################
# Aufgabe 6
# Lasse dir für Baden-Württemberg die Zahlen von 01. Oktober bis einschließlich 15. Oktober ausgeben
# Tipp: df.loc[...][...:...]


########################################################################################################################
# Aufgabe 7
# Gruppiere nach Wochentagen (Mo-Fr), und bilde den jeweiligen Mittelwert über alle Observationen an dem Wochentag für jedes Bundesland
# Tipp: df.columns.weekday, axis=1, mean
# ...


########################################################################################################################
# Aufgabe 8
# Verwende das Ergebnis des letzten Schritts und berechne den Mittelwert über alle Bundesländer für die jeweiligen Wochentage
# Tipp: groupby, mean
# ...


########################################################################################################################
# Aufgabe 9
# Logarithmiere alle Werte im Datensatz und speichere ihn als df_log
# Tipp: apply, np.log
df_log = # ...


########################################################################################################################
# Aufgabe 10
# Berechne nun die Differenz der logarithmierten Werte von einem auf den nächsten Tag
# Tipp: diff, axis=1
df_logdiff = df.diff(axis=1)


########################################################################################################################
# Aufgabe 11
# Berechne nun den Mittelwert für jedes Bundesland über alle Beobachtungen
# Tipp: mean, axis=1, skipna=True
# ...


########################################################################################################################
# Aufgabe 12
# Berechne nun den Median für jedes Bundesland über alle Beobachtungen
# Tipp: median, axis=1, skipna=True
df_logdiff.median(axis=1, skipna=True)



