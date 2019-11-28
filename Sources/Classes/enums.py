#!/usr/bin/env python
'''
Created on Oct. 15, 2019

@author: philip
'''

from enum import Enum

class EtatActionneurs(Enum):
    Marche = True
    Arret = False
    
class Direction(Enum):
    Ouverture = True
    Fermeture = False
    
class EtatPorte(Enum):
    Ouvert = 1
    Ferme = 0
    
class ModePorte(Enum):
    Automatique = 1
    Manuel = 0
    
class Niveaux(Enum):
    Haut = True
    Bas = False