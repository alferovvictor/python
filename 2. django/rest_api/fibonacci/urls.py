from django.urls import path
from . import views

urlpatterns = [
    path('api/fib/', views.fib_handler, name='fib'),
]