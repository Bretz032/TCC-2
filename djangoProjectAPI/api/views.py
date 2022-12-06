from codecs import getencoder
import numpy as np
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from kafka import KafkaProducer
import pickle #pickle converts data into byte array
from rest_framework.permissions import IsAuthenticated
   
class WeightPrediction(APIView):
 
   # permission_classes=[IsAuthenticated]
    def post(self, request,):
         #Iniciando Kafka
        producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
     
        data = request.data
        height = int(data['Altura'])
        gender = data['Sexo']
        if gender == 'Masculino':
            gender = 0
        elif gender == 'Feminino':
            gender = 1
        else:
            return Response("Campo gênero é invalido.", status=400)

        lin_reg_model = ApiConfig.model
        weight_predicted = lin_reg_model.predict([[gender, height]])[0][0]
        weight_predicted = np.round(weight_predicted, 1)

        
        response_dict = str(height)+"-"+str(gender)
         
        encoded_string = response_dict.encode()
        byte_array = bytearray(encoded_string)
         #EnvioKafka
        serialized_data = pickle.dumps(response_dict, pickle.HIGHEST_PROTOCOL)
        
        producer.send('APIML_DADOS', byte_array)
        args = {}
        result = "Peso deduzido: "+str(weight_predicted)+"KG"
        args['mytext'] = str(result)

        if request.META['QUERY_STRING']=="type=page":
            return render(request, 'home.html', args)
        else: 
            return Response("Peso deduzido: "+str(weight_predicted)+"KG")