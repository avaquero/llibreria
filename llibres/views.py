from django.shortcuts import render

from django.http import HttpResponse
from llibres.models import Titol, Genere
def index(request):
    llibres = Titol.objects.all()
    context = {'llibres': llibres}
    return render(request, 'index.html', context)

def generes(request):
    generes = Genere.objects.all()
    context = {'generes':generes}
    return render(request, 'generes.html', context)
