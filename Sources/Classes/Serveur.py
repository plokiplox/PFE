'''
Created on Nov. 12, 2019

@author: philip
'''

from Classes.Poulailler import Poulailler

class Serveur(object):
    '''
    classdocs
    '''
    _Poulailler = Poulailler()

    def __init__(self):
        '''
        Constructor
        '''
        
    def __start__(self):
        self._Poulailler.InitialisationThreads()