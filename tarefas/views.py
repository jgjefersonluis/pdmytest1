from django.shortcuts import render

from tarefas.models import Tarefas


def tarefas(request):
    tarefas = Tarefas.objects.all()
    context = {
        'tarefas': tarefas
    }

    return render(request, 'tarefas.html', context)