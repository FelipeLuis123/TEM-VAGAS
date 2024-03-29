
from django.urls import path
from . import views

urlpatterns = [
    path('', views.destaques, name='main-page'),
    path('create-recommendation/', views.create_recommendation, name='create-recommendation'),
    path('recommendation-detail/<int:id>/', views.recommendation_detail, name='recommendation-detail'),
    path('recommendation-update/<int:id>/', views.recommendation_update, name='recommendation-update'),
    path('recommendation-delete/<int:id>/', views.recommendation_delete, name='recommendation-delete'),
    path('listar-recomendacoes/', views.listar_recomendacoes, name='listar-recomendacoes'),
    path('curtir_recomendacao/<int:id>/', views.curtir_recomendacao, name='curtir-recomendacao'),
    path('buscar-recomendacoes/', views.buscar_recomendacoes, name='buscar-recomendacoes'),
    path('adicionar-comentario/<int:id>/', views.adicionar_comentario, name='adicionar-comentario'),
    path('editar-comentario/<int:comentario_id>/', views.editar_comentario, name='editar-comentario'),
    path('excluir-comentario/<int:comentario_id>/', views.excluir_comentario, name='excluir-comentario'),
    path('meu-perfil/', views.my_profile, name='meu-perfil'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
    path('search/', views.search_recommendations, name='search-recommendations'),
    path('buscar-recomendacoes/<str:tipo_imovel>/', views.buscar_recomendacoes, name='buscar-recomendacoes'),
    path('favoritar_recomendacao/<int:id>/', views.favoritar_recomendacao, name='favoritar_recomendacao'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('excluir-conta/', views.excluir_conta, name='excluir_conta'),
    path('atualizar_perfil/', views.atualizar_perfil, name='atualizar_perfil'),
    ]


