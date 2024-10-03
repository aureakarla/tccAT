from django.shortcuts import get_object_or_404, redirect, render
from .forms import EspeciesModelForm
from .models import Especies
from django.contrib.auth.decorators import login_required


def especies_listagem(request):
    display_type = request.GET.get('display_type', 'cards')  # Padrão para 'cards' se não estiver definido

    if display_type == 'cards':
        especies = Especies.objects.all().order_by('nome_especie')
        template_name = 'especies/lista_especies.html'
    elif display_type == 'list':
        especies = Especies.objects.all().order_by('nome_especie')
        template_name = 'especies/lista_especies.html'  # Altere para o nome correto do template de listagem
    else:
        # Trate outros valores, se necessário
        especies = Especies.objects.all().order_by('nome_especie')
        template_name = 'especies/lista_especies.html'

    context = {
        'especies': especies,
        'display_type': display_type,
    }

    return render(request, 'especies/lista_especies.html', context)



@login_required(login_url='/users/accounts/login/')
def especies_cadastro(request):
    if request.method == 'POST':
        form = EspeciesModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = EspeciesModelForm(request.POST, request.FILES)
    else:
        form = EspeciesModelForm()

    context = {'form': form}
    return render(request, 'especies/especies_cadastro.html', context)


@login_required(login_url='/users/accounts/login/')
def especies_edicao(request, id):
    especies = get_object_or_404(Especies, id=id)
    if request.method == 'POST':
        form = EspeciesModelForm(request.POST, request.FILES, instance=especies)
        if form.is_valid():
            form.save()
            return redirect('listagem_especies')
    else:
        form = EspeciesModelForm(instance=especies)

    context = {'form': form}
    return render(request, 'especies/especies_cadastro.html', context)



@login_required(login_url='/users/accounts/login/')
def especies_exclusao(request, id):
    especies = get_object_or_404(Especies, id=id)

    if request.method == 'POST':
        especies.delete()
        return redirect('listagem_especies')

    return render(request, 'especies/especies_exclusao.html')


def detalhe_especies(request, id):
    especies = get_object_or_404(Especies, id=id)
    context = {'especies': especies}
    return render(request, 'especies/detalhe_especies.html', context)
