from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from ..models import Year, Gender, Quality, Movie
from .serializer import MovieSerializer, GenderSerializer, YearSerializer, QualitySerializer


class GenderViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Gender.objects.all()
	serializer_class = GenderSerializer


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer


class QualityViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Quality.objects.all()
	serializer_class = QualitySerializer


class YearViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Year.objects.all()
	serializer_class = YearSerializer