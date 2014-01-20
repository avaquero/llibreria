from django.shortcuts import render
from usuaris.models import Perfil

# Create your views here.

def llistatUsuaris(request):
    usuaris = Perfil.objects.all()
    context = {'usuaris':usuaris}
    return render(request, 'llistatUsuaris.html', context)