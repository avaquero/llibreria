from django.contrib import admin
from usuaris.models import Perfil
# Register your models here.
class PerfilAdmin(admin.ModelAdmin):
    pass

admin.site.register(Perfil, PerfilAdmin)