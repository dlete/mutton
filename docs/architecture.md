# Why have a local copy?
For billing

# Python packages
- `lxml` to parse XML files.
- `djangorestframework` to have a REST API.
  - `markdown` so that there is Markdown support for the browsable API. Required by `djangorestframework`.
  - `django-filter` provides filtering support, required by `djangorestframework`.
  - The `coreapi` library is required as a dependancy for the API docs.
  - The `pygments` and `markdown` libraries are optional but recommended.
- `django-rest-swagger`, an API documentation generator for Swagger UI and Django REST Framework. 

# How to build DRF
- install drf package
- create an apiv1 app
- in main urls.py, route apiv1/ to apiv1/urls.py
- in apiv1/urls.py
```Python
from django.urls import include
from django.urls import path

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
```

- in project urls.py
```Python
urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]
```

- edit serializers.py under directory apiv1/
- edit views.py under directory apiv1/

## References
[DRF tutorial](https://medium.com/@djstein/modern-django-part-2-rest-apis-apps-and-django-rest-framework-ea0cac5ab104)
[DRF quickstart](http://www.django-rest-framework.org/tutorial/quickstart/#settings)
[Django REST framework how to structure your app](http://danielhnyk.cz/django-rest-framework-how-to-structure-your-app/)
Cheat sheet for working with DRF: [Classy Django REST Framework](http://www.cdrf.co/)


# How to Django REST Swagger
- install package `pip install django-rest-swagger`
- Add rest_framework_swagger to your INSTALLED_APPS setting:
```Python
INSTALLED_APPS = (
    ...
    'rest_framework_swagger',
)
```
- Then configure
```Python
from django.urls import  path
# to document the API with Django REST Swagger
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Mutton API')
urlpatterns += [
    path('api-swagger/', schema_view)
]
```
