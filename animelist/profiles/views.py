from django.shortcuts import render
from .models import *

def registration_page(request):
    return render(request, 'rp.html')

def login_page(request):
    return render(request, 'lp.html')
