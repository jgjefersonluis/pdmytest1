from django.shortcuts import render

from servicos.models import Servicos


def servicos(request):
    servicos = Servicos.objects.all()
    context = {
        'servicos': servicos
    }

    return render(request, 'servicos.html', context)


