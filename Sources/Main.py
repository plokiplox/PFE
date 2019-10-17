#!/usr/bin/env python

'''
Created on Oct. 15, 2019

@author: philip
'''
from Classes.Porte import Porte

if __name__ == '__main__':
    
    A = Porte(23,1,2)
    
    print(A.GetEtat())
    print(A.Moteur_porte.GetIO())
    print(A.SwitchHaut.GetIO())
    
    pass