from django.urls import path

from diario.views import diario

urlpatterns = [
    path('diario/', diario),
]