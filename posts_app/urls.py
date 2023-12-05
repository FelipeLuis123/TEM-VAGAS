from django.urls import path
from . import views

urlpatterns = [
    path('', views.destaques, name='main-page'),
    path('create-recommendation', views.create_recommendation, name='create-recommendation'),
    path('recommendation-detail/<int:id>/', views.recommendation_detail, name='recommendation-detail'),
    path('recommendation-update/<int:id>', views.recommendation_update, name='recommendation-update'),
    path('recommendation-delete/<int:id>/', views.recommendation_delete, name='recommendation-delete'),
    path('listar-recomendacoes/', views.listar_recomendacoes, name='listar-recomendacoes'),
    path('curtir_recomendacao/<int:id>/', views.curtir_recomendacao, name='curtir_recomendacao'),
    path('buscar-recomendacoes/', views.buscar_recomendacoes, name='buscar-recomendacoes'),
    path('adicionar-comentario/<int:id>/', views.adicionar_comentario, name='adicionar-comentario'),
    path('editar-comentario/<int:comentario_id>/', views.editar_comentario, name='editar-comentario'),
    path('excluir-comentario/<int:comentario_id>/', views.excluir_comentario, name='excluir-comentario'),
    path('meu-perfil', views.my_profile, name='meu-perfil'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
]