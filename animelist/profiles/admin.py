from django.contrib import admin
from .models import AnimeProfile


class AnimeProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'userlink', 'username')
    list_display_links = ('id', 'userlink')
    ordering = ['-userlink']


admin.site.register(AnimeProfile, AnimeProfileAdmin)