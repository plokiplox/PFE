#!/usr/bin/env python
'''
Created on Oct. 15, 2019

@author: philip

TODO
Connecter les bonnes classes de GPIOZero aux capteurs correspondants
avec les adresses IO données aux constructeurs. Sans ça nou ne pourrons
pas tester les actionneurs.

'''

from Classes.enums import EtatActionneurs
from Classes.enums import Direction
from Classes.enums import EtatPorte

class Actionneurs:
    '''
    --------------
    Classe mère pour tous les actionneurs
    --------------
    Variables
    IO (integer) : Numéro du connecteur
    Etat (Booléen) : Marche / Arrêt (Choisi de l'énumération EtatActionneurs)
    --------------
    '''

    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        self.IO = ioNumber
        self.SetEtat(EtatActionneurs.Arret)
    pass

    def SetEtat(self, e):
        self.Etat = e

    def GetEtat(self):
        return self.Etat

    def GetIO(self):
        return self.IO;
    
    
class Moteur(Actionneurs):
    '''
    --------------
    Classe pour les objets de type Moteur, classe enfant de la classe Actionneurs.
    --------------
    Variables
    Sens (Booléen) : Ouverture / Fermeture (Choisi de l'énumération Direction)
    --------------
    '''

    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Actionneurs.__init__(self, ioNumber)
        self.SetSens(Direction.Fermeture)
    
    def SetSens(self, s):
        self.Sens = s
    
    def GetSens(self):
        return self.Sens
    
    def Marche(self):
        self.SetEtat(EtatPorte.Ouvert)
    
    def Arret(self):
        self.SetEtat(EtatPorte.Ferme)
    
class ElementChauffant(Actionneurs):
    '''
    --------------
    Classe pour les objets de type ElementChauffant, classe enfant de la classe Actionneurs.
    --------------
    Variables
    --------------
    '''

    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Actionneurs.__init__(self, ioNumber)
    
    def Marche(self):
        self.SetEtat(EtatActionneurs.Marche)
    
    def Arret(self):
        self.SetEtat(EtatActionneurs.Arret)
    
class ElectroVanne(Actionneurs):
    '''
    --------------
    Classe pour les objets de type ElectroVanne, classe enfant de la classe Actionneurs.
    --------------
    Variables
    --------------
    '''

    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Actionneurs.__init__(self, ioNumber)
    
    def Ouverture(self):
        self.SetEtat(EtatPorte.Ouvert)
    
    def Fermeture(self):
        self.SetEtat(EtatPorte.Ferme)