from django.forms import ModelForm
from django.db import models
from prestecs.models import Solicitut_Prestec, Prestec

class FormSolicitutPrestec(ModelForm):
    class Meta:
        model = Solicitut_Prestec
        fields = ['dataSolicitut', 'solicitant','titol']

class FormPrestec(ModelForm):
    class Meta:
        model = Prestec
        fields = ['dataPrestec','beneficiari', 'prestamista', 'llibre', 'estat']