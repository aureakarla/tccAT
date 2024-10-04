from django.contrib import admin
from .models import Especies


@admin.register(Especies)
class EspeciesAdmin(admin.ModelAdmin):
    list_display = [
        'nome_especie', 'imagem', 'introducao',
        'origem', 'causa_efeito', 'prevencao'
    ]
