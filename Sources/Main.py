#!/usr/bin/env python

'''
Created on Oct. 15, 2019

@author: philip
'''
#from Classes.Poulailler import Poulailler
from Classes.Capteurs import Presence
from Classes.Actionneurs import LumiereLED
import time

if __name__ == '__main__':
    
    #A = Poulailler()
    #A.InitialisationThreads()
    
    motion = Presence(23)
    led = LumiereLED(24)
    
    while True:
        if motion.motion_detected:
            led.Allumer()
            print("Motion Detected")
        else:
            led.Fermer()
            print("No Motion")
            
        time.sleep(1)
        continue
    pass