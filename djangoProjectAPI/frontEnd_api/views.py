from django.shortcuts import render

# Create your views here.
        #EnvioKafka
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from kafka import KafkaProducer
import pickle #pickle converts data into byte array


class frontEnd(APIView):
    def get(self, request):
        
        return Response(status=200)