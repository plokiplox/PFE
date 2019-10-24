#!/usr/bin/env python
'''
Created on Oct. 21, 2019

@author: philip
'''

from Classes.enums import Niveaux
from Classes.Actionneurs import Moteur
from Classes.Capteurs import Niveau
from Classes.Actionneurs import Sirene
import time

class Distribution_Nourriture:
    '''
    Classe pour contrôler le système de distribution d'eau dans le poulailler
    '''
    
    Niveau_Nourriture = Niveaux.Haut
    # Compté en secondes 
    Quantite_Nourriture = 5

    def __init__(self, IO_Moteur, IO_CNiveau_Haut, IO_CNiveau_Bas, IO_Sirene):
        '''
        Constructeur
        '''
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
        