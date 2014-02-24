# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from prestecs.models import Prestec, Solicitut_Prestec
from llibres.models import Llibre
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
    prestecs = Prestec.objects.all()
    context = {'prestecs':prestecs}
    return render(request, 'prestecs.html', context)


#@login_required
#def llistatSolicituds(request):
    #solicituds = Solicitut_Prestec.objects.all()
    #context = {'solicituds':solicituds}
    #return render(request, 'solicituds.html', context)

@login_required
def llistatSolicituds(request):
    solicitud = Solicitut_Prestec.objects.all()
    paginator = Paginator(solicitud, 2) #Quantes solicituds volem mostrar
    page = request.GET.get('pagina') #('pagina') és el que s'assignara al get
    try:
        solicituds = paginator.page(page)
    except PageNotAnInteger:
        # Si la pagina no es un  numero li en viem a la primera pagina
        solicituds = paginator.page(1)
    except EmptyPage:
        # Si no posa pagina li enviem a la primera... per correus... li enviaria a la ultima
        #contacts = paginator.page(paginator.num_pages) -- per enviar a la ultima pagina
        solicituds = paginator.page(1)
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
            prestamista = form.cleaned_data['prestamista']
            beneficiari = form.cleaned_data['beneficiari']
            llibre = form.cleaned_data['llibre']
                 
            if prestamista != beneficiari:
                if llibre.estat == "disponible":
                    form.save()
                    messages.success(request, 'Prestec introduit correctament')
                    return HttpResponseRedirect('/prestecs')
                else:
                   messages.error(request,'El llibre no esta disponible') 
            else:
                messages.error(request,'El beneficiari i el prestamista no poden ser el mateix')
        else:
            messages.error(request, "Ep! Hi ha hagut un error al introduir un prestec")
    #Si no es POST serà GET, mostrem el formulari buit
    else:
        form = FormPrestec(instance = prestec)
        
    camps_bootstrap = ('dataPrestec','beneficiari', 'prestamista', 'llibre')
    for c in camps_bootstrap:
        form.fields[c].widget.attrs['class'] = 'form-control'
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
            messages.success(request, 'Solicitud introduïda correctament')
            return HttpResponseRedirect('/solicituds')
        else:
            messages.error(request, "Ep! Hi ha hagut un error al introduir una solicitud")
    #Si no es POST serà GET, mostrem el formulari buit
    else:
        form = FormSolicitutPrestec(instance = solicitud)
    return render(request, 'solicitudPrestec.html', {'form':form,})

@login_required
def novaSolicitut (request, idLlibre):
    llibre = Llibre.objects.get( id = idLlibre )
    solicitant = get_object_or_404(Perfil, pk = request.user.id)
    solicitut = Solicitut_Prestec();
    
    if llibre.estat == "disponible":
        solicitut.dataSolicitut = datetime.datetime.now()
        solicitut.solicitant = solicitant
        solicitut.titol = llibre.titol
        solicitut.save()
        llibre.estat = "pendent"
        llibre.save()
        messages.success(request, 'Solicitut enviada correctament')
        return HttpResponseRedirect('/')
    else:
        messages.error(request,'El llibre no esta disponible')
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
        
