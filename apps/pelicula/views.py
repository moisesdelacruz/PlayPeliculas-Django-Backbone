from django.shortcuts import render
from django.views.generic import TemplateView#, ListView, DetailView, FormView, CreateView
from .models import Year, Gender, Quality, Movie
from datetime import datetime

# Create your views here.

class Home(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **Kwargs):
		context = super(Home, self).get_context_data(**Kwargs)
		context['quality'] = Quality.objects.all().order_by("-title_quality")
		context['years'] = Year.objects.all().order_by("-title_year")
		context['movies'] = Movie.objects.all().order_by('-date')[:8]
		genders = Gender.objects.all().order_by("title_gender")
		quantity = [ gender.movie_set.all().count() for gender in genders ]
		context['genders'] = genders
		now = datetime.now()
		context['date'] = now
		return context