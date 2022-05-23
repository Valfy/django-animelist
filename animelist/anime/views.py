from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from profiles.models import AnimeProfile

def main(request):
    anime_objects = Anime.objects.filter(is_activated=True)
    paginator = Paginator(anime_objects, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Anime_Tag.objects.all()
    if request.user.is_authenticated:
        authenticated_user = AnimeProfile.objects.get(userlink=request.user.pk)
        return render(request, 'anime/all.html', {'page_obj': page_obj, 'tags': tags, 'a_user': authenticated_user})
    else:
        return render(request, 'anime/all.html', {'page_obj': page_obj, 'tags': tags})


def tagged(request, tag_id):
    anime_objects = Anime.objects.filter(is_activated=True, tags=tag_id)
    paginator = Paginator(anime_objects, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Anime_Tag.objects.all()
    tag = tags.get(pk=tag_id)
    if request.user.is_authenticated:
        authenticated_user = AnimeProfile.objects.get(userlink=request.user.pk)
        return render(request, 'anime/tagged.html', {'page_obj': page_obj, 'tags': tags, 'tag': tag,\
            'a_user': authenticated_user})
    else:
        return render(request, 'anime/tagged.html', {'page_obj': page_obj, 'tags': tags, 'tag': tag})


def anime(request, anime_id):
    anime_object = Anime.objects.get(pk=anime_id)
    tags = Anime_Tag.objects.all()
    if request.user.is_authenticated:
        authenticated_user = AnimeProfile.objects.get(userlink=request.user.pk)
        return render(request, 'anime/anime.html', {'anime_object': anime_object, 'tags': tags,\
            'a_user': authenticated_user})
    else:
        return render(request, 'anime/anime.html', {'anime_object': anime_object, 'tags': tags})
