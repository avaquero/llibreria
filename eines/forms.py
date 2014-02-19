# -*- encoding: utf-8 -*-
from django import forms

class BuscaForm(forms.Form):
    busca = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Recerca per títol'}))