from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

from .models import AnimeProfile, UserAnimeRate


def registration_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('main')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserCreationForm()
    return render(request, 'rp.html', {'form': form})


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вход произведён успешно!')
            return redirect('main')
        else:
            messages.error(request, 'Ошибка входа!')
    else:
        form = AuthenticationForm()
    return render(request, 'lp.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('lp')


def profile_view(request, user_id):
    profile = AnimeProfile.objects.get(pk=user_id)
    total_anime = UserAnimeRate.objects.filter(user=user_id, is_watched=True)
    if request.user.is_authenticated:
        authenticated_user = AnimeProfile.objects.get(userlink=request.user.pk)
        context = {
            'profile': profile,
            'a_user': authenticated_user,
            'total_anime': total_anime
        }
    else:
        context = {
            'profile': profile,
            'total_anime': total_anime
        }
    return render(request, 'profiles/profile.html', context)


def profiles_all(request):
    profile_objects = AnimeProfile.objects.all()
    paginator = Paginator(profile_objects, 14)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.user.is_authenticated:
        authenticated_user = AnimeProfile.objects.get(userlink=request.user.pk)
        context = {
            'page_obj': page_obj,
            'a_user': authenticated_user
        }
    else:
        context = {
            'page_obj': page_obj,
        }
    return render(request, 'profiles/profiles_all.html', context)