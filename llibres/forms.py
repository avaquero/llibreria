from django.forms import ModelForm
from django.db import models

class FormGenere(ModelForm):
    class Meta:
        model = Genere
        fields = ['nom']

class FormTitol(ModelForm):
    class Meta:
        model = Titol
        fields = ['titol','sinopsis','genere']