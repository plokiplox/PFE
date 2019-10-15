'''
Created on Oct. 15, 2019

@author: philip
'''
from Classes.Actionneurs import Actionneurs
from Classes.enums import EtatActionneurs
from Classes.enums import Direction

class Moteur(Actionneurs):
    '''
    --------------
    Classe pour les objets de type Moteur, classe enfant de la classe Actionneurs.
    --------------
    Variables
    Etat (Booléen) : Marche / Arrêt (Choisi de l'énumération EtatActionneurs)
    Sens (Booléen) : Ouverture / Fermeture (Choisi de l'énumération Direction)
    --------------
    '''

    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Actionneurs.__init__(self, ioNumber)
        self.Etat = EtatActionneurs.Arret
        self.Sens = Direction.Ouverture
        pass
    
    def SetEtat(self, e):
        self.Etat = e
        pass
    
    def GetEtat(self):
        return self.Etat
    
    def SetSens(self, s):
        self.Sens = s
        pass
    
    def GetSens(self):
        return self.Sens