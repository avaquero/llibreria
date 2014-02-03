from django.contrib import admin
from llibres.models import Genere, Titol, Llibre
# Register your models here.

class GenereAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genere, GenereAdmin)

class TitolAdmin(admin.ModelAdmin):
    pass
admin.site.register(Titol, TitolAdmin)

class LlibreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Llibre, LlibreAdmin)
