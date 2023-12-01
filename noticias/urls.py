from django.urls import path
from .views import (
    depoimento_cadastro,
    # depoimento_detalhe,
    depoimento_edicao,
    depoimento_exclusao,
    forum,
)


urlpatterns = [
    path('depoimentos/', depoimento_cadastro, name='depoimentos_cadastro'),
    # path('depoimentos/<int:id>/', depoimento_detalhe, name='depoimentos_detalhe'),
    path('depoimentos/<int:id>/edicao/', depoimento_edicao, name='depoimentos_edicao'),
    path('depoimentos/<int:id>/exclusao', depoimento_exclusao, name='depoimentos_exclusao'),
    path('forum/', forum, name='forum'),
]
