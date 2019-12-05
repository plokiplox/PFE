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
    
    _Camera = Camera()
    
    # Thermostat(IO_CapteurTemperature, IO_ElementChauffant)
    _Thermostat = Thermostat(4,10)
    
    # Porte(IO_moteur_forward, IO_moteur_backward, IO_switch_haut, IO_switch_bas, IO_capteur_obscurite, IO_capteur_temperature)
    _Porte = Porte(9,11,27,17,22,26)
    
    # Distribution_Eau(IO_HeaterReservoire,IO_CTemp_Reservoire,IO_HeaterCanalisation, IO_CTemp_Canalisation, IO_ElectroVanne, IO_CNiveau_Haut, IO_CNiveau_Bas)
    _Distribution_Eau = Distribution_Eau(6,4,5,26,12,19,13)
    
    # Distribution_Nourriture(IO_Moteur, IO_CNiveau_Haut, IO_CNiveau_Bas, IO_Sirene)
    _Distribution_Nourriture = Distribution_Nourriture(16,8,7,24)
    
    # Pondoire(IO_CapteurPresence)
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
        self._Distribution_Eau.start()
        self._Distribution_Nourriture.start()
        
        # Init des threads pondoire (boulce pour partir tous les pondoires)
        #for i in self._Pondoires:
        #    i.start()
        #    continue
        
        pass
    
    
    