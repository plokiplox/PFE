'''
Created on Oct. 17, 2019

@author: philip
'''

from Classes.enums import EtatPorte
from Classes.Actionneurs import Moteur
from Classes.Capteurs import Switch

class Porte(object):
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
    
    