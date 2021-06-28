import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    return render(request, 'index.html', data)

def error404(request, exception):
    template = loader.get_template('error404.html')
    return HttpResponse(content=template.render(), content_type='text/thml; charset=utf8', status=404)

def error500(request, exception):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
