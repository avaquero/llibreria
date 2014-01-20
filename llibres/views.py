# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from llibres.models import Titol, Genere, Llibre
from django.http.response import HttpResponseRedirect
from llibres.forms import FormGenere
from django.contrib import messages




def index(request):
    llibres = Titol.objects.all()
    context = {'llibres': llibres}
    return render(request, 'index.html', context)

def fitxaLlibre(request, idLlibre):
    llibre = get_object_or_404(Llibre, pk=idLlibre)
    context = {'llibre': llibre}
    return render(request, 'fitxaLlibre.html', context)


def llistatGeneres(request):
    generes = Genere.objects.all()
    context = {'generes':generes}
    return render(request, 'generes.html', context)

def entradaGeneres(request, idGenere = None):
    #Si idGenere es None creem un nou genere, sinó editem
    if idGenere is not None:
        genere = get_object_or_404(Genere, pk=idGenere)
    else:
        genere = Genere()
    #Si el metode es POST tractem les dades
    if request.method == 'POST':
        form = FormGenere(request.POST, instance = genere)
        #Si les dades son correctes, les processem i redirigim a la llista de generes
        if form.is_valid():
            form.save()
            messages.success(request, 'Genere introduit correctament')
            return HttpResponseRedirect('/llibres/llistatGeneres')
        else:
            messages.error(request, 'Ep! Hi ha hagut un error al introduir un genere')
    #Si no es POST serà GET, mostrem el formulari buit
    else:
        form = FormGenere(instance=genere)
        
    return render(request, 'entradaGenere.html', {'form':form,})


