from django.shortcuts import render, redirect
from .models import AnimeProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def registration_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('lp')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserCreationForm()
    return render(request, 'rp.html', {'form': form})

def login_page(request):
    return render(request, 'lp.html')
