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

#from gpiozero import Button, LightSensor, MotionSensor
#import Adafruit_DHT

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
    TODO
    '''
    
    #sensor = Adafruit_DHT.DHT11
    
    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Capteurs.__init__(self, ioNumber)
        
    def GetTemperature(self):
        #humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.GetIO())
        #return temperature
        pass
    
    def GetHumidity(self):
        #humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.GetIO())
        #return humidity
        pass
    
class Switch(Capteurs):
    '''
    Classe pour les switch de fin de course
    
    '''
    
    def __init__(self, ioNumber, time_held):
        '''
        Constructeur
        '''
        Capteurs.__init__(self, ioNumber)
        #Button.__init__(self, pin=ioNumber,pull_up=False, hold_time=time_held)
        
    def LectureCapteur(self):
        #return self.is_held
        pass
        
class Presence(Capteurs):
    '''
    Classe pour les capteurs de présence (pour compter le nombre d'oeufs)
    '''
    
    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Capteurs.__init__(self, ioNumber)
        #MotionSensor.__init__(self, pin=ioNumber,pull_up=False, queue_len=1, threshold=0.5)
    
    def LectureCapteur(self):
        #return self.motion_detected
        pass
        
class Obscurite(Capteurs):
    '''
    Classe pour les capteurs d'obscurité
    '''
    
    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Capteurs.__init__(self, ioNumber)
        #LightSensor.__init__(self, ioNumber)
        
    def LectureCapteur(self):
        #return not self.light_detected
        pass
        
class Niveau(Capteurs):
    '''
    Classe pour les capteurs de niveau (eau ou nourriture)
    '''
    
    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Capteurs.__init__(self, ioNumber)