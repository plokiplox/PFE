#!/usr/bin/env python

'''
Created on Oct. 15, 2019

@author: philip
'''
#from Classes.Poulailler import Poulailler
from Classes.Capteurs import Presence
import time

if __name__ == '__main__':
    
    #A = Poulailler()
    #A.InitialisationThreads()
    
    motion = Presence(23)
    while True:
        if motion.motion_detected:
            print("Motion Detected")
        else:
            print("No Motion")
            
        time.sleep(1)
        continue
    pass