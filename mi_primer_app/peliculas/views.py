from .models import Pelicula, Director, Actor  
from .forms import PeliculaForm, DirectorForm, ActorForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def home(request):
    # Obtener los datos de actores, directores y películas
    actores = Actor.objects.all()
    directores = Director.objects.all()
    peliculas = Pelicula.objects.all()

    return render(request, 'peliculas/home.html', {
        'actores': actores,
        'directores': directores,
        'peliculas': peliculas,
    })

# Vista de sobre nosotros
def about_view(request):
    return render(request, "peliculas/about.html")

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

# Vista para listar todas las películas
def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/listar.html', {'peliculas': peliculas})

@login_required
def editar_objeto(request, tipo, pk):
    # Dependiendo del tipo, obtenemos el objeto correspondiente
    if tipo == 'pelicula':
        objeto = get_object_or_404(Pelicula, pk=pk)
        form_class = PeliculaForm
        titulo = 'Editar Película'
        redirect_url = 'listar-peliculas'
    elif tipo == 'director':
        objeto = get_object_or_404(Director, pk=pk)
        form_class = DirectorForm
        titulo = 'Editar Director'
        redirect_url = 'home'
    elif tipo == 'actor':
        objeto = get_object_or_404(Actor, pk=pk)
        form_class = ActorForm
        titulo = 'Editar Actor'
        redirect_url = 'home'
    else:
        # Si el tipo no es válido, redirigimos a una página de error o al home
        return redirect('home')

    # Si el método es POST, procesamos el formulario
    if request.method == 'POST':
        form = form_class(request.POST, instance=objeto)
        if form.is_valid():
            form.save()
            messages.success(request, f'{titulo} actualizado correctamente.')
            return redirect(redirect_url)
    else:
        form = form_class(instance=objeto)

    return render(request, 'peliculas/formulario.html', {'form': form, 'titulo': titulo})

@login_required
def borrar_objeto(request, tipo, pk):
    if tipo == 'pelicula':
        obj = get_object_or_404(Pelicula, pk=pk)
        nombre_objeto = obj.titulo
        url_redirect = 'listar-peliculas'
    elif tipo == 'actor':
        obj = get_object_or_404(Actor, pk=pk)
        nombre_objeto = obj.nombre
        url_redirect = 'home'
    elif tipo == 'director':
        obj = get_object_or_404(Director, pk=pk)
        nombre_objeto = obj.nombre
        url_redirect = 'home'
    else:
        return redirect('home')

    if request.method == 'POST':
        obj.delete()
        messages.success(request, f'{tipo.capitalize()} eliminada correctamente!.')
        return redirect(url_redirect)

    return render(request, 'peliculas/borrar_confirmacion.html', {
        'nombre_objeto': nombre_objeto,
        'tipo': tipo,
        'url_redirect': url_redirect
    })