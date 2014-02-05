# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from prestecs.models import Prestec, Solicitut_Prestec
from prestecs.forms import FormPrestec, FormSolicitutPrestec
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def llistatPrestecs(request):
    prestecs = Prestec.objects.all()
    context = {'prestecs':prestecs}
    return render(request, 'prestecs.html', context)

@login_required
def llistatSolicituds(request):
    prestecs = Solicitut_Prestec.objects.all()
    context = {'solicituds':solicituds}
    return render(request, 'solicituds.html', context)

@login_required
def nouPrestec(request, idPrestec =  None):
    #Si idLlibre es None creem un nou llibre, sinó l'editem
    if idPrestec is not None:
        prestec = get_object_or_404(Prestec, pk = idPrestec)
    else:
        prestec = Prestec()
    #Si el metode es POST tractem les dades
    if request.method == 'POST':
        form = FormPrestec(request.POST, instance = prestec)
    #Si les dades son correctres, les procressem i redirigim a la llista de prestecs
        if form.is_valid():
            form.save()
            messages.success(request, 'Prestec introduit correctament')
            return HttpResponseRedirect('/prestecs')
        else:
            messages.error(request, "Ep! Hi ha hagut un error al introduir un prestec")
    #Si no es POST serà GET, mostrem el formulari buit
    else:
        form = FormPrestec(instance = prestec)
    return render(request, 'entrarPrestec.html', {'form':form,})

@login_required
def solicitudPrestec(request, idSolicitud =  None):
    #Si idLlibre es None creem un nou llibre, sinó l'editem
    if idSolicitud is not None:
        solicitud = get_object_or_404(Solicitut_Prestec, pk = idSolicitud)
    else:
        solicitud = Solicitut_Prestec()
    #Si el metode es POST tractem les dades
    if request.method == 'POST':
        form = FormSolicitutPrestec(request.POST, instance = solicitud)
    #Si les dades son correctres, les procressem i redirigim a la llista de prestecs
        if form.is_valid():
            form.save()
            messages.success(request, 'Prestec introduit correctament')
            return HttpResponseRedirect('/solicituds')
        else:
            messages.error(request, "Ep! Hi ha hagut un error al introduir un prestec")
    #Si no es POST serà GET, mostrem el formulari buit
    else:
        form = FormSolicitutPrestec(instance = solicitud)
    return render(request, 'solicitudPrestec.html', {'form':form,})
