from django.forms import ModelForm
from django.db import models
from llibres.models import Genere, Titol


class FormGenere(ModelForm):
    class Meta:
        model = Genere
        fields = ['nom']

class FormTitol(ModelForm):
    class Meta:
        model = Titol
        fields = ['titol','sinopsis','genere']