from django.shortcuts import render

from clientes.models import Clientes


def clientes(request):
    clientes = Clientes.objects.all()
    context = {
        'clientes': clientes
    }

    return render(request, 'clientes.html', context)