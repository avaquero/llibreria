# -*- encoding: utf-8 -*-
from django.shortcuts import render
from usuaris.models import Perfil
from usuaris.forms import formulariLogin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
# Create your views here.

def llistatUsuaris(request):
    usuaris = Perfil.objects.all()
    context = {'usuaris':usuaris}
    return render(request, 'llistatUsuaris.html', context)

def entrada(request):
    #Si el metode es POST m'ho en enviat a mi mateix vol dir que ja tinc dades per processar
    if request.method == 'POST': 
        form = formulariLogin(request.POST)
        #Si les dades entrades són correctes (compleixen el tipus de camp...) Procesem i redirigim a portada
        if form.is_valid():
            #Emmagatzemem les dades que es troben al diccioanri form.cleaned_data a les variables corresponents
            username = form.cleaned_data['usuari']
            password = form.cleaned_data['contrasenya']
            #Autenticar usuaris
            user = authenticate(username=username, password=password)
            #Si es tot correcte
            if user is not None:
                #Pot ser que l'usuari estigui descativat! s'ha de comprovar
                if user.is_active:
                    #Fem login
                    login(request, user)
                    messages.success(request, 'Login correcte')
                    next = request.GET.get('next','/')
                    return HttpResponseRedirect(next)
                    # Redirect to a success page.
                else:
                    messages.error(request, 'Compte desactivada, contacti amb l\'administrador')
            # Return a 'disabled account' error message
            else:
                messages.error(request, 'Ep! Hi ha hagut un error!')
        # Return an 'invalid login' error message.
            
        else:
            messages.error(request, 'Ep! Hi ha hagut un error!')
        #Si no es pots es GET i vol dir que no tenim dades a processar
    else:
        form = formulariLogin() 

    return render(request, 'login.html', {
        'form': form,
    })
#La funció logout fa login
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout correcte, a reveure')
    return HttpResponseRedirect('/')
    