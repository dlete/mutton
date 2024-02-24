# imports Django
from django.urls import path

# imports from this project
from . import views

# set the namespace for this app
app_name = 'inventories'

urlpatterns = [
    # ex: /inventories/
    path('', views.client_all, name='inventories_landing'),

    # ex: /inventories/client/
    path('client/', views.client_all, name='client_all'),

    # /inventories/client/5/
    path('client/<int:pk>/', views.client_one, name='client_one'),

    # ex: /inventories/eline_ldp/
    path('eline_ldp/', views.eline_ldp_all, name='eline_ldp_all'),

    # ex: /inventories/eline_ldp/5/
    path('eline_ldp/<int:pk>/', views.eline_ldp_one, name='eline_ldp_one'),

    # ex: /inventories/l3vpn/
    path('l3vpn/', views.l3vpn_all, name='l3vpn_all'),

    # ex: /inventories/l3vpn/5/
    path('l3vpn/<int:pk>/', views.l3vpn_one, name='l3vpn_one'),

    # ex: /inventories/ne/
    path('ne/', views.ne_all, name='ne_all'),

    # ex: /inventories/service/
    path('service/', views.service_all, name='service_all'),

    # ex: /inventories/service_endpoint/
    path('service_endpoint/', views.service_endpoint_all, name='service_endpoint_all'),
]

