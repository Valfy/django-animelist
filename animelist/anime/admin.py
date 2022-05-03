from django.contrib import admin

from .models import Anime_Tag, Anime

class Anime_Tag_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ['name']


class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'release_date')
    list_display_links = ('id', 'name')

    ordering = ['-id']


admin.site.register(Anime_Tag, Anime_Tag_Admin)
admin.site.register(Anime, AnimeAdmin)