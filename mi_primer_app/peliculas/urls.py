from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear-director/', views.crear_director, name='crear-director'),
    path('crear-pelicula/', views.crear_pelicula, name='crear-pelicula'),
    path('crear-resena/', views.crear_resena, name='crear-resena'),
    path('buscar-pelicula/', views.buscar_pelicula, name='buscar-pelicula'),
    path('listar-peliculas/', views.listar_peliculas, name='listar-peliculas'),
]