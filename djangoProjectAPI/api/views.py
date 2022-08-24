import numpy as np
import pandas as pd
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response


class WeightPrediction(APIView):
    def post(self, request):
        data = request.data
        height = data['Altura']
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
        response_dict = {"Peso deduzido (kg)": weight_predicted}
        return Response(response_dict, status=200)