from rest_framework import serializers
from ..models import Year, Gender, Quality, Movie


class GenderSerializer(serializers.ModelSerializer):

	class Meta:
		model = Gender


class MovieSerializer(serializers.ModelSerializer):
	year = serializers.ReadOnlyField(source='year.title_year')
	gender = serializers.SlugRelatedField(many=True, read_only=True,
                                          slug_field='title_gender')
	quality = serializers.ReadOnlyField(source='quality.title_quality')

	class Meta:
		model = Movie
		fields = ('id', 'title_movie', 'year', 'gender', 'quality', 'photo', 'data_movie', 'sinopsis', 'technical_data', 'links', 'date', 'slug')


class YearSerializer(serializers.ModelSerializer):

	class Meta:
		model = Year


class QualitySerializer(serializers.ModelSerializer):

	class Meta:
		model = Quality