#!/usr/bin/env python
'''
Created on Oct. 21, 2019

@author: philip
'''

from Classes.Capteurs import Presence

class Pondoire:
    '''
    Classe pour contrôler le compte d'oeufs par pondoire
    '''
    Compte = 0
    
    def __init__(self, IO_CapteurPresence):
        '''
        Constructeur
        '''
        self.CPresence = Presence(IO_CapteurPresence)
        
    def ResetCompte(self):
        self.Compte = 0    
        
    def IncrementerCompte(self):
        self.Compte += 1