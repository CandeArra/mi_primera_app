from django import forms
from .models import Pelicula, Director, Actor

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'

class BusquedaPeliculaForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=100)