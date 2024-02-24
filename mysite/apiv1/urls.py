# imports Django
from django.urls import include
from django.urls import path

# imports third party apps
from rest_framework import routers

# imports this project
from .inventories import views


# set the namespace for this app
app_name = 'apiv1'



router = routers.DefaultRouter()

# The items below will appear in the Api Root page of DRF
router.register(r'inventories/client', views.ClientViewSet)
router.register(r'inventories/ne', views.NeViewSet)
router.register(r'inventories/service_type', views.ServiceTypeViewSet)
router.register(r'inventories/service', views.ServiceViewSet)
router.register(r'inventories/service_endpoint', views.ServiceEndpointViewSet)

# The 'urlpatterns' block must appear after the 'router.register' block.
urlpatterns = [
    path('', include(router.urls)),
]
