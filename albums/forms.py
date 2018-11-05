from django import forms
from .models import Album, Artista, Cancion

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('nombre', 'fecha_salida', 'descripcion', 'cantidad_canciones', 'nombre_integrantes')


