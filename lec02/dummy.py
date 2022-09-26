import os
class Auto:
    max_tempo=240
    min_tempo=0      # class Attribute werden außerhalb von init definiert (z.B. globale Konstanten für alle Instanzen einer Klasse)
    def __init__(self, modell, entf_zum_ziel, tempo=100, sound='hup, '): 
        self.modell=modell 
        self.dist = entf_zum_ziel
        self.tempo=tempo
        self.sound= sound         
    
    def hupen(self,anzahl):
        out = self.sound*anzahl
        os.system('say {}'.format(out))
        print(out)
    def berechne_zeit(self, ausgabe=True):
        zeit= self.dist / self.tempo  # t = s/v
        if ausgabe:
            print('die Geschätzte Reisedauer beträgt {} Stunden'.format(zeit))
        return zeit