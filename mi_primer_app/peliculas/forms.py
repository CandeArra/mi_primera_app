# Formulario para Película
from django import forms
from .models import Pelicula, Director, Actor

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'anio', 'genero']

# Formulario para Director
class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['nombre', 'nacionalidad']

# Formulario para Actor
class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['nombre', 'edad']
