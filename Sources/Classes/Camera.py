#!/usr/bin/env python
'''
Created on Oct. 17, 2019

@author: philip
'''

from picamera import PiCamera
import time

class Camera(PiCamera):
    '''
    Classe pour les objets Camera qui héritent de la classe mère PiCamera.
    La version de PiCamera 1.13 à été inclue dans le dossier Labrary du projet.
    '''
    nom_fichier_image = "camera.jpg"

    def __init__(self):
        '''
        Constructor
        '''
        PiCamera.__init__(self)
        
    def captureImage(self):
        self.capture(self.nom_fichier_image, resize=(720,480))
        
    def GetImage(self):
        self.captureImage()
        f=open(self.nom_fichier_image, "rb") #3.7kiB in same folder
        return f.read()
        
    def ImgToByteArray(self):
        self.captureImage()
        f=open(self.nom_fichier_image, "rb") #3.7kiB in same folder
        fileContent = f.read()
        return bytearray(fileContent)
    
    def Preview(self,temps):
        self.start_preview()
        time.sleep(temps)
        self.stop_preview()
        