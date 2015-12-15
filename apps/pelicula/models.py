from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Year(models.Model):
	title_year = models.CharField(max_length=4)

	def __str__(self):
		return self.title_year


class Gender(models.Model):
	title_gender = models.CharField(max_length=20)

	def __str__(self):
		return self.title_gender


class Quality(models.Model):
	title_quality = models.CharField(max_length=10)

	def __str__(self):
		return self.title_quality


class Movie(models.Model):
	title_movie = models.CharField(max_length=50)
	release = models.BooleanField(default=False)
	year = models.ForeignKey(Year)
	gender = models.ManyToManyField(Gender)
	quality = models.ForeignKey(Quality)
	trailer = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='portada/')
	data_movie = RichTextField()
	sinopsis = RichTextField()
	technical_data = RichTextField()
	links = models.TextField(default="<a href=' \# ' class='link' target='blank'> Descargar </a>")
	date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(editable=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title_movie)
			super(Movie, self).save(*args, **kwargs)
		else:
			super(Movie, self).save(*args, **kwargs)


	def Gender(self):
		return ", " . join([gender.__str__() for gender in self.gender.all()])

	def portadas(self):
		return self.photo.url