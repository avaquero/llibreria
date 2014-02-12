from django.contrib import admin
from llibres.models import Genere, Titol, Llibre
# Register your models here.

class GenereAdmin(admin.ModelAdmin):
    fields = ('nom',)

admin.site.register(Genere, GenereAdmin)

class TitolAdmin(admin.ModelAdmin):
    fields = ('titol','sinopsis','genere','idioma')
admin.site.register(Titol, TitolAdmin)

class LlibreAdmin(admin.ModelAdmin):
    fields = ('isbn','edicio','editorial','titol','propietari','estat','imatge')
admin.site.register(Llibre, LlibreAdmin)
