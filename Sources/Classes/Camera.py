#!/usr/bin/env python
'''
Created on Oct. 17, 2019

@author: philip
'''

from Library.picamera import PiCamera

class Camera(PiCamera):
    '''
    Classe pour les objets Camera qui héritent de la classe mère PiCamera.
    La version de PiCamera 1.13 à été inclue dans le dossier Labrary du projet.
    '''

    def __init__(self):
        '''
        Constructor
        '''