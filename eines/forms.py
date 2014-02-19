from django import forms

class BuscaForm(forms.Form):
    busca = forms.CharField(max_length=100)