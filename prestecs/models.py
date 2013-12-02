from django.db import models
from usuaris.models import Perfil
from llibres.models import Llibre

class Prestec(models.Model):
    dataPrestec = models.DateTimeField()
    beneficiari = models.ForeignKey(Perfil, related_name='prectecBeneficiari_set')
    prestamista = models.ForeignKey(Perfil, related_name='prestecPrestamista_set')
    llibre = models.OneToOneField(Llibre)
