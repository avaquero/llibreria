# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from prestecs.models import Prestec, Solicitut_Prestec
from prestecs.forms import FormPrestec
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib import messages


def llistatPrestecs(request):
    prestecs = Prestec.objects.all()
    context = {'prestecs':prestecs}
    return render(request, 'prestecs.html', context)

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
