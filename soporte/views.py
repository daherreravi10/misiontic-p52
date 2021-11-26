
from django.shortcuts import render
from rest_framework import views, generics, authentication, permissions, status
from rest_framework.serializers import Serializer
from .models import PQR,PersonaSoporte
from .serializers import PQRSerializer, PersonaSoporteSerializer
# Create your views here.
class PersonaSoporteListCreate(generics.ListCreateAPIView):
    querySet= PersonaSoporte.objects.all()
    serializer_class= PersonaSoporteSerializer

class PersonaSoporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    querySet = PersonaSoporte.objects.all()
    serializer_class = PersonaSoporteSerializer

class PQRListCreate(generics.ListCreateAPIView):
    querySet= PQR.objects.all()
    serializer_class= PQRSerializer

class PQRUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    querySet = PQR.objects.all()
    serializer_class = PQRSerializer