#!/usr/bin/env python
'''
Created on Oct. 21, 2019

@author: philip
'''

from Classes.Actionneurs import ElementChauffant
from Classes.Capteurs import Temperature
import time
import threading

class Thermostat(threading.Thread):
    '''
    Classe pour contrôler la chaleur des pondoires et perchoires du poulailler
    '''
    # Degré Celsius
    Tempearture_Min = 18
    Temperature_Max = 25
    Temp = 0
    
    # Secondes
    Delai_temp = 60

    def __init__(self, IO_CapteurTemperature, IO_ElementChauffant):
        '''
        Constructeur
        '''
        threading.Thread.__init__(self, target=self.Actions())
        self.Heater = ElementChauffant(IO_ElementChauffant)
        self.CTemp = Temperature(IO_CapteurTemperature)
    
    def Rechauffer(self):
        self.Heater.Marche()
        
        while self.CTemp.GetTemperature() < self.Temperature_Max:
            time.sleep(self.Delai_temp)
            continue
        
        self.Heater.Arret()
        
    def Actions(self):
        while True:
            time.sleep(self.Delai_temp)
            if self.CTemp.GetTemperature() < self.Tempearture_Min:
                self.Heater.Marche()
                while self.CTemp.GetTemperature() < self.Temperature_Max:
                    time.sleep(self.Delai_temp)
                    continue
            continue