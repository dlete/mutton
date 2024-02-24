"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# project apps
urlpatterns += [
    path('api/v1/', include('apiv1.urls')),
    path('core/', include('core.urls')),
    path('inventories/', include('inventories.urls')),
]

# to authenticate in DRF
urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]

# to document the API with DRF built-in documentation
# http://www.django-rest-framework.org/topics/documenting-your-api/
# https://stackoverflow.com/questions/45829200/django-rest-api-docs-is-not-a-registered-namespace
from rest_framework.documentation import include_docs_urls
urlpatterns += [
    path('docs/', include_docs_urls(title='Mutton API'))
]

# to document the API with Django REST Swagger
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Mutton API')
urlpatterns += [
    path('api-swagger/', schema_view)
]


# This is the landing page. Redirects the base URL '/' (or empty) to '/inventories/'.
# Taken from https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website
# Leave the first parameter of the path function empty to imply '/'.
# If you write the first parameter as '/' Django will give you the following warning:
# ?: (urls.W002) Your URL pattern '/' has a route beginning with a '/'.
# Remove this slash as it is unnecessary.
from django.views.generic.base import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/core/', permanent=True)),
]
