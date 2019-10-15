'''
Created on Oct. 15, 2019

@author: philip
'''

class Actionneurs:
    '''
    --------------
    Classe mère pour tous les actionneurs
    --------------
    Variables
    IO (integer) : Numéro du connecteur
    --------------
    '''

    def __init__(self, ioNumber):
        '''
        Constructeur
        '''
        self.IO = ioNumber
    pass

    def GetIO(self):
        return self.IO;