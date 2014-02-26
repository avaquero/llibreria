from django.contrib import admin
from usuaris.models import Perfil
# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    fields = ('Perfil','PerfilAdmin',)

admin.site.register(Perfil, PerfilAdmin)