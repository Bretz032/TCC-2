from django.urls import path
from . import views

urlpatterns = [
        path('frontend/', views.frontEnd, name='frontEnd'),
        path('frontend/envioKAFKA', views.envioKAFKA, name='envioKAFKA'),

   
]