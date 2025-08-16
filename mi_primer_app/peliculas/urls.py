from django.urls import path
from django.urls import path, include  
from . import views

urlpatterns = [    
    path('accounts/', include('accounts.urls')),  
    path('messaging/', include('messaging.urls')),        
    # Ruta para la página de inicio 
    path('', views.home, name='home'),  
    # Ruta para la página de sobre nosotros 
    path('about/', views.about_view, name='about'),
    # Ruta para crear un nuevo director
    path('crear-director/', views.crear_director, name='crear-director'),
    # Ruta para crear una nueva película
    path('crear-pelicula/', views.crear_pelicula, name='crear-pelicula'),
    # Ruta para crear un nuevo actor o reseña
    path('crear-resena/', views.crear_resena, name='crear-resena'),
    # Ruta para listar todas las películas
    path('listar-peliculas/', views.listar_peliculas, name='listar-peliculas'),
    path('editar/<str:tipo>/<int:pk>/', views.editar_objeto, name='editar-objeto'),
    path('borrar/<str:tipo>/<int:pk>/', views.borrar_objeto, name='borrar-objeto'),

]