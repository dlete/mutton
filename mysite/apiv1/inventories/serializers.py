# imports Django
# Need to import models from django.db to be able to import models
# from other apps.
from django.db import models

# imports third-party apps
from rest_framework import serializers

# imports this project apps
from inventories.models import Client
from inventories.models import Ne
from inventories.models import ServiceType
from inventories.models import Service
from inventories.models import ServiceEndpoint

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        #fields = '__all__'
        # in Python ('my_field') is a string. To make a single-element tuple
        # you need a comma: ('my_field',).
        # https://stackoverflow.com/questions/35676293/django-rest-framework
        #-tuple-being-interpreted-as-a-string
        fields = ('id', 'name', 'id_csd')

class NeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ne
        fields = ('id', 'fqdn', 'id_csd', 'role', 'meid')

class ServiceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceType
        fields = ('id', 'name')

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    service_type = serializers.PrimaryKeyRelatedField(queryset=ServiceType.objects.all(), write_only=False)
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), write_only=False)

    class Meta:
        model = Service
        fields = ('id', 'name', 'csd_id', 'state', 'comments', 'csd_created', 
            'csd_updated', 'service_type', 'client'
        )

class ServiceEndpointSerializer(serializers.HyperlinkedModelSerializer):
    """
    Note:
    'write_only=False, allows you to ALSO read. It is almost counter intuitive.
    But that is the key if you only want to deal with ID as an integer.
    """
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), write_only=False)
    ne = serializers.PrimaryKeyRelatedField(queryset=Ne.objects.all(), write_only=False)

    # This that were tried.
    #service = serializers.CharField(source='service.id', read_only=True)   # works for reading, and service is treated as a character, not an integer.
    #service = serializers.CharField(source='service.id', read_only=False) # does not work for writing. "The `.create()` method does not support writable dotted-source fields by default. Write an explicit `.create()` method for serializer `apiv1.inventories.serializers.ServiceEndpointSerializer`, or set `read_only=True` on dotted-source serializer fields."

    #service = ServiceSerializer() # this returns the whole service object, with all its fields, as nested. You have to POST service as a whole dictionary."
    #service = serializers.IntegerField(source='service.id') # can't create: The `.create()` method does not support writable dotted-source fields by default.

    class Meta:
        model = ServiceEndpoint
        fields = ('id', 'service', 'ne', 'interface_name', 'interface_index')
