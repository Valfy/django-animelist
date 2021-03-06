from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Count

from .models import *
from profiles.models import AnimeProfile, UserAnimeRate


def main(request):
    anime_objects = Anime.objects.filter(is_activated=True)
    paginator = Paginator(anime_objects, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Anime_Tag.objects.all()
    if request.user.is_authenticated:
        authenticated_user = AnimeProfile.objects.get(userlink=request.user.pk)
        context = {
            'page_obj': page_obj,
            'tags': tags,
            'a_user': authenticated_user
        }
    else:
        context = {
            'page_obj': page_obj,
            'tags': tags
        }
    return render(request, 'anime/all.html', context)


def tagged(request, tag_id):
    anime_objects = Anime.objects.filter(is_activated=True, tags=tag_id)
    paginator = Paginator(anime_objects, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Anime_Tag.objects.all()
    tag = tags.get(pk=tag_id)
    if request.user.is_authenticated:
        authenticated_user = AnimeProfile.objects.get(userlink=request.user.pk)
        context = {
            'page_obj': page_obj,
            'tags': tags,
            'tag': tag,
            'a_user': authenticated_user
        }
    else:
        context = {
            'page_obj': page_obj,
            'tags': tags,
            'tag': tag
        }
    return render(request, 'anime/tagged.html', context)


def anime(request, anime_id):
    anime_obj = Anime.objects.get(pk=anime_id)
    tags = Anime_Tag.objects.all()
    anime_status_total = UserAnimeRate.objects.filter(anime=anime_obj)
    anime_total_views = anime_status_total.filter(is_watched=1).aggregate(count_views=Count('is_watched'))
    anime_total_rate = anime_status_total.filter(rate__gt=0).aggregate(avg=Avg('rate'), count_rates=Count('rate'))
    if request.user.is_authenticated:
        authenticated_user = AnimeProfile.objects.get(userlink=request.user.pk)
        try:
            anime_status = UserAnimeRate.objects.get(user=authenticated_user, anime=anime_obj)
        except ObjectDoesNotExist:
            anime_status = UserAnimeRate.objects.create(user=authenticated_user, anime=anime_obj, is_watched=0, rate=0)
            anime_status.save()
        context = {
            'anime_obj': anime_obj,
            'tags': tags,
            'a_user': authenticated_user,
            'a_status': anime_status,
            'a_total':  anime_status_total,
            'a_totalrate': anime_total_rate,
            'a_totalviews': anime_total_views
        }
    else:
        context = {
            'anime_obj': anime_obj,
            'tags': tags,
            'a_total': anime_status_total,
            'a_totalrate': anime_total_rate,
            'a_totalviews': anime_total_views
        }
    return render(request, 'anime/anime.html', context)


def anime_change_watched(request, anime_id):
    anime_obj = Anime.objects.get(pk=anime_id)
    if request.method == "POST":
        authenticated_user = AnimeProfile.objects.get(userlink=request.user.pk)
        anime_status = UserAnimeRate.objects.filter(user=authenticated_user, anime=anime_obj)
        if anime_status.values_list('is_watched')[0][0]:
            anime_status.update(is_watched=False)
        else:
            anime_status.update(is_watched=True)
    return redirect('anime', anime_id)


def anime_change_rate(request, anime_id):
    anime_obj = Anime.objects.get(pk=anime_id)
    authenticated_user = AnimeProfile.objects.get(userlink=request.user.pk)
    anime_status = UserAnimeRate.objects.filter(user=authenticated_user, anime=anime_obj)
    user_rate = request.GET.get('r', None)
    anime_status.update(rate=user_rate)
    return redirect('anime', anime_id)