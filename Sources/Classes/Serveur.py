'''
Created on Nov. 12, 2019

@author: philip
'''

from Classes.Poulailler import Poulailler
from Classes.enums import EtatPorte, ModePorte
import threading
import paho.mqtt.client as mqtt
import time

'''
    Pour l'application sur Android nous allons utiliser IoT MQTT Panel : https://play.google.com/store/apps/details?id=snr.lab.iotmqttpanel.prod
    Car cette application nous permet de faire des graphiques et aussi nous permet d'exporter les
    configurations faites (pas besoin de les refaires pour chaque téléphone).
'''

# Fonction est appelée lors de la connection d'un client
def on_connect(client, userdata, flags, rc):
    # On check la réponse du serveur pour que ça soit correcte
    if rc == 0:
        client.connected_flag = True
        print("Vous êtes maintenant connecté: {}".format(mqtt.connack_string(rc)))
    else:
        raise IOError("La connection au serveur MQTT à retournée l'erreur suivante :{}".format(mqtt.connack_string(rc)))
    pass

# Fonction qui sera utilisée pour publier les messages
def publish_value(client, topic, value):
    result = client.publish(topic=topic, payload=value, qos=2)
    return result

class Serveur:
    '''
    classdocs
    '''
    # Informations sur le MQTT Broker que nous allons utiliser
    # pour une liste complète de broker publics visiter : https://github.com/mqtt/mqtt.github.io/wiki/public_brokers
    broker_address = "broker.hivemq.com"
    broker_port = 1883
    
    _client = mqtt.Client(protocol=mqtt.MQTTv311)
    _Poulailler = Poulailler()
    _thread_Publish_TempHumi = threading.Thread()
    _thread_Publish_Camera = threading.Thread()
    _thread_Publish_Restant = threading.Thread()

    def __init__(self):
        '''
        Constructor
        '''
        
    def PublishInit(self):
        publish_value(self._client, "switch_porte", self._Poulailler._Porte.GetEtat())
        publish_value(self._client, "mode_porte", self._Poulailler._Porte.Mode)
        
    def BouclePublishTempHumi(self):
        while True:
            self.PublierTempHumi()
            print("Publié temp")
            continue
        
    def BouclePublishRestant(self):
        while True:
            self.PublierRestant()
            print("Publié restant")
            time.sleep(1)
            continue     
        
    def BouclePublishCamera(self):
        while True:
            self.PublierCamera()
            print("Publié camera")
            #self._Poulailler._Camera.Preview(2)
            time.sleep(5)
            continue     
        
    def PublierTempHumi(self):
        publish_value(self._client, "Temp_In", self._Poulailler._Distribution_Eau.CTemp_Reservoire.GetTemperature())
        publish_value(self._client, "Temp_Out", self._Poulailler._Distribution_Eau.CTemp_Canalisation.GetTemperature())
        publish_value(self._client, "Humi_In", self._Poulailler._Distribution_Eau.CTemp_Reservoire.GetHumidity())
        publish_value(self._client, "Humi_Out", self._Poulailler._Distribution_Eau.CTemp_Canalisation.GetHumidity())

    def PublierRestant(self):
        publish_value(self._client, "Etat_porte", self._Poulailler._Porte.GetEtat())
        publish_value(self._client, "Compte_Oeufs", self._Poulailler._Pondoires.Compte)
        
    def PublierCamera(self):
        self._client.loop_start()
        publish_value(self._client, "camera_poulailler", self._Poulailler._Camera.ImgToByteArray())
        self._client.loop_stop()
        
    def on_message(self, client, userdata, message):
        payload = int(message.payload.decode("utf-8"))
        topic = str(message.topic)
        
        if message.topic == "reset_compte_oeufs":
            print("Reset compte oeufs")
            self._Poulailler._Pondoires.ResetCompte()
        elif message.topic == "mode_porte":
            self._Poulailler._Porte.Mode = payload
        elif message.topic == "switch_porte" and self._Poulailler._Porte.Mode == ModePorte.Manuel.value:
            if self._Poulailler._Porte.GetEtat() == EtatPorte.Ferme.value:
                print("Forcer fermeture porte")
                self._Poulailler._Porte.Ouvrir()
            else:
                print("Forcer ouverture porte")
                self._Poulailler._Porte.Fermer()
                        
    def __start__(self):
        # On start tout les threads du poulailler
        self._Poulailler.InitialisationThreads()
        self._thread_Publish_TempHumi.run = self.BouclePublishTempHumi
        self._thread_Publish_Restant.run = self.BouclePublishRestant
        self._thread_Publish_Camera.run = self.BouclePublishCamera
        # On change la fonction on_connect du client pour la notre
        self._client.on_connect = on_connect
        self._client.on_message = self.on_message
        #On se connecte au broker
        print("Connecting ...")
        self._client.connect(host=self.broker_address,port=self.broker_port)
        self.PublishInit()
        
        
        self._client.subscribe("switch_porte")
        self._client.subscribe("mode_porte")
        self._client.subscribe("reset_compte_oeufs")
        self._thread_Publish_Restant.start()
        self._thread_Publish_Camera.start()
        self._thread_Publish_TempHumi.start()
            
        
        while True:
            continue
            

        
        
        
        
        
        
        
        