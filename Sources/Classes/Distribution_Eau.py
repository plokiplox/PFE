#!/usr/bin/env python
'''
Created on Oct. 21, 2019

@author: philip
'''

from Classes.enums import Niveaux
from Classes.Actionneurs import ElementChauffant, ElectroVanne, LumiereLED
from Classes.Capteurs import Temperature, Niveau, Switch
import threading
import time

class Distribution_Eau(threading.Thread):
    '''
    Classe pour contrôler le système de distribution d'eau dans le poulailler
    '''
    
    Niveau_Eau = Niveaux.Haut
    # Degré Celsius
    Tempearture_Canalisation_Max = 25
    Tempearture_Reservoire_Min = 23
    Temperature_Reservoire_Max = 24
    # Secondes
    Temps_Rechauffage_Canalisation = 10
    Delai_temps_heater = 5
    Delai_temps_remplissage = 1

    def __init__(self, IO_HeaterReservoire,IO_CTemp_Reservoire,IO_HeaterCanalisation, IO_CTemp_Canalisation, IO_ElectroVanne, IO_CNiveau_Haut, IO_CNiveau_Bas):
        '''
        Constructeur
        '''
        threading.Thread.__init__(self)
        
        self.Vanne = LumiereLED(IO_ElectroVanne)
        
        self.Heater_Reservoire = LumiereLED(IO_HeaterReservoire)
        self.CTemp_Reservoire = Temperature(IO_CTemp_Reservoire)
        
        self.Heater_Canalisation = LumiereLED(IO_HeaterCanalisation)
        self.CTemp_Canalisation = Temperature(IO_CTemp_Canalisation)
        
        self.CNiveau_Haut = Switch(IO_CNiveau_Haut,0)
        self.CNiveau_Bas = Switch(IO_CNiveau_Bas,0)
        
    def RechaufferReservoire(self):
        self.Heater_Reservoire.Allumer()
        
        while self.CTemp_Reservoire.GetTemperature() < self.Temperature_Reservoire_Max:
            time.sleep(self.Delai_temps_heater)
        
        self.Heater_Reservoire.Fermer()
        
    def RechaufferCanalisation(self):
        if self.CTemp_Canalisation.GetTemperature() < self.Tempearture_Canalisation_Max:
            self.Heater_Canalisation.Allumer()
#             print("Rechauffer canalisation")
            time.sleep(self.Temps_Rechauffage_Canalisation)
            self.Heater_Canalisation.Fermer()
#             print("Arreter rechauffement canalisation")
        else:
#             print("Trop chaud pour rechauffer canalisation")
            pass
    
    def RemplirReservoire(self):
        self.Vanne.Allumer()
#         print("Remplir Reservoir")
        while not self.CNiveau_Haut.LectureCapteur():
            time.sleep(self.Delai_temps_remplissage)
#         print("Reservoir plein")
        self.Vanne.Fermer()
    
    def Actions(self):
        
        while True:
            if not self.CNiveau_Bas.LectureCapteur():
                self.RechaufferCanalisation()
                self.RemplirReservoire()
            else:
                if self.CTemp_Reservoire.GetTemperature() <= self.Tempearture_Reservoire_Min:
                    self.RechaufferReservoire()
            continue
    
    def run(self):
        self.Actions()