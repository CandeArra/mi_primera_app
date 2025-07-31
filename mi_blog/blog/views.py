from django.shortcuts import render, redirect
from .models import Entrada, Categoria, Comentario
from .forms import EntradaForm, ComentarioForm, BusquedaForm

# Vista de inicio
def index(request):
    entradas = Entrada.objects.all()
    return render(request, 'index.html', {'entradas': entradas})

# Vista para crear una nueva entrada
def crear_entrada(request):
    if request.method == "POST":
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntradaForm()
    return render(request, 'crear_entrada.html', {'form': form})

# Vista de búsqueda
def buscar(request):
    form = BusquedaForm(request.GET)
    entradas = []
    if form.is_valid() and form.cleaned_data['query']:
        query = form.cleaned_data['query']
        entradas = Entrada.objects.filter(titulo__icontains=query)
    return render(request, 'buscar.html', {'form': form, 'entradas': entradas})