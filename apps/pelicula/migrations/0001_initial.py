# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title_gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title_movie', models.CharField(max_length=50)),
                ('release', models.BooleanField(default=False)),
                ('trailer', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='portada/')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title_quality', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title_year', models.CharField(max_length=4)),
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
