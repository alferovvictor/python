# Django

url: https://www.w3schools.com/django/django_urls.php

## Installing:
```
pip install Django
```

## Run:
```
1) install:
py -m pip install Django

2) write your app ...

3) run:
python manage.py runserver
```

##CSRF

```
1)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def users(request):

2)
MIDDLEWARE = [
#    'django.middleware.csrf.CsrfViewMiddleware',
]
```

## Comments
https://realpython.com/python-assert-statement/

## TESTING
Testing the API:
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#testing-the-api

coverage:
```
coverage run manage.py test whatever -v 2
coverage html
```