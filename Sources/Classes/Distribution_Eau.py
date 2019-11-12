#!/usr/bin/env python
'''
Created on Oct. 21, 2019

@author: philip
'''

from Classes.enums import Niveaux
from Classes.Actionneurs import ElementChauffant
from Classes.Actionneurs import ElectroVanne
from Classes.Capteurs import Temperature
from Classes.Capteurs import Niveau
import threading.Thread
import time

class Distribution_Eau(threading.Thread):
    '''
    Classe pour contrôler le système de distribution d'eau dans le poulailler
    '''
    
    Niveau_Eau = Niveaux.Haut
    # Degré Celsius
    Tempearture_Reservoire_Min = 3
    Temperature_Reservoire_Max = 8
    # Secondes
    Delai_temps_heater = 5
    Delai_temps_remplissage = 1

    def __init__(self, IO_HeaterReservoire,IO_CTemp_Reservoire,IO_HeaterCanalisation, IO_CTemp_Canalisation, IO_ElectroVanne, IO_CNiveau_Haut, IO_CNiveau_Bas):
        '''
        Constructeur
        '''
        threading.Thread.__init__(self, target=self.Actions())
        
        self.Vanne = ElectroVanne(IO_ElectroVanne)
        
        self.Heater_Reservoire = ElementChauffant(IO_HeaterReservoire)
        self.CTemp_Reservoire = Temperature(IO_CTemp_Reservoire)
        
        self.Heater_Canalisation = ElementChauffant(IO_HeaterCanalisation)
        self.CTemp_Canalisation = Temperature(IO_CTemp_Canalisation)
        
        self.CNiveau_Haut = Niveau(IO_CNiveau_Haut)
        self.CNiveau_Bas = Niveau(IO_CNiveau_Bas)
        
    def RechaufferReservoire(self):
        self.Heater_Reservoire.Marche()
        
        while self.CTemp_Reservoire.GetTemperature() < self.Temperature_Max:
            time.sleep(self.Delai_temps_heater)
        
        self.Heater_Reservoire.Arret()
        
    def RechaufferCanalisation(self):
        self.Heater_Canalisation.Marche()
        
        while self.CTemp_Canalisation.GetTemperature() < self.Temperature_Max:
            time.sleep(self.Delai_temps_heater)
        
        self.Heater_Canalisation.Arret()
    
    def RemplirReservoire(self):
        self.Vanne.Ouverture()
        
        while not self.CNiveau_Haut.LectureCapteur():
            time.sleep(self.Delai_temps_remplissage)
            
        self.Vanne.Fermeture()
    
    def Actions(self):
        
        while True:
            if not self.CNiveau_Bas:
                self.RechaufferCanalisation()
                self.RemplirReservoire()
            else:
                if self.CTemp_Reservoire.GetTemperature() < self.Tempearture_Reservoire_Min:
                    self.RechaufferReservoire()
        continue
        