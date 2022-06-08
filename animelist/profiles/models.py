from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.dispatch import receiver
from anime.models import Anime


class AnimeProfile(models.Model):
    id = models.AutoField(primary_key=True)
    userlink = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Юзер')
    username = models.CharField(blank=True, max_length=64, verbose_name='Имя')
    avatar = models.ImageField(upload_to='profiles/%Y/%m/%d/', blank=True,  verbose_name='Аватарка')

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-userlink']


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        AnimeProfile.objects.create(userlink=instance, username=instance)


class UserAnimeRate(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AnimeProfile, on_delete=models.CASCADE, verbose_name='Юзер')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name='Юзер')
    is_watched = models.BooleanField(verbose_name='Просмотренно?')
    rate = models.IntegerField(blank=True, verbose_name='Оценка', null=True)

    class Meta:
        ordering = ['rate', 'anime']




