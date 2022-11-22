import string
from django.shortcuts import render
from django.http import HttpResponse
from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
import json
import pickle
producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')

def frontEnd(request):
    return render(request, 'home.html')

def envioKAFKA(request):
    if request.method == 'POST':
        sexo=request.POST['sexo']
        altura=request.POST['altura']

        dados = {
        'dados': {
            'Sexo': sexo,
             "Altura": altura,
        },
        }
        serialized_data = pickle.dumps(dados, pickle.HIGHEST_PROTOCOL)
        producer.send('APIML_NEW_REQUEST', serialized_data)

        #args = {}
        #text = "hello world"
        #args['mytext'] = text
        #return render(request, 'home.html', args)
    else:
        return HttpResponse('404')

