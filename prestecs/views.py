from django.shortcuts import render, get_object_or_404
from prestecs.models import Prestec

def llistatPrestecs(request):
    prestecs = Prestec.objects.all()
    context = {'prestecs':prestecs}
    return render(request, 'prestecs.html', context)
