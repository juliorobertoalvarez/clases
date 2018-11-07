from django import forms
from .models import Album, Artista, Cancion

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('nombre', 'fecha_salida', 'descripcion', 'cantidad_canciones', 'nombre_integrantes')

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ('nombre', 'apodo', 'anios', 'profesion', 'albums')

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ('nombre', 'descripcion', 'album', 'artista')


