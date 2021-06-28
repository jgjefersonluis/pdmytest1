from django.urls import path

from tarefas.views import tarefas

urlpatterns = [
    path('tarefas/', tarefas),
]