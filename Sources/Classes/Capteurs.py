#!/usr/bin/env python
'''
Created on Oct. 17, 2019

@author: philip

TODO
Connecter les bonnes classes de GPIOZero aux capteurs correspondants
avec les adresses IO données aux constructeurs. Sans ça nou ne pourrons
pas tester les capteurs.

Obscurité = 

'''

from gpiozero import Button, LightSensor, MotionSensor

class Capteurs(object):
    '''
    Classe mère pourt les capteurs
    '''


    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        self.SetIO(ioNumber)

    def SetIO(self, ioNumber):
        self.IO = ioNumber
        
    def GetIO(self):
        return self.IO
    
    def LectureCapteur(self):
        return True
    
class Temperature(Capteurs):
    '''
    Classe pour les capteurs de température de humidité
    '''
    
    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Capteurs.__init__(self, ioNumber)
        
    def GetTemperature(self):
        pass
    
    def GetHumidity(self):
        pass
    
class Switch(Button):
    '''
    Classe pour les switch de fin de course
    
    '''
    
    def __init__(self, ioNumber, time_held):
        '''
        Constructeur
        '''
        Button.__init__(self, pin=ioNumber,pull_up=False, hold_time=time_held)
        
    def LectureCapteur(self):
        return self.is_held
        
class Presence(MotionSensor):
    '''
    Classe pour les capteurs de présence (pour compter le nombre d'oeufs)
    '''
    
    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        MotionSensor.__init__(self, pin=ioNumber,pull_up=False,sample_rate=10)
    
    def LectureCapteur(self):
        return self.motion_detected
        
class Obscurite(LightSensor):
    '''
    Classe pour les capteurs d'obscurité
    '''
    
    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        LightSensor.__init__(self, ioNumber)
        
    def LectureCapteur(self):
        return self.light_detected
        
class Niveau(Capteurs):
    '''
    Classe pour les capteurs de niveau (eau ou nourriture)
    '''
    
    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Capteurs.__init__(self, ioNumber)