#!/usr/bin/env python
'''
Created on Oct. 17, 2019

@author: philip
'''

from Classes.enums import EtatPorte
from Classes.enums import Direction
from Classes.Actionneurs import Moteur
from Classes.Capteurs import Switch
import time

class Porte:
    '''
    Classe pour contrôler la porte du poulailler
    '''

    def __init__(self, IO_moteur, IO_switch_haut, IO_switch_bas):
        '''
        Constructeur
        '''
        self.Moteur_porte = Moteur(IO_moteur)
        self.SwitchHaut = Switch(IO_switch_haut)
        self.SwitchBas = Switch(IO_switch_bas)
        self.SetEtat(EtatPorte.Ferme)
        
    def SetEtat(self, e):
        self.Etat = e
        
    def GetEtat(self):
        return self.Etat
    
    def Ouvrir(self):
        self.Moteur_porte.SetSens(Direction.Ouverture)
        self.Moteur_porte.Marche()
        
        while not self.SwitchHaut.LectureCapteur() == True:
            time.sleep(0.5)
        else:
            self.Moteur_porte.Arret()
        
    def Fermer(self):
        self.Moteur_porte.SetSens(Direction.Fermeture)
        self.Moteur_porte.Marche()
        
        while not self.SwitchBas.LectureCapteur() == True:
            time.sleep(0.5)
        else:
            self.Moteur_porte.Arret()