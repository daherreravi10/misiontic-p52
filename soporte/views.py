from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from rest_framework.serializers import Serializer
from .models import PQR,PersonaSoporte
from .serializers import PQRSerializer, PersonaSoporteSerializer
# Create your views here.
class PersonaSoporteListCreate(generics.ListCreateAPIView):
    QuerySet= PersonaSoporte.objects.all()
    serializer_class= PersonaSoporteSerializer

class PersonaSoporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    QuerySet = PersonaSoporte.objects.all()
    serializer_class = PersonaSoporteSerializer

class PQRListCreate(generics.ListCreateAPIView):
    QuerySet= PQR.objects.all()
    serializer_class= PQRSerializer

class PQRUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    QuerySet = PQR.objects.all()
    serializer_class = PQRSerializer