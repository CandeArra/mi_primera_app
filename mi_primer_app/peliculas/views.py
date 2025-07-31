from django.shortcuts import render, redirect
from .models import Pelicula, Director, Actor  
from .forms import PeliculaForm, DirectorForm, ActorForm, BusquedaPeliculaForm


def home(request):
    actores = Actor.objects.all()
    directores = Director.objects.all()
    return render(request, 'peliculas/home.html', {
        'actores': actores,
        'directores': directores
    })

def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar-peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/formulario.html', {'form': form, 'titulo': 'Crear Película'})

def crear_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DirectorForm()
    return render(request, 'peliculas/formulario.html', {'form': form, 'titulo': 'Crear Director'})

def crear_resena(request):  # en este caso usás Actor como "reseña" para cumplir la consigna
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ActorForm()
    return render(request, 'peliculas/formulario.html', {'form': form, 'titulo': 'Crear Actor'})

def buscar_pelicula(request):
    resultado = None
    if request.method == 'POST':
        form = BusquedaPeliculaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultado = Pelicula.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaPeliculaForm()
    return render(request, 'peliculas/busqueda.html', {'form': form, 'resultado': resultado})

def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/listar.html', {'peliculas': peliculas})