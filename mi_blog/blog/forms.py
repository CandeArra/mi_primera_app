from django import forms
from .models import Entrada, Comentario

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'contenido', 'categoria']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'texto']

class BusquedaForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)