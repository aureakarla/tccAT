from django.urls import path
from .views import cadastro, logout_, login_

urlpatterns = [
    path('accounts/cadastro/', cadastro, name='cadastro'),
    path('accounts/login/', login_, name='login'),
    path('accounts/logout/', logout_, name='logout'),
]
