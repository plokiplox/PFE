#!/usr/bin/env python

'''
Created on Oct. 15, 2019

@author: philip
'''
#from Classes.Poulailler import Poulailler
from Classes.Capteurs import Obscurite

if __name__ == '__main__':
    
    #A = Poulailler()
    #A.InitialisationThreads()
    
    O = Obscurite(9)
    print(O.LectureCapteur())
    
    pass