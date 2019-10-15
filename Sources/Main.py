'''
Created on Oct. 15, 2019

@author: philip
'''
from Classes.Moteur import Moteur

if __name__ == '__main__':
    
    A = Moteur(23)
    
    print(A.GetIO())
    print(A.GetEtat())
    print(A.GetSens())
    
    pass