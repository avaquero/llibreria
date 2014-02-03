from django import  forms

class formulariLogin(forms.Form):
    usuari = forms.CharField(max_length=100)
    contrasenya = forms.CharField(max_length=100, widget=forms.PasswordInput() )
    