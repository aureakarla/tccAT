from django.shortcuts import render, redirect
from .forms import LoginForm, CadastroModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def cadastro(request):
    if request.method == 'POST':
        form = CadastroModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Cadastro realizado com sucesso.")
            return redirect('login')
        else:
            messages.error(request, "Erro no cadastro. Verifique os dados e tente novamente.")
    else:
        form = CadastroModelForm()

    context = {
        'form': form
    }
    return render(request, 'users/cadastro.html', context)

def login_(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login realizado com sucesso.")
                return redirect('index')
            else:
                messages.error(request, "Usuário ou senha incorretos.")
        else:
            messages.error(request, "Erro no formulário. Verifique os dados e tente novamente.")
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

def logout_(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso.")
    return redirect('login')
