'''
Created on Nov. 12, 2019

@author: philip
'''

import Classes.Poulailler

class Serveur:
    '''
    classdocs
    '''
    _Poulailler = Classes.Poulailler()

    def __init__(self, params):
        '''
        Constructor
        '''
        
        
    def __start__(self):
        self._Poulailler.InitialisationThreads()