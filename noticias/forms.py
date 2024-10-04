from django import forms
from .models import Depoimentos


class DepoimentosModelForm(forms.ModelForm):
    class Meta:
        model = Depoimentos
        fields = [
            'email', 'nome', 'relato',
            'depoimento_ou_discussao'
        ]
        widgets = {
            'email': forms.EmailInput(
                attrs={'id': 'id-email', 'placeholder': 'Digite seu email'}
            ),
            'nome': forms.TextInput(
                attrs={'id': 'id-nome', 'placeholder': 'Digite seu nome'}
            ),
            'relato': forms.TextInput(
                attrs={
                    'style': ' height: 200px;' +
                    'text-align: center;' +
                    'justify-content: center;',

                    'id': 'id-senha-confirm'
                }
            ),
            'depoimento_ou_discussao': forms.Select(
                attrs={'id': 'id-assunto'}
            ),
        }
