from django.shortcuts import get_object_or_404, render
from posts_app.models import recomendacoes
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from posts_app.forms import RecommendationForm

# Create your views here.
def destaques(request):
    template_name = 'main-page.html' # template
    posts = recomendacoes.objects.all() # query com todas as postagens
    context = { # cria context para chamar no template
        'imovel': posts # o primeiro 'posts' é o nome como ele vai ser chamado no html.
        }
    return render(request, template_name, context) # render

def create_recommendation(request):
    if request.method == 'POST': # para metodo POST
        form = RecommendationForm(request.POST, request.FILES) # pega as informações do form
        if form.is_valid(): # se for valido
            form = form.save(commit=False)
            form.save() # salva
            
            messages.success(request, 'A recomendação foi criada com sucesso') # mensagem quando cria o post
            return HttpResponseRedirect(reverse('main-page')) # coloquei para retornar post-list
        
    form = RecommendationForm() # senão carrega o formulario  
    return render(request, 'recommendation-form.html', {"form": form}) # nesse template

def recommendation_detail(request, id):
    template_name = 'recommendation-detail.html' # template
    post = recomendacoes.objects.get(id=id) # Metodo Get
    context = { # cria context para chamar no template
        'imovel': post
        }
    return render(request, template_name, context) # render

def recommendation_update(request, id):
    post = get_object_or_404(recomendacoes, id=id) # id do post
    form = RecommendationForm(request.POST or None, request.FILES or None, instance=post) # pega as informações do form
    if form.is_valid(): # se for valido
        form.save() # salva
        
        messages.warning(request, 'A recomendação foi atualizada com sucesso') # mensagem quando cria o post
        return HttpResponseRedirect(reverse('recommendation-detail', args=[post.id])) # coloquei para retornar post-list
         
    return render(request, 'recommendation-form.html', {"form": form}) # nesse template

def recommendation_delete(request, id): 
    post = recomendacoes.objects.get(id=id) # pelo ID pega o objeto
    if request.method == 'POST':         
        post.delete()
        messages.error(request, 'A recomendação foi excluida com sucesso') # quando deleta post 
        return HttpResponseRedirect(reverse('main-page')) # retorna rota post-list
    return render(request, 'recommendation-delete.html') # nesse template

def mysite(request):
    return render(request, 'main-page.html')
