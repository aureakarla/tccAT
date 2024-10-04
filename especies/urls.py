from django.urls import path
from .views import (
    especies_listagem, detalhe_especies,
    especies_cadastro, especies_edicao,
    especies_exclusao,
)


urlpatterns = [
    path('', especies_listagem, name='listagem_especies'),
    path('detalhe/<int:id>/', detalhe_especies, name='detalhe_especies'),
    path('cadastro/', especies_cadastro, name='especies_cadastro'),
    path('edicao/<int:id>/', especies_edicao, name='especies_edicao'),
    path('exclusao/<int:id>/', especies_exclusao, name='especies_exclusao'),
]
