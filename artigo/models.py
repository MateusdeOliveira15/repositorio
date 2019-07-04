from django.db import models
from django.contrib import admin
import datetime

# Create your models here.
class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=250)
    palavras_chaves = models.CharField(max_length=500, blank=False, null=True)
    data_do_documento = models.CharField(max_length=100)
    editor = models.CharField(max_length=100)
    citacao = models.IntegerField()
    resumo = models.TextField()
    abstract = models.TextField()
    descricao = models.TextField()
    data_de_publicacao = models.DateField(default=datetime.date.today)

    link = models.CharField(max_length=999, blank=False, null=True)

    def __str__(self):
        return self.titulo

class ArtigoAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'autores', 'palavras_chaves',)
    date_hierarchy = 'data_de_publicacao'
    list_display = ('titulo', 'autores', 'data_de_publicacao')
    list_filter = ('editor', 'data_do_documento', 'data_de_publicacao')