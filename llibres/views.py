from django.shortcuts import render

from django.http import HttpResponse
from llibres.models import Titol
def index(request):
    llibres = Titol.objects.all()
    context = {'llibres': llibres}
    return render(request, 'index.html', context)
