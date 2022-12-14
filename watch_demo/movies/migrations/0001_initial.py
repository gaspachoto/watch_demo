# Generated by Django 4.1.3 on 2022-12-05 14:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import watch_demo.core.model_mixin


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('movie_poster', models.URLField()),
                ('description', models.CharField(max_length=300, validators=[django.core.validators.MinLengthValidator(20)])),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(watch_demo.core.model_mixin.StrFromFieldsMixin, models.Model),
        ),
    ]
