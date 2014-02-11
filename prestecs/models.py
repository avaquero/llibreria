from django.db import models
from usuaris.models import Perfil
from llibres.models import Llibre, Titol
import datetime
from django.utils import timezone


class Prestec(models.Model):
    dataPrestec = models.DateTimeField(default=timezone.now)
    beneficiari = models.ForeignKey(Perfil, related_name='prectecBeneficiari_set')
    prestamista = models.ForeignKey(Perfil, related_name='prestecPrestamista_set')
    llibre = models.OneToOneField(Llibre)
    dataTornada = models.DateTimeField(null=True)
    

class Solicitut_Prestec(models.Model):
    dataSolicitut = models.DateTimeField(default=timezone.now)
    solicitant = models.ForeignKey(Perfil, related_name='solicitant_set')
    titol = models.OneToOneField(Titol)