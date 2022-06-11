from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('tag/<int:tag_id>/', tagged, name='tag'),
    path('anime/<int:anime_id>/', anime, name='anime'),
    path('anime_change_watched/<int:anime_id>/', anime_change_watched, name='anime_change_watched'),
    path('anime_change_rate/<int:anime_id>/', anime_change_rate, name='anime_change_rate')
]