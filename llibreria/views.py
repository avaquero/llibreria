from django.shortcuts import render

from django.http import HttpResponse
from llibres.models import Titol, Genere
def home(request):
    
    return render(request, 'home.html')