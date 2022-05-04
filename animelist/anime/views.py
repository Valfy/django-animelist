from django.shortcuts import render
from .models import *

def main(request):
    animes = Anime.objects.all()
    return render(request, 'anime/all.html', {'animes': animes})

def tagged(request, tag_id):
    animes = Anime.objects.filter(tags=tag_id)
    tag = Anime_Tag.objects.get(pk=tag_id)
    return render(request, 'anime/tagged.html', {'animes': animes, 'tag': tag})
