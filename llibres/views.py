# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from llibres.models import Titol, Genere, Llibre
from django.http.response import HttpResponseRedirect
from llibres.forms import FormGenere, FormLlibre, FormTitol
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def index(request):
    llibres = Llibre.objects.all()
    context = {'llibres': llibres}
    return render(request, 'index.html', context)

def fitxaLlibre(request, idLlibre):
    llibre = get_object_or_404(Llibre, pk=idLlibre)
    context = {'llibre': llibre}
    return render(request, 'fitxaLlibre.html', context)

def fitxaTitol(request, idTitol):
    llibre = get_object_or_404(Llibre, pk=idTitol)
    context = {'llibre': llibre}
    return render(request, 'fitxaTitol.html', context)

@login_required
def entradaLlibre(request, idLlibre =  None):
    #Si idLlibre es None creem un nou llibre, sinó l'editem
    if idLlibre is not None:
        llibre = get_object_or_404(Llibre, pk = idLlibre)
    else:
        llibre = Llibre()
    #Si el metode es POST tractem les dades
    if request.method == 'POST':
        form = FormLlibre(request.POST, request.FILES, instance = llibre)
    #Si les dades son correctres, les procressem i redirigim a la llista de llibres
        if form.is_valid():
            form.save()
            messages.success(request, 'Llibre introduit correctament')
            return HttpResponseRedirect('/llibres')
        else:
            messages.error(request, "Ep! Hi ha hagut un error al introduir un llibre")
    #Si no es POST serà GET, mostrem el formulari buit
    else:
        form = FormLlibre(instance = llibre)
        
    camps_bootstrap = ('isbn', 'edicio', 'editorial', 'titol', 'propietari', 'estat', 'imatge')
    for c in camps_bootstrap:
        form.fields[c].widget.attrs['class'] = 'form-control'
    return render(request, 'entradaLlibre.html', {'form':form,})

def llistatGeneres(request):
    generes = Genere.objects.all()
    context = {'generes':generes}
    return render(request, 'generes.html', context)

@login_required
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

def llistatTitolsDeGenere(request, idGenere):
    #TODO No acabat!
    titols = get_object_or_404(Titol, genere = idGenere )
    genere = get_object_or_404(Genere, pk=idGenere)
    context = {'titols':titols, 'genere':genere}
    
    return render(request, 'llistaTitolsGenere.html', context)
@login_required
def entradaTitols(request, idTitol = None):
    #Si idGenere es None creem un nou genere, sinó editem
    if idTitol is not None:
        titol = get_object_or_404(Titol, pk=idTitol)
    else:
        titol = Titol()
    #Si el metode es POST tractem les dades
    if request.method == 'POST':
        form = FormTitol(request.POST, instance = titol)
        #Si les dades son correctes, les processem i redirigim a la llista de generes
        if form.is_valid():
            form.save()
            messages.success(request, 'Titol introduit correctament')
            return HttpResponseRedirect('/llibres/llistatTitols')
        else:
            messages.error(request, 'Ep! Hi ha hagut un error al introduir un titol')
    #Si no es POST serà GET, mostrem el formulari buit
    else:
        form = FormTitol(instance=titol)
        
    return render(request, 'entradaTitol.html', {'form':form,})

def llistatTitols(request):
    titols = Titol.objects.all()
    context = {'titols':titols}
    return render(request, 'llistatTitol.html', context)
