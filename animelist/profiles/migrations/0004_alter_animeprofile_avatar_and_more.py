# Generated by Django 4.0.4 on 2022-05-21 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_alter_animeprofile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animeprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='profiles/%Y/%m/%d/', verbose_name='Аватарка'),
        ),
        migrations.AlterField(
            model_name='animeprofile',
            name='userlink',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Юзер'),
        ),
    ]