from django.shortcuts import render
from .models import *

def main(request):
    anime_objects = Anime.objects.all()
    return render(request, 'anime/all.html', {'anime_objects': anime_objects})

def tagged(request, tag_id):
    anime_objects = Anime.objects.filter(tags=tag_id)
    tag = Anime_Tag.objects.get(pk=tag_id)
    return render(request, 'anime/tagged.html', {'anime_objects': anime_objects, 'tag': tag})

def anime(request, anime_id):
    anime_object = Anime.objects.get(pk=anime_id)
    return render(request, 'anime/anime.html', {'anime_object': anime_object})
