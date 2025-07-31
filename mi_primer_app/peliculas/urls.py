from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página de inicio (Home)
    path('', views.home, name='home'),

    # Ruta para crear un nuevo director
    path('crear-director/', views.crear_director, name='crear-director'),

    # Ruta para crear una nueva película
    path('crear-pelicula/', views.crear_pelicula, name='crear-pelicula'),

    # Ruta para crear un nuevo actor o reseña
    path('crear-resena/', views.crear_resena, name='crear-resena'),

    # Ruta para buscar una película por título
    path('buscar-pelicula/', views.buscar_pelicula, name='buscar-pelicula'),

    # Ruta para listar todas las películas
    path('listar-peliculas/', views.listar_peliculas, name='listar-peliculas'),
]