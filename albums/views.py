from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import AlbumForm
from albums.models import Album, Artista, Cancion
from django.shortcuts import redirect

# Create your views here.
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