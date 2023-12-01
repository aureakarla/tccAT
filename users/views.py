from django.shortcuts import render, redirect
from .forms import LoginForm, CadastroModelForm
from django.contrib.auth import authenticate, login, logout


def cadastro(request):
    if request.method == 'POST':
        form = CadastroModelForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.is_staff = True
            user.save()

            return redirect('login')

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
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')

    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def logout_(request):
    logout(request)
    return redirect('login')
