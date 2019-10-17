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
    Ouvert = True
    Ferme = False
    
class Niveau(Enum):
    Haut = True
    Bas = False