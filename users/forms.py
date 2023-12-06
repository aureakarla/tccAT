from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'id-email',
                'style': 'outline: #f6f6f6',
                'placeholder': 'Digite aqui seu usuário',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'id-password',
                'style': 'outline: #f6f6f6',
                'placeholder': 'Digite aqui sua senha'
            },
        ),
    )


class CadastroModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': '',
                    'placeholder': 'Digite seu nome de usuario',
                    'id': 'id-nome'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': '',
                    'placeholder': 'Digite seu e-mail',
                    'id': 'id-email',
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': '',
                    'id': 'id-senha',
                    'placeholder': 'Digite sua senha'
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': '',
                    'id': 'id-senha-confirm',
                    'placeholder': 'Confirme sua senha'
                }
            ),
        }
