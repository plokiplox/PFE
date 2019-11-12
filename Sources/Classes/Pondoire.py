#!/usr/bin/env python
'''
Created on Oct. 21, 2019

@author: philip
'''

from Classes.Capteurs import Presence
import threading.Thread
import time

class Pondoire(threading.Thread):
    '''
    Classe pour contrôler le compte d'oeufs par pondoire
    '''
    Compte = 0
    TimeoutCompteur = 8 #secondes
    
    def __init__(self, IO_CapteurPresence):
        '''
        Constructeur
        '''
        threading.Thread.__init__(self, target=self.Actions())
        self.CPresence = Presence(IO_CapteurPresence)
        
    def ResetCompte(self):
        self.Compte = 0    
        
    def IncrementerCompte(self):
        self.Compte += 1
        
    def Actions(self):
        while(True):
            if self.CPresence.LectureCapteur():
                self.IncrementerCompte()
                time.sleep(self.TimeoutCompteur)
            else:
                continue