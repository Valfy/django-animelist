from django.contrib import admin
from .models import AnimeProfile, UserAnimeRate


class AnimeProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'userlink', 'username')
    list_display_links = ('id', 'userlink')
    ordering = ['-userlink']


class UserAnimeRateAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'anime', 'is_watched', 'rate')
    list_display_links = ('id', 'user', 'anime')
    ordering = ['-id']


admin.site.register(AnimeProfile, AnimeProfileAdmin)
admin.site.register(UserAnimeRate, UserAnimeRateAdmin)