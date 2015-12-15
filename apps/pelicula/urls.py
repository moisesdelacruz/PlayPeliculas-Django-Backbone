from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from .api.viewSet import MovieViewSet, GenderViewSet, QualityViewSet, YearViewSet
from .views import Home

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'year', YearViewSet)
router.register(r'quality', QualityViewSet)
router.register(r'gender', GenderViewSet)


urlpatterns = [
    url(r'^$', Home.as_view()),
    url(r'^movie/(?P<slug>[-\ \w]+)/$', Home.as_view()),
    url(r'^api/', include(router.urls)),
]
