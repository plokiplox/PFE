#!/usr/bin/env python
'''
Created on Oct. 21, 2019

@author: philip
'''

from Classes.enums import Niveaux
from Classes.Actionneurs import Moteur
from Classes.Capteurs import Niveau
from Classes.Actionneurs import Sirene
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
    Quantite_Nourriture = 30
    Delai_entre_repas = 7200 # 2 heures = 7200 secondes
    Delai_update_temps = 300

    def __init__(self, IO_Moteur, IO_CNiveau_Haut, IO_CNiveau_Bas, IO_Sirene):
        '''
        Constructeur
        '''
        threading.Thread.__init__(self)
        self.Moteur = Moteur(IO_Moteur)
        self.CNiveau_Haut = Niveau(IO_CNiveau_Haut)
        self.CNiveau_Bas = Niveau(IO_CNiveau_Bas)
        self.Sirene = Sirene(IO_Sirene)
        
    def SetQuantite(self, Secondes):
        self.Quantite_Nourriture=Secondes
        
    def DistribuerNourriture(self):
        self.Moteur.Marche()
        
        while self.CTemp_Reservoire.GetTemperature() < self.Temperature_Max:
            time.sleep(self.Delai_temp)
        
        self.Moteur.Arret()
        
    def Actions(self):
        while True:
            now = datetime.datetime.now()
            if now.hour >= self.Heure_premier_repas and now.hour <= self.Heure_dernier_repas:
                self.Sirene.Marche()
                self.DistribuerNourriture()
                self.Sirene.Arret()
                time.sleep(self.Delai_entre_repas)
            else:
                time.sleep(self.Delai_update_temps)
            continue
        
    def run(self):
        self.Actions()