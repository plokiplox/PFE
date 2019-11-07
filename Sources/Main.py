#!/usr/bin/env python

'''
Created on Oct. 15, 2019

@author: philip
'''
#from Classes.Poulailler import Poulailler
from Classes.Capteurs import Obscurite
from Classes.Actionneurs import LumiereLED
import time

if __name__ == '__main__':
    
    #A = Poulailler()
    #A.InitialisationThreads()
    
    light = Obscurite(25)
    led = LumiereLED(24)
    
    while True:
        if light.LectureCapteur():
            led.Allumer()
            print("Light Detected")
        else:
            led.Fermer()
            print("No Light")
            
        time.sleep(1)
        continue
    pass