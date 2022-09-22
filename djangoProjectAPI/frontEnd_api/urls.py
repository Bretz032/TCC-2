
from django.urls import path
from .views import frontEnd

urlpatterns = [
    path('frontend/', frontEnd.as_view(), name = 'frontEnd'),
]