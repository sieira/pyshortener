from django.urls import path

from core.views import liveness
from resolver.views import resolve

urlpatterns = [
    path('', liveness, name='liveness'),
    path('<str:short_url>', resolve, name='resolver'),
]
