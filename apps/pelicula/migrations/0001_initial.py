# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import uuid
import apps.pelicula.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, serialize=False, default=uuid.uuid4)),
                ('title_gender', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, serialize=False, default=uuid.uuid4)),
                ('title_movie', models.CharField(max_length=50, unique=True)),
                ('release', models.BooleanField(default=False)),
                ('photo', models.ImageField(upload_to=apps.pelicula.models.content_file_name)),
                ('data_movie', ckeditor.fields.RichTextField()),
                ('sinopsis', ckeditor.fields.RichTextField()),
                ('technical_data', ckeditor.fields.RichTextField()),
                ('links', models.TextField(default="<a href=' \\# ' class='link' target='blank'> Descargar </a>")),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False)),
                ('gender', models.ManyToManyField(to='pelicula.Gender')),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, serialize=False, default=uuid.uuid4)),
                ('title_quality', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, serialize=False, default=uuid.uuid4)),
                ('title_year', models.CharField(max_length=4, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='quality',
            field=models.ForeignKey(to='pelicula.Quality'),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.ForeignKey(to='pelicula.Year'),
        ),
    ]
