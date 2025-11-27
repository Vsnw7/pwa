from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('noticias/', views.noticias, name='noticias'),
    path('galeria/', views.galeria, name='galeria'),
    path('descargas/', views.descargas, name='descargas'),
]
