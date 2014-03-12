# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from prestecs.models import Prestec, Solicitut_Prestec
from llibres.models import Llibre, Titol
from usuaris.models import Perfil
from prestecs.forms import FormPrestec, FormSolicitutPrestec
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import request
import datetime
from django.contrib.auth.models import User

@login_required
def llistatPrestecs(request):
    usuari = get_object_or_404(Perfil, pk = request.user.id)
    prestecs = Prestec.objects.filter(prestamista = usuari)
    mhanprestat = Prestec.objects.filter(beneficiari = usuari)
    context = {'prestecs':prestecs, 'mhanprestat':mhanprestat}
    return render(request, 'prestecs.html', context)


@login_required
def llistatMevesSolicituts(request):
    #Usuari actual
    usuari = get_object_or_404(Perfil, pk = request.user.id)
    #Prestecs dels que sóc el solicitants
    solicitud = Solicitut_Prestec.objects.filter(solicitant=usuari)
    paginator = Paginator(solicitud, 20) #Quantes solicituds volem mostrar
    page = request.GET.get('pagina') #('pagina') és el que s'assignara al get
    try:
        solicituds = paginator.page(page)
    except PageNotAnInteger:
        # Si la pagina no es un  numero l'enviem a la primera pagina
        solicituds = paginator.page(1)
    except EmptyPage:
        # Si no posa pagina li enviem a la primera... per correus... li enviaria a la ultima
        #contacts = paginator.page(paginator.num_pages) -- per enviar a la ultima pagina
        solicituds = paginator.page(1)
    #---------------------
    #Solicituds pendents d'acceptar
    llibresUsuari = Llibre()
    teLlibres = False
    try:
        titolsUsuari = Titol.objects.filter(llibre__propietari = usuari)
        teLlibres = True
    except Llibre.DoesNotExist:
        llibresUsuari = Llibre()
        teLlibres = False
    if(teLlibres):
        solicitud2 = Solicitut_Prestec.objects.filter(titol__in = titolsUsuari)
    else:
        solicitud = Solicitut_Prestec()
    context = {'solicituds':solicituds}
    return render(request, 'solicituds.html', context)

#@login_required
#def llistatSolicituds(request):
    #solicituds = Solicitut_Prestec.objects.all()
    #context = {'solicituds':solicituds}
    #return render(request, 'solicituds.html', context)

#@login_required
#def llistatSolicituds(request):
    #solicitud = Solicitut_Prestec.objects.all()
    #paginator = Paginator(solicitud, 2) #Quantes solicituds volem mostrar
    #page = request.GET.get('pagina') #('pagina') és el que s'assignara al get
    #try:
        #solicituds = paginator.page(page)
    #except PageNotAnInteger:
        # Si la pagina no es un  numero li en viem a la primera pagina
        #solicituds = paginator.page(1)
    #except EmptyPage:
        # Si no posa pagina li enviem a la primera... per correus... li enviaria a la ultima
        #contacts = paginator.page(paginator.num_pages) -- per enviar a la ultima pagina
        #solicituds = paginator.page(1)
    #context = {'solicituds':solicituds}
    #return render(request, 'solicituds.html', context)

@login_required
def novaSolicitut (request, idTitol):
    titolet = Titol.objects.get( id = idTitol )
    solicitant = get_object_or_404(Perfil, pk = request.user.id)
    solicitut = Solicitut_Prestec();
    llibres = Llibre.objects.filter(titol__id = titolet.id)
    comptador = False
    for llibre in llibres:
        #print llibre.estat
        if llibre.estat == "disponible" and comptador == False:
            #print "Llibre disponible"
            solicitut.dataSolicitut = datetime.datetime.now()
            
            solicitut.solicitant = solicitant
            solicitut.titol = llibre.titol
            solicitut.estat = "pendent"
            solicitut.save()
            llibre.estat = "pendent"
            llibre.save()
            comptador =  True
            messages.success(request, 'Solicitut enviada correctament')
            messages.success(request, 'Solicitut registrada a nom de '+solicitant.usuari.username+ " amb el llibre  "+ solicitut.titol.titol )
            return HttpResponseRedirect('/')
    
    messages.error(request,'El titol no té cap llibre disponible')
    return HttpResponseRedirect('/llibres')
        
@login_required
def retornarLlibre(request, idLlibre):
    llibre = get_object_or_404(Llibre, pk = idLlibre)
    if llibre.propietari == request.user.id:
        llibre.estat = 'disponible'
        messages.success(request, 'Llibre tornat correctament')
        return HttpResponseRedirect("{% url 'home' %}")
    else:
        messages.error(request, 'S\'ha produit un error al retornar el llibre')
        return HttpResponseRedirect("/llibres/fitxaLlibre/"+idLlibre)
        
