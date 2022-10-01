from django.urls import path, include
from . import views

urlpatterns = [
    path('prueba1/', views.muestra_datos, name='prueba1'),
]
