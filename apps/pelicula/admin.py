from django.contrib import admin
from .models import Year, Gender, Quality, Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
	list_display = ('title_movie', 'premiere', 'Gender', 'year', 'quality', 'date', 'mi_portada')
	list_filter = ('quality', 'year', 'gender', 'premiere')
	search_fields = ('gender__title_gender', 'title_movie', 'year__title_year', 'quality__title_quality')
	filter_horizontal = ('gender',)

	def mi_portada(self, obj):
		url = obj.portadas()
		tag = '<img src="%s" width="100"/>' % url
		return tag
	mi_portada.allow_tags = True
	mi_portada.admin_order_field = 'photo'


admin.site.register(Year)
admin.site.register(Gender)
admin.site.register(Quality)
admin.site.register(Movie, MovieAdmin)