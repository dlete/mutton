# imports Django
from django.urls import path

# imports from this project
from . import views

# set the namespace for this app
app_name = 'core'

urlpatterns = [
    # ex: /core/
    path('', views.about, name='about'),

    # ex: /core/about/
    path('about/', views.about, name='about'),
]

