# Django

url: https://www.w3schools.com/django/django_urls.php


run:
```
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
