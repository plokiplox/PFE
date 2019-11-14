#!/usr/bin/env python
'''
Created on Oct. 17, 2019

@author: philip
'''

from Classes.enums import EtatPorte, Direction
from Classes.Actionneurs import Moteur, LumiereLED
from Classes.Capteurs import Switch, Obscurite, Temperature
import time
import threading

class Porte(threading.Thread):
    '''
    Classe pour contrôler la porte du poulailler
    Fermer la porte dû à la température avec les mêmes temps qu'on donne la nourriture (variables globales)
    '''
    Delai_temp = 300

    def __init__(self, IO_moteur_forward, IO_moteur_backward, IO_switch_haut, IO_switch_bas, IO_capteur_obscurite, IO_capteur_temperature):
        '''
        Constructeur
        '''
        threading.Thread.__init__(self, target=self.Actions())
        #self.Moteur_porte = Moteur(IO_moteur_forward,IO_moteur_backward)
        
        self.led_forward = LumiereLED(IO_moteur_forward)
        self.led_backward = LumiereLED(IO_moteur_backward)
        
        self.SwitchHaut = Switch(IO_switch_haut)
        self.SwitchBas = Switch(IO_switch_bas)
        self.CObscurite = Obscurite(IO_capteur_obscurite)
        self.CTemperature = Temperature(IO_capteur_temperature)
        self.SetEtat(EtatPorte.Ferme)
        
    def SetEtat(self, e):
        self.Etat = e
        
    def GetEtat(self):
        return self.Etat
    
    def Ouvrir(self):
        #self.Moteur_porte.forward()
        self.led_forward.Allumer()
        
        while not self.SwitchHaut.LectureCapteur() == True:
            time.sleep(0.5)
        else:
            self.led_forward.Fermer()
            #self.Moteur_porte.Stop()
            self.SetEtat(EtatPorte.Ouvert)
        
    def Fermer(self):
        #self.Moteur_porte.backward()
        self.led_backward.Allumer()
        
        while not self.SwitchBas.LectureCapteur() == True:
            time.sleep(0.5)
        else:
            self.led_backward.Fermer()
            #self.Moteur_porte.Stop()
            self.SetEtat(EtatPorte.Ferme)
            
    def Actions(self):
        while True:
            time.sleep(self.Delai_temp)
            
            if not self.CObscurite.LectureCapteur() and self.Etat == EtatPorte.Ferme:
                self.Ouvrir()
                
            if self.CObscurite.LectureCapteur() and self.Etat == EtatPorte.Ouvert:
                self.Fermer()
                
            continue