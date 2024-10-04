from django.contrib import admin
from .models import Depoimentos


@admin.register(Depoimentos)
class DepoimentosAdmin(admin.ModelAdmin):
    list_display = [
        'email', 'nome', 'relato',
        'depoimento_ou_discussao'
    ]
