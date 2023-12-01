from django.shortcuts import get_object_or_404, render, redirect
from .forms import DepoimentosModelForm
from .models import Depoimentos
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'noticias/index.html')


def forum(request):
    depoimentos = Depoimentos.objects.filter(depoimento_ou_discussao='depoimento')
    discussoes = Depoimentos.objects.filter(depoimento_ou_discussao='discussao')
    context = {'depoimentos': depoimentos, 'discussoes': discussoes}
    return render(request, 'noticias/forum.html', context)


@login_required(login_url='/users/accounts/login/')
def depoimento_cadastro(request):
    if request.method == 'POST':
        form = DepoimentosModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = DepoimentosModelForm()
            return redirect('forum')
        else:
            form = DepoimentosModelForm(request.POST)
    else:
        form = DepoimentosModelForm()
    context = {'form': form}
    return render(request, 'noticias/depoimentos_cadastro.html', context)


@login_required(login_url='/users/accounts/login/')
def depoimento_edicao(request, id):
    depoimento = get_object_or_404(Depoimentos, id=id)

    if request.method == 'POST':
        form = DepoimentosModelForm(request.POST, request.FILES, instance=depoimento)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DepoimentosModelForm(instance=depoimento)

    context = {'form': form}
    return render(request, 'noticias/depoimentos_cadastro.html', context)


@login_required(login_url='/users/accounts/login/')
def depoimento_exclusao(request, id):
    depoimento = get_object_or_404(Depoimentos, id=id)

    if request.method == 'POST':
        depoimento.delete()
        return redirect('forum')

    return render(request, 'noticias/depoimentos_exclusao.html')


def depoimento_detalhe(request, id=id):
    depoimento = get_object_or_404(Depoimentos, id=id)
    context = {'depoimentos': depoimento}
    return render(request, 'noticias/depoimentos.html', context)
