from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.db import models
import uuid

# Funciones:
# funcion para almacenamiento de imagenes
def content_file_name(instance, filename):
	return '/'.join(['portadas', instance.year.title_year, filename])



# Create your models here.

class Year(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title_year = models.CharField(max_length=4, unique=True)

	def __str__(self):
		return self.title_year


class Gender(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title_gender = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.title_gender


class Quality(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title_quality = models.CharField(max_length=10, unique=True)

	def __str__(self):
		return self.title_quality


class Movie(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title_movie = models.CharField(max_length=50, unique=True)
	release = models.BooleanField(default=False)
	year = models.ForeignKey(Year)
	gender = models.ManyToManyField(Gender)
	quality = models.ForeignKey(Quality)
	photo = models.ImageField(upload_to=content_file_name)
	data_movie = RichTextField()
	sinopsis = RichTextField()
	technical_data = RichTextField()
	links = models.TextField(default="<a href=' \# ' class='link' target='blank'> Descargar </a>")
	date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(editable=False)

	def save(self, *args, **kwargs):
		if self.id:
			self.slug = slugify(self.title_movie)
			super(Movie, self).save(*args, **kwargs)
		else:
			super(Movie, self).save(*args, **kwargs)


	def Gender(self):
		return ", " . join([gender.__str__() for gender in self.gender.all()])

	def portadas(self):
		return self.photo.url