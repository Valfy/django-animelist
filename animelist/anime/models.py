from django.db import models


class Anime_Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    release_date = models.IntegerField(verbose_name='Год выпуска')
    image = models.ImageField(upload_to='anime/%Y/%m/%d/', verbose_name='Картинка')
    tags = models.ManyToManyField(Anime_Tag, verbose_name='Тэги')
    is_activated = models.BooleanField(default=True, verbose_name='Отображается ли на сайте')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
