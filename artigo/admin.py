from django.contrib import admin
from .models import Artigo, ArtigoAdmin
# Register your models here.

admin.site.site_header = 'Repositório FMB'
admin.site.register(Artigo, ArtigoAdmin)