####################################################################################
# Os, Sys
import os, sys
from sameAs import SameAs

# Mqtt
from paho.mqtt import client as mqtt_client
import random

# Imagehash
from PIL import Image
import imagehash

# Download Input Image
import requests

# Class
from samples import Samples

####################################################################################

# Atributos Mqtt
broker = 'broker.hivemq.com'
port = 1883
topic = "function/mqtt/python"
client_id = f'FuncOrgPy-{random.randint(0, 1000)}'


# Mqtt Function
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n, rc")

    # Set conection
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"\nReceived `{msg.payload.decode()}` from `{msg.topic}` topic")
        checkImg(client, msg.payload.decode())

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


####################################################################################

# Attr
AcidosCarboxilicos = Samples('AcidosCarboxilicos')
AcidosCarboxilicos = AcidosCarboxilicos.getSamples()

Alcanos = Samples('Alcanos')
Alcanos = Alcanos.getSamples()

Alcenos = Samples('Alcenos')
Alcenos = Alcenos.getSamples()

Alcinos = Samples('Alcinos')
Alcinos = Alcinos.getSamples()

Alcoois = Samples('Alcoois')
Alcoois = Alcoois.getSamples()

Aldeidos = Samples('Aldeidos')
Aldeidos = Aldeidos.getSamples()

Amidas = Samples('Amidas')
Amidas = Amidas.getSamples()

Aminas = Samples('Aminas')
Aminas = Aminas.getSamples()

Aromaticos = Samples('Aromaticos')
Aromaticos = Aromaticos.getSamples()

Cetonas = Samples('Cetonas')
Cetonas = Cetonas.getSamples()

Cicloalcanos = Samples('Cicloalcanos')
Cicloalcanos = Cicloalcanos.getSamples()

Cicloalcenos = Samples('Cicloalcenos')
Cicloalcenos = Cicloalcenos.getSamples()

Esteres = Samples('Esteres')
Esteres = Esteres.getSamples()

Eteres = Samples('Eteres')
Eteres = Eteres.getSamples()

Fenois = Samples('Fenois')
Fenois = Fenois.getSamples()

Haletos = Samples('Haletos')
Haletos = Haletos.getSamples()

Nitrilas = Samples('Nitrilas')
Nitrilas = Nitrilas.getSamples()

Nitrocompostos = Samples('Nitrocompostos')
Nitrocompostos = Nitrocompostos.getSamples()

dirVars = [AcidosCarboxilicos, Alcanos, Alcenos, Alcinos, Alcoois, Aldeidos, Amidas, Aminas, Aromaticos, Cetonas,
           Cicloalcanos, Cicloalcenos, Esteres, Eteres, Fenois, Haletos, Nitrilas, Nitrocompostos]

# Comparison cutoff
cutoff = 5


# Function Img
def checkImg(client, msg):
    # List Dir
    path = "./BancoDeDados/"
    dirs = os.listdir(path)

    # Add to an Array
    for dir in dirs:
        a = SameAs(dir)
    dirs.sort()

    # Input Image
    response = requests.get(msg)

    inpImageId = "input-images/inpImage%s.png" % (random.randint(0, 10000))

    file = open(inpImageId, "wb")
    file.write(response.content)
    file.close()

    inpImage = imagehash.average_hash(Image.open(inpImageId))

    r = 0
    while r < len(dirVars):
        print(f"\n{dirs[r]}: \n")
        for x in dirVars[r]:
            if inpImage - x < cutoff:
                print("- - - AEEEE - - -")
                a.addOn(dirs[r])
            else:
                print("- - - X X X - - -")
        r += 1
    else:
        msg = a.toString()
        result = client.publish("function/mqtt/js", msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"\nSend `{msg}` to topic function/mqtt/js")
        else:
            print(f"\nFailed to send message to topic {topic}")
        a.clear()


####################################################################################

if __name__ == '__main__':
    run()

####################################################################################
