'''
Created on Nov. 12, 2019

@author: philip
'''

from Classes.Poulailler import Poulailler
import paho.mqtt.client as mqtt
import time

# Fonction est appelée lors de la connection d'un client
def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}".format(mqtt.connack_string(rc)))
    # Check whether the result form connect is the CONNACK_ACCEPTED connack code
    if rc != mqtt.CONNACK_ACCEPTED:
        raise IOError("Couldn't establish a connection with the MQTT server")

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
        self.connect(host=self.broker_address,port=self.breker_port)
        self._client.loop_start()
        
        