from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Year, Gender, Quality, Movie

# Create your views here.

class Home(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **Kwargs):
		context = super(Home, self).get_context_data(**Kwargs)
		context['quality'] = Quality.objects.all().order_by("-title_quality")
		context['years'] = Year.objects.all().order_by("-title_year")
		context['movies'] = Movie.objects.filter(premiere = True)[:8]
		genders = Gender.objects.all().order_by("title_gender")
		quantity = [ gender.movie_set.all().count() for gender in genders ]
		listGender = []
		for gender, cantidad in zip(genders, quantity):
			listGender.append((gender, cantidad))

		context['genders'] = listGender
		return context