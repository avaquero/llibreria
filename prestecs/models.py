from django.db import models
from usuaris.models import Perfil
from llibres.models import Llibre, Titol

ESTATS_LLIBRES_CHOICES = (
    ('disponible', 'Disponible'),
    ('pendent', 'Pendent d\'intercanvi'),
    ('prestat', 'Prestat'),
)


class Prestec(models.Model):
    dataPrestec = models.DateTimeField()
    beneficiari = models.ForeignKey(Perfil, related_name='prectecBeneficiari_set')
    prestamista = models.ForeignKey(Perfil, related_name='prestecPrestamista_set')
    llibre = models.OneToOneField(Llibre)
    estat = models.CharField(max_length=20, choices=ESTATS_LLIBRES_CHOICES)

class Solicitut_Prestec(models.Model):
    dataSolicitut = models.DateTimeField()
    solicitant = models.ForeignKey(Perfil, related_name='solicitant_set')
    titol = models.OneToOneField(Titol)