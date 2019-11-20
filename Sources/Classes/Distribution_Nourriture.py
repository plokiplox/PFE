#!/usr/bin/env python
'''
Created on Oct. 21, 2019

@author: philip
'''

from Classes.enums import Niveaux
from Classes.Actionneurs import Moteur, Sirene, LumiereLED
from Classes.Capteurs import Niveau, Switch
import threading
import datetime
import time

class Distribution_Nourriture(threading.Thread):
    '''
    Classe pour contrôler le système de distribution d'eau dans le poulailler
    '''
    
    Niveau_Nourriture = Niveaux.Haut
    
    Heure_premier_repas = 6  # 6 heure du matin
    Heure_dernier_repas = 19 # 7 heure du soir
    
    # Compté en secondes 
    Quantite_Nourriture = 5
    Delai_entre_repas = 10 # 2 heures = 7200 secondes
    Delai_update_temps = 5

    def __init__(self, IO_Moteur, IO_CNiveau_Haut, IO_CNiveau_Bas, IO_Sirene):
        '''
        Constructeur
        '''
        threading.Thread.__init__(self)
        self.Moteur = LumiereLED(IO_Moteur)
        self.CNiveau_Haut = Switch(IO_CNiveau_Haut,0)
        self.CNiveau_Bas = Switch(IO_CNiveau_Bas,0)
        self.Sirene = LumiereLED(IO_Sirene)
        
    def SetQuantite(self, Secondes):
        self.Quantite_Nourriture=Secondes
        
    def DistribuerNourriture(self):
        self.Moteur.Allumer()
        print("Distribution nourriture")
        time.sleep(self.Quantite_Nourriture)
        self.Moteur.Fermer()
        print("Arreter la distribution de nourriture")
        
    def Actions(self):
        while True:
            now = datetime.datetime.now()
            if now.hour >= self.Heure_premier_repas and now.hour <= self.Heure_dernier_repas:
                self.Sirene.Allumer()
                self.DistribuerNourriture()
                self.Sirene.Fermer()
                time.sleep(self.Delai_entre_repas)
            else:
                time.sleep(self.Delai_update_temps)
            continue
        
    def run(self):
        self.Actions()