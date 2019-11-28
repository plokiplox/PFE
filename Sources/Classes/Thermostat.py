#!/usr/bin/env python
'''
Created on Oct. 21, 2019

@author: philip
'''

from Classes.Actionneurs import ElementChauffant, LumiereLED
from Classes.Capteurs import Temperature
import time
import threading

class Thermostat(threading.Thread):
    '''
    Classe pour contrôler la chaleur des pondoires et perchoires du poulailler
    '''
    
    # Degré Celsius
    Tempearture_Min = 23
    Temperature_Max = 24
    Temp = 0
    
    # Secondes
    Delai_temp = 5

    def __init__(self, IO_CapteurTemperature, IO_ElementChauffant):
        '''
        Constructeur
        '''
        #self.Heater = ElementChauffant(IO_ElementChauffant)
        self.Heater = LumiereLED(IO_ElementChauffant)
        self.CTemp = Temperature(IO_CapteurTemperature)
        threading.Thread.__init__(self)
        self.daemon = True
    
    def Rechauffer(self,t):
        self.Heater.Allumer()
        #print("Allumer Heater")
        while t < self.Temperature_Max:
            t = self.CTemp.GetTemperature()
            #print("Temperature = ",t)
            time.sleep(self.Delai_temp)
            continue
        #print("Fermer Heater")
        self.Heater.Fermer()
        
    def Actions(self):
        while True:
            time.sleep(self.Delai_temp)
            t = self.CTemp.GetTemperature()
            #print("Temperature = ",t)
            if t <= self.Tempearture_Min:
                self.Rechauffer(t)
            #else:
                #print("Temperature adequate")
        #continue
        
    def run(self):
        self.Actions()
