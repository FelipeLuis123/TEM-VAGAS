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
]