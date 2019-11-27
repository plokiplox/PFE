'''
Created on Nov. 12, 2019

@author: philip
'''

from Classes.Poulailler import Poulailler
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
    breker_port = 1883
    
    _client = mqtt.Client(protocol=mqtt.MQTTv311)
    _Poulailler = Poulailler()

    def __init__(self):
        '''
        Constructor
        '''
        
    def __start__(self):
        # On start tout les threads du poulailler
        self._Poulailler.InitialisationThreads()
        # On change la fonction on_connect du client pour la notre
        self._client.on_connect = on_connect
        #On se connecte au broker
        print("Connecting ...")
        self._client.connect(host=self.broker_address,port=self.breker_port)
        self._client.loop_start()
        
        for i in range(0,60):
            self.PublierPoulailler()
            print("Publié ",i)
            time.sleep(10)
            continue
        
        print("Déconnecté")
        self._client.disconnect()
        self._client.loop_stop()
        
    def PublierPoulailler(self):
        publish_value(self._client, "Temp_In", self._Poulailler._Distribution_Eau.CTemp_Reservoire.GetTemperature())
        publish_value(self._client, "Temp_Out", self._Poulailler._Distribution_Eau.CTemp_Canalisation.GetTemperature())
        publish_value(self._client, "Humi_In", self._Poulailler._Distribution_Eau.CTemp_Reservoire.GetHumidity())
        publish_value(self._client, "Humi_Out", self._Poulailler._Distribution_Eau.CTemp_Canalisation.GetHumidity())
        publish_value(self._client, "Compte_Oeufs", self._Poulailler._Pondoires.Compte)
        
        
        
        
        
        
        
        