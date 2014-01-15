from django.forms import ModelForm
from django.db import models

class FormSolicitutPrestec(ModelForm):
    class Meta:
        model = Solicitut_Prestec
        fields = ['dataSolicitut', 'solicitant','titol']