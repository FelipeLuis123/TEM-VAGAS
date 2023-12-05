from django.shortcuts import get_object_or_404, render, redirect
from posts_app.models import recomendacoes
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from posts_app.forms import RecommendationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from .forms import ComentarioForm  # Certifique-se de importar o formulário de comentário
from django.shortcuts import get_object_or_404, render, redirect
from .models import Comentario

def destaques(request):
    # usuarioLogado(request)
    template_name = 'main-page.html'  # template
    posts = recomendacoes.objects.all()  # query com todas as postagens
    context = {  # cria context para chamar no template
        'imovel': posts  # o primeiro 'posts' é o nome como ele vai ser chamado no html.
    }
    return render(request, template_name, context)  # render

@login_required
def create_recommendation(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST, request.FILES)
        if form.is_valid():
            recommendation = form.save(commit=False)  # Cria instância, mas não salva no banco de dados ainda
            recommendation.owner = request.user  # associando o usuário logado como o proprietário
            recommendation.save()  # Salva a instância no banco de dados

            messages.success(request, 'A recomendação foi criada com sucesso')
            return redirect('main-page')  # Utilizando redirect ao invés de HttpResponseRedirect
    else:
        form = RecommendationForm()  # Inicializa o formulário para ser apresentado na página

    return render(request, 'recommendation-form.html', {"form": form})

@login_required
def recommendation_detail(request, id):
    # usuarioLogado(request)
    template_name = 'recommendation-detail.html'  # template
    post = recomendacoes.objects.get(id=id)  # Metodo Get
    context = {  # cria context para chamar no template
        'imovel': post
    }
    return render(request, template_name, context)  # render

def recommendation_update(request, id):
    recommendation = get_object_or_404(recomendacoes, id=id)
    
    # Verificar se o usuário logado é o proprietário da recomendação
    if request.user != recommendation.owner:
        return HttpResponseForbidden('Você não tem permissão para editar esta recomendação.')

    if request.method == 'POST':
        form = RecommendationForm(request.POST, request.FILES, instance=recommendation)
        if form.is_valid():
            form.save()
            
            messages.warning(request, 'A recomendação foi atualizada com sucesso')
            return HttpResponseRedirect(reverse('recommendation-detail', args=[recommendation.id]))

    form = RecommendationForm(instance=recommendation)
    return render(request, 'recommendation-form.html', {"form": form})

def recommendation_delete(request, id):
    recommendation = get_object_or_404(recomendacoes, id=id)

    # Verificar se o usuário logado é o proprietário da recomendação
    if request.user != recommendation.owner:
        return HttpResponseForbidden('Você não tem permissão para excluir esta recomendação.')

    if request.method == 'POST':         
        recommendation.delete()
        
        messages.error(request, 'A recomendação foi excluída com sucesso')
        return HttpResponseRedirect(reverse('main-page'))

    return render(request, 'recommendation-delete.html')

def mysite(request):
    # usuarioLogado(request)
    return render(request, 'main-page.html')

@login_required
def listar_recomendacoes(request):
    # Recupere o usuário logado
    usuario_logado = request.user

    # Recupere todas as recomendações feitas pelo usuário
    recomendacoes_do_usuario = recomendacoes.objects.filter(owner=usuario_logado)

    # Passe as recomendações para o template
    context = {'recomendacoes': recomendacoes_do_usuario}
    return render(request, 'listar_recomendacoes.html', context)

@login_required
def curtir_recomendacao(request, id):
    recomendacao = get_object_or_404(recomendacoes, id=id)

    # Verificar se o usuário já curtiu a recomendação
    if request.user in recomendacao.curtidas.all():
        recomendacao.curtidas.remove(request.user)
        mensagem = 'Curtida removida'
    else:
        recomendacao.curtidas.add(request.user)
        mensagem = 'Recomendação curtida'

    # Retornar uma resposta JSON indicando o número atual de curtidas
    numero_curtidas = recomendacao.curtidas.count()
    data = {'mensagem': mensagem, 'numero_curtidas': numero_curtidas}
    return JsonResponse(data)

@login_required
def buscar_recomendacoes(request):
    query = request.GET.get('q')

    if query:
        resultados = recomendacoes.objects.filter(
            Q(bairro__icontains=query) |  
            Q(endereco__icontains=query)| 
            Q(valor_aluguel__icontains=query) |  
            Q(quantidade_quartos__icontains=query)|  
            Q(quantidade_banheiros__icontains=query) |  
            Q(tipo_imovel__icontains=query)  |
            Q(logradouro__icontains=query) |  
            Q(descricao__icontains=query)| 
            Q(cep__icontains=query) |  
            Q(numero__icontains=query)|  
            Q(estado__icontains=query) 
          
            
            
            # Adicione mais condições se necessário
        ).distinct()

        context = {
            'query': query,
            'resultados': resultados
        }

        return render(request, 'resultados_busca.html', context)
    else:
        return render(request, 'resultados_busca.html', {'resultados': None})
    
@login_required
def adicionar_comentario(request, id):
    imovel = get_object_or_404(recomendacoes, id=id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.recomendacao = imovel
            comentario.save()
            messages.success(request, 'Comentário adicionado com sucesso.')
            
            # Modificação aqui - redirecionar para recommendation-detail
            return HttpResponseRedirect(reverse('recommendation-detail', kwargs={'id': imovel.id}))

    else:
        form = ComentarioForm()

    return render(request, 'adicionar_comentario.html', {'form': form, 'imovel': imovel})

@login_required
def editar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    # Verificar se o usuário logado é o autor do comentário
    if request.user != comentario.usuario:
        messages.error(request, 'Você não tem permissão para editar este comentário.')
        return redirect('recommendation-detail', id=comentario.recomendacao.id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comentário editado com sucesso.')
            return redirect('recommendation-detail', id=comentario.recomendacao.id)
    else:
        form = ComentarioForm(instance=comentario)

    return render(request, 'editar_comentario.html', {'form': form, 'comentario': comentario})

@login_required
def excluir_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    # Verificar se o usuário logado é o autor do comentário
    if request.user != comentario.usuario:
        messages.error(request, 'Você não tem permissão para excluir este comentário.')
        return redirect('recommendation-detail', id=comentario.recomendacao.id)

    if request.method == 'POST':
        comentario.delete()
        messages.success(request, 'Comentário excluído com sucesso.')
        return redirect('recommendation-detail', id=comentario.recomendacao.id)

    return render(request, 'excluir_comentario.html', {'comentario': comentario})

@login_required
def my_profile(request):
    return render(request, 'my_profile.html')

# Aqui começa a seção de código comentado
# def usuarioLogado(request):
#     print('Logado')
#     if request.user.is_authenticated:
#         print('Authenticated')
#         render(request, "main-page.html") 
#         return 200 
#     else:
#         render(request, "accounts/templetes/login.html")
#         return 401

# filtragem por palavras similares que estão dando erro ainda
# def buscar_recomendacoes(request):
#     query = request.GET.get('q', '')
#     ...
#     # Continuação do código comentado

@login_required
def sobre_nos(request):
    return render(request, 'sobre_nos.html')
