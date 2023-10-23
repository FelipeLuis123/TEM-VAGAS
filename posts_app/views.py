from django.shortcuts import get_object_or_404, render, redirect
from posts_app.models import recomendacoes
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from posts_app.forms import RecommendationForm

# Create your views here.
def destaques(request):
    # usuarioLogado(request)
    template_name = 'main-page.html' # template
    posts = recomendacoes.objects.all() # query com todas as postagens
    context = { # cria context para chamar no template
        'imovel': posts # o primeiro 'posts' é o nome como ele vai ser chamado no html.
        }
    return render(request, template_name, context) # render

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
def recommendation_detail(request, id):
    # usuarioLogado(request)
    template_name = 'recommendation-detail.html' # template
    post = recomendacoes.objects.get(id=id) # Metodo Get
    context = { # cria context para chamar no template
        'imovel': post
        }
    return render(request, template_name, context) # render

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


# def usuarioLogado(request):
#     print('Logado')
#     if request.user.is_authenticated:
#         print('Authenticated')
#         render(request, "main-page.html") 
#         return 200 
#     else:
#         render(request, "accounts/templetes/login.html")
#         return 401
