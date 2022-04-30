from django.urls import path

import anime.views

urlpatterns = [
    path('', anime.views.main, name='main')
]