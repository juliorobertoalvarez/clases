from django.db import models
from django.contrib import admin

class Album(models.Model):
    nombre                  = models.CharField(max_length=30)
    fecha_salida            = models.DateField()
    descripcion             = models.CharField(max_length=120)
    cantidad_canciones      = models.IntegerField()
    nombre_integrantes      = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class Artista(models.Model):
    nombre                  = models.CharField(max_length=60)
    apodo                   = models.CharField(max_length=60)
    anios                   = models.IntegerField()
    profesion               = models.CharField(max_length=60)
    albums                  = models.ManyToManyField(Album, through='Cancion')

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

class CacionInLine(admin.TabularInline):
    model = Cancion
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    inlines = (CacionInLine,)

class ArtistaAdmin (admin.ModelAdmin):
    inlines = (CacionInLine,)