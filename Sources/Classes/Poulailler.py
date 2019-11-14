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

class Poulailler(object):
    '''
    Classe qui inclu toutes les autres classes qui forment un poulailler
    La porte ne dois pas ouvrir si le thermomètre de dehors est à -5 degré
    '''
    
    #_Camera = Camera()
    _Thermostat = Thermostat(4,10)
    _Porte = Porte(9,11,27,17,22,26)
    #_Distribution_Eau = Distribution_Eau(6,7,8,9,10,11,12)
    #_Distribution_Nourriture = Distribution_Nourriture(13,14,15,00)
    _Pondoires = Pondoire(23)

    def __init__(self):
        '''
        Constructeur
        '''
    
    def InitialisationThreads(self):
        # Init du thread thermostat
        self._Porte.start()
        self._Thermostat.start()
        self._Pondoires.start()
        
        # Init des threads pondoire (boulce pour partir tous les pondoires)
        #for i in self._Pondoires:
        #    i.start()
        #    continue
        
        self._Porte.join()
        self._Thermostat.join()
        self._Pondoires.join()

        
        # Init du thread de distribution d'eau
        #self._Distribution_Eau.start()
        #self._Distribution_Eau.join()
        
        pass
    
    
    