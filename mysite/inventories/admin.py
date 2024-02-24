from django.contrib import admin

from .models import Client
from .models import ElineLdp
from .models import L3vpn
from .models import Ne
from .models import ServiceType
from .models import Service
from .models import ServiceEndpoint

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'id_cdb', 'id_csd']

admin.site.register(Client, ClientAdmin)


class NeAdmin(admin.ModelAdmin):
    list_display = ['fqdn', 'role', 'id_csd']

admin.site.register(Ne, NeAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_type', 'csd_id', 'client']

admin.site.register(Service, ServiceAdmin)

class ServiceEndpointAdmin(admin.ModelAdmin):
    list_display = ['service', 'ne', 'interface_name', 'interface_index']

admin.site.register(ServiceEndpoint, ServiceEndpointAdmin)


admin.site.register(ElineLdp)
admin.site.register(L3vpn)
admin.site.register(ServiceType)
