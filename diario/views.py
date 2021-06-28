from django.shortcuts import render
from diario.models import Diario


def diario(request):
    diario = Diario.objects.all()
    context = {
        'diario': diario
    }

    return render(request, 'diario.html', context)
