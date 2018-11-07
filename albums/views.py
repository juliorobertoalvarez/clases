from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import AlbumForm, ArtistaForm, CancionForm
from albums.models import Album, Artista, Cancion
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('album_detail', pk=post.pk)
    else:
        form = AlbumForm()
    return render(request, 'albums/album_edit.html', {'form': form})

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'album': album})

def album_remove(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('album_list')

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('album_detail', pk=post.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/album_edit.html', {'form': form})

@login_required
def artista_new(request):
    if request.method == "POST":
        form = ArtistaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('artista_detail', pk=post.pk)
    else:
        form = ArtistaForm()
    return render(request, 'albums/artista_edit.html', {'form': form})

def artista_list(request):
    artistas = Artista.objects.all()
    return render(request, 'albums/artista_list.html', {'artistas': artistas})


def artista_detail(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    return render(request, 'albums/artista_detail.html', {'artista': artista})

def artista_remove(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    artista.delete()
    return redirect('artista_list')

def artista_edit(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    if request.method == "POST":
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('artista_detail', pk=post.pk)
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'albums/artista_edit.html', {'form': form})

@login_required
def cancion_new(request):
    if request.method == "POST":
        form = CancionForm(request.POST)
        if form.is_valid():
            cancion = Cancion.objects.create(nombre=form.cleaned_data['nombre'], descripcion=form.cleaned_data['descripcion'],album=form.cleaned_data['album'],artista=form.cleaned_data['artista'])
            post = form.save(commit=False)
            post.save()
            return redirect('cancion_detail', pk=post.pk)
    else:
        form = CancionForm()
    return render(request, 'albums/cancion_edit.html', {'form': form})

def cancion_list(request):
    canciones = Cancion.objects.all()
    return render(request, 'albums/cancion_list.html', {'canciones': canciones})


def cancion_detail(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    return render(request, 'albums/cancion_detail.html', {'cancion': cancion})

def cancion_remove(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    cancion.delete()
    return redirect('cancion_list')

def cancion_edit(request, pk):
    cancion = get_object_or_404(Cancion, pk=pk)
    if request.method == "POST":
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('cancion_detail', pk=post.pk)
    else:
        form = CancionForm(instance=cancion)
    return render(request, 'albums/cancion_edit.html', {'form': form})