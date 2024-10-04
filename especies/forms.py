from django import forms
from .models import Especies


class EspeciesModelForm(forms.ModelForm):
    class Meta:
        model = Especies
        fields = [
            'nome_especie', 'imagem', 'introducao',
            'origem', 'causa_efeito', 'prevencao'
        ]
        widgets = {
            'nome_especie': forms.TextInput(
                attrs={'': ''}
            ),
            'imagem': forms.FileInput(
                attrs={'class': 'conteudo-especies__especie__imagem'}
            ),
            'introducao': forms.TextInput(
                attrs={
                    'style': ' height: 200px;' +
                    'text-align: center;' +
                    'justify-content: center;',
                }
            ),
            'origem': forms.TextInput(
                attrs={
                    'style': ' height: 200px;' +
                    'text-align: center;' +
                    'justify-content: center;',
                }
            ),
            'causa_efeito': forms.TextInput(
                attrs={
                    'style': ' height: 200px;' +
                    'text-align: center;' +
                    'justify-content: center;',
                }
            ),
            'prevencao': forms.TextInput(
                attrs={
                    'style': ' height: 200px;' +
                    'text-align: center;' +
                    'justify-content: center;',
                }
            )
        }
