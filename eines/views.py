# -*- encoding: utf-8 -*-
from django.shortcuts import render
from llibres.models import  Titol, Llibre
from django.contrib.redirects.models import Redirect
from httplib import HTTP
from eines.forms import BuscaForm
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def home(request):
    titols = Titol.objects.all()
    context = {'titols': titols}
    return render(request, 'home.html', context)


def xat(request):
    return render(request, 'xat.html')

def recerca(request):
    if request.method == 'POST':
        form = BuscaForm(request.POST)
        if form.is_valid():
            buscat = form.cleaned_data['busca']
            
            url_next = reverse('recerca')
            return HttpResponseRedirect( url_next + "?q=" + buscat)
        else:
            messages.error(request, "Ep! Busqueda no vàlida")
            return HttpResponseRedirect('/')
        
    else:    
        form = BuscaForm()   
        buscat = request.GET.get("q", '')
        llibres = Titol.objects.filter(titol__contains= buscat)
    return render(request, 'recerca.html', { 'formCerca': form, 'llibres':llibres })

