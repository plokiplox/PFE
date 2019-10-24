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
    
class Switch(Capteurs):
    '''
    Classe pour les switch de fin de course
    '''
    
    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Capteurs.__init__(self, ioNumber)
        
class Presence(Capteurs):
    '''
    Classe pour les capteurs de présence (pour compter le nombre d'oeufs)
    '''
    
    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Capteurs.__init__(self, ioNumber)
        
class Obscurite(Capteurs):
    '''
    Classe pour les capteurs d'obscurité
    '''
    
    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        
        Capteurs.__init__(self, ioNumber)
        
class Niveau(Capteurs):
    '''
    Classe pour les capteurs de niveau (eau ou nourriture)
    '''
    
    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        Capteurs.__init__(self, ioNumber)