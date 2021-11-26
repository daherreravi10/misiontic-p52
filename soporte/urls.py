from django.urls import path

from soporte.views import PQRListCreate, PQRUpdateDelete, PersonaSoporteListCreate, PersonaSoporteUpdateDelete

urlpatterns =[
    path('persona-soporte/', PersonaSoporteListCreate.as_view),
    path('persona.soporte/<pk>/', PersonaSoporteUpdateDelete.as_view),
    path('pqr/', PQRListCreate.as_view),
    path('pqr/<pk>/', PQRUpdateDelete.as_view),
    ]