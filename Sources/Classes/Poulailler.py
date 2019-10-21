#!/usr/bin/env python
'''
Created on Oct. 21, 2019

@author: philip
'''

from Classes.Camera import Camera
from Classes.Thermostat import Thermostat
from Classes.Porte import Porte
from Classes.Distribution_Eau import Distribution_Eau
from Classes.Distribution_Nourriture import Distribution_Nourriture
from Classes.Pondoire import Pondoire

class Poulailler:
    '''
    Classe qui inclu toutes les autres classes qui forment un poulailler
    '''
    
    _Camera = Camera()
    _Thermostat = Thermostat(1,2)
    _Porte = Porte(3,4,5)
    _Distribution_Eau = Distribution_Eau(6,7,8,9,10,11,12)
    _Distribution_Nourriture = Distribution_Nourriture(13,14,15)
    _Pondoires = [Pondoire(16),Pondoire(17)]

    def __init__(self):
        '''
        Constructeur
        '''
    
    def InitialisationThreads(self):
        self._Thermostat.start()
        self._Thermostat.join()
        pass
    
    
    