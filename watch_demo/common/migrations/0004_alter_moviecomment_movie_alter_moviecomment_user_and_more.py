# Generated by Django 4.1.3 on 2022-12-17 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_alter_movie_name_alter_movie_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0003_alter_movierating_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecomment',
            name='movie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='moviecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movierating',
            name='movie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
    ]
