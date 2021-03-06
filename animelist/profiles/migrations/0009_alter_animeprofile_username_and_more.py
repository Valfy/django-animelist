# Generated by Django 4.0.4 on 2022-06-13 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0003_alter_anime_tag_options'),
        ('profiles', '0008_alter_useranimerate_options_alter_useranimerate_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animeprofile',
            name='username',
            field=models.CharField(blank=True, max_length=48, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='useranimerate',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime', verbose_name='Аниме'),
        ),
    ]
