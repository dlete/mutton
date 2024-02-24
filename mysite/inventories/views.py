# imports Django
from django.shortcuts import get_object_or_404
from django.shortcuts import render

# imports from this app
from .models import Client
from .models import ElineLdp
from .models import L3vpn
from .models import Ne
from .models import Service
from .models import ServiceEndpoint

def client_all(request):
    context = {'bodymessage': "Clients in CSD"}
    context['client_all'] = Client.objects.all()
    return render(request, 'inventories/client_all.html', context)

def client_one(request, pk):
    context = {'bodymessage': "Details of one Client in CSD"}
    context['eline_all'] = ElineLdp.objects.filter(client=pk)
    context['eline_count'] = context['eline_all'].count()
    context['eline_price'] = 2835
    context['eline_charges'] = context['eline_count'] * context['eline_price']

    context['l3vpn_all'] = L3vpn.objects.filter(client=pk)
    context['l3vpn_count'] = context['l3vpn_all'].count()
    context['l3vpn_price'] = 1113
    context['l3vpn_charges'] = context['l3vpn_count'] * context['l3vpn_price']

    context['total_charges'] = context['eline_charges'] + context['l3vpn_charges'] 

    context['client'] = Client.objects.get(pk=pk)
    return render(request, 'inventories/client_one_services.html', context)

def eline_ldp_all(request):
    context = {'bodymessage': "ELINE LDP in CSD"}
    context['eline_all'] = ElineLdp.objects.all()
    return render(request, 'inventories/elineldp_all.html', context)

def eline_ldp_one(request, pk):
    context = {'bodymessage': "Details of one ELINE LDP in CSD"}
    eline_one = get_object_or_404(ElineLdp, pk=pk)
    context['eline_one'] = eline_one
    return render(request, 'inventories/elineldp_one.html', context)

def l3vpn_all(request):
    context = {'bodymessage': "L3VPN in CSD"}
    context['l3vpn_all'] = L3vpn.objects.all()
    return render(request, 'inventories/l3vpn_all.html', context)

def l3vpn_one(request, pk):
    context = {'bodymessage': "Details of one L3VPN in CSD"}
    l3vpn_one = get_object_or_404(L3vpn, pk=pk)
    context['l3vpn_one'] = l3vpn_one
    return render(request, 'inventories/l3vpn_one.html', context)

def ne_all(request):
    context = {'bodymessage': "NE in CSD"}
    context['ne_all'] = Ne.objects.all()
    return render(request, 'inventories/ne_all.html', context)

def service_all(request):
    context = {'bodymessage': "Service instances in CSD"}
    context['service_all'] = Service.objects.all()
    return render(request, 'inventories/service_all.html', context)

def service_endpoint_all(request):
    context = {'bodymessage': "Service Endpoints in CSD"}
    context['service_endpoint_all'] = ServiceEndpoint.objects.all()
    return render(request, 'inventories/service_endopoint_all.html', context)
