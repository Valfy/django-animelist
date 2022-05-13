from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('tag/<int:tag_id>/', tagged, name='tag'),
    path('anime/<int:anime_id>/', anime, name='anime')
]