from django.db import models

class Anime_Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

class Anime(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    release_date = models.IntegerField()
    image = models.ImageField(upload_to='images/anime/%Y/%m/%d/')
    tags = models.ManyToManyField(Anime_Tag)

    class Meta:
        ordering = ['name']





