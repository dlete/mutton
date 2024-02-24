from django.shortcuts import render

# Create your views here.

'''
To do:
    check http://www.django-rest-framework.org/tutorial/2-requests-and-responses/
    for this
    REST framework provides two wrappers you can use to write API views.

    The @api_view decorator for working with function based views.
    The APIView class for working with class-based views.
Note:
    VERY IMPORTANT, need to import django.db models to be able to import
    models from other apps.
'''

# imports Django
from django.db import models
#from django.shortcuts import render

# imports third-party apps
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

# imports this project apps
from inventories.models import Client
from inventories.models import Ne
from inventories.models import ServiceType
from inventories.models import Service
from inventories.models import ServiceEndpoint
from .serializers import ClientSerializer
from .serializers import NeSerializer
from .serializers import ServiceTypeSerializer
from .serializers import ServiceSerializer
from .serializers import ServiceEndpointSerializer


class ClientViewSet(viewsets.ModelViewSet):
    '''
    list:
    Return al list of all the existing Client.

    create:
    Create a new Client.

    retrieve:
    Return the given Client.

    update:
    Update the given Client.

    partial_update:
    Update part of the given Client.

    destroy:
    Delete the given Client.
    '''
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class NeViewSet(viewsets.ModelViewSet):
    queryset = Ne.objects.all()
    serializer_class = NeSerializer

class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceEndpointViewSet(viewsets.ModelViewSet):
    queryset = ServiceEndpoint.objects.all()
    serializer_class = ServiceEndpointSerializer
