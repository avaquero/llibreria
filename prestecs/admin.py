from django.contrib import admin
from prestecs.models import Prestec, Solicitut_Prestec
# Register your models here.

class PrestecAdmin(admin.ModelAdmin):
    pass

admin.site.register(Prestec, PrestecAdmin)

class Solicitut_PrestecAdmin(admin.ModelAdmin):
    pass

admin.site.register(Solicitut_Prestec, Solicitut_PrestecAdmin)


