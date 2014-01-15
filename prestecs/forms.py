from django.forms import ModelForm
from django.db import models

class FormPrestec():
    class Meta:
        model = Prestec
        fields = ['dataPrestec', 'beneficiari', 'prestamista','llibre']

class FormSolicitutPrestec(ModelForm):
    class Meta:
        model = Solicitut_Prestec
        fields = ['dataSolicitut', 'solicitant','titol']