from django.contrib import admin
from .models import Destino
from cms.admin.placeholderadmin import PlaceholderAdminMixin
# Register your models here.

class MyModelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Destino,MyModelAdmin)
