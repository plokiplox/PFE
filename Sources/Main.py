#!/usr/bin/env python

'''
Created on Oct. 15, 2019

@author: philip
'''
#from Classes.Poulailler import Poulailler
from Classes.Capteurs import Switch

if __name__ == '__main__':
    
    #A = Poulailler()
    #A.InitialisationThreads()
    
    Haut = Switch(27, 0.2)
    Bas = Switch(17 , 0.2)
    
    while True:
        if Haut.LectureCapteur():
            print("Porte Ouverte")
        if Bas.LectureCapteur():
            print("Porte Fermee")
        continue
    
    print("Arret du programme")
    pass