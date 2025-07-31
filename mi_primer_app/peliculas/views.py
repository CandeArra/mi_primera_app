from django.shortcuts import render, redirect
from .models import Pelicula, Director, Actor  
from .forms import PeliculaForm, DirectorForm, ActorForm, BusquedaPeliculaForm

# Vista principal mostrando actores y directores
def home(request):
    actores = Actor.objects.all()
    directores = Director.objects.all()
    return render(request, 'peliculas/home.html', {
        'actores': actores,
        'directores': directores
    })

# Vista para crear una nueva película
def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar-peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/formulario.html', {'form': form, 'titulo': 'Crear Película'})

# Vista para crear un nuevo director
def crear_director(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DirectorForm()
    return render(request, 'peliculas/formulario.html', {'form': form, 'titulo': 'Crear Director'})

# Vista para crear un nuevo actor
def crear_resena(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ActorForm()
    return render(request, 'peliculas/formulario.html', {'form': form, 'titulo': 'Crear Actor'})

# Vista para buscar películas por título
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

# Vista para listar todas las películas
def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/listar.html', {'peliculas': peliculas})