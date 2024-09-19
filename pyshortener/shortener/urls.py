from django.urls import path

from core.views import liveness

from shortener.views import shorten

urlpatterns = [
    path('liveness', liveness, name='liveness'),
    path('shorten', shorten, name='shorten'),
]
