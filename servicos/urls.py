from django.urls import path

from servicos.views import servicos

urlpatterns = [
    path('servicos/', servicos),
]